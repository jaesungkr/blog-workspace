const fs = require("node:fs");
const path = require("node:path");
const { pathToFileURL } = require("node:url");
const { chromium } = require("playwright");

async function main() {
  const qaDir = __dirname;
  const source = path.join(
    qaDir,
    "dark-remote-rendered",
    "gyeonggi-finance-crisis-fact-check-rich-preview.html",
  );
  const outputDir = path.join(qaDir, "dark-remote");
  fs.mkdirSync(outputDir, { recursive: true });
  const browser = await chromium.launch({
    executablePath: "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    headless: true,
  });
  const observations = [];
  try {
    for (const viewport of [
      { width: 1280, height: 900 },
      { width: 390, height: 844 },
      { width: 360, height: 800 },
    ]) {
      const page = await browser.newPage({ viewport, deviceScaleFactor: 1 });
      await page.goto(pathToFileURL(source).href, { waitUntil: "networkidle" });
      await page.evaluate(async () => {
        await document.fonts.ready;
        for (const image of document.images) {
          image.scrollIntoView({ block: "center" });
          if (!image.complete) await image.decode();
        }
        window.scrollTo(0, 0);
      });
      const measurement = await page.evaluate(() => ({
        client_width: document.documentElement.clientWidth,
        scroll_width: document.documentElement.scrollWidth,
        h1_count: document.querySelectorAll("h1").length,
        images: [...document.images].map((image) => ({
          complete: image.complete,
          natural_width: image.naturalWidth,
          natural_height: image.naturalHeight,
        })),
        tables: [...document.querySelectorAll("table")].map((table) => ({
          wrapper_client_width: table.parentElement.clientWidth,
          wrapper_scroll_width: table.parentElement.scrollWidth,
          overflow_x: getComputedStyle(table.parentElement).overflowX,
        })),
      }));
      const screenshot = path.join(outputDir, `dark-${viewport.width}.png`);
      await page.screenshot({ path: screenshot, type: "png", fullPage: true });
      observations.push({ ...viewport, ...measurement, screenshot });
      await page.close();
    }
  } finally {
    await browser.close();
  }
  fs.writeFileSync(
    path.join(outputDir, "measurements.json"),
    `${JSON.stringify({ status: "pass", source, observations }, null, 2)}\n`,
    "utf8",
  );
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
