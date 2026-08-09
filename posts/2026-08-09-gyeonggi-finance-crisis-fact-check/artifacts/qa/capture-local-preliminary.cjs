const fs = require("node:fs");
const path = require("node:path");
const { pathToFileURL } = require("node:url");
const { chromium } = require("playwright");

async function capturePage(browser, source, theme, outputDir) {
  const profiles = [
    { width: 1280, height: 900 },
    { width: 390, height: 844 },
    { width: 360, height: 800 },
  ];
  const observations = [];

  for (const profile of profiles) {
    const page = await browser.newPage({ viewport: profile, deviceScaleFactor: 1 });
    await page.goto(pathToFileURL(source).href, { waitUntil: "networkidle" });
    await page.evaluate(async () => {
      await document.fonts.ready;
      for (const image of document.images) {
        image.scrollIntoView({ block: "center" });
        if (!image.complete) {
          await new Promise((resolve) => {
            image.addEventListener("load", resolve, { once: true });
            image.addEventListener("error", resolve, { once: true });
          });
        }
      }
      window.scrollTo(0, 0);
    });
    const measurement = await page.evaluate(() => {
      const root = document.documentElement;
      const tables = [...document.querySelectorAll("table")].map((table) => {
        const wrapper = table.parentElement;
        const style = getComputedStyle(wrapper);
        return {
          wrapper_client_width: wrapper.clientWidth,
          wrapper_scroll_width: wrapper.scrollWidth,
          overflow_x: style.overflowX,
          table_client_width: table.clientWidth,
        };
      });
      const images = [...document.images].map((img) => ({
        complete: img.complete,
        natural_width: img.naturalWidth,
        natural_height: img.naturalHeight,
      }));
      return {
        client_width: root.clientWidth,
        scroll_width: root.scrollWidth,
        h1_count: document.querySelectorAll("h1").length,
        toc_links: document.querySelectorAll("nav a[href^='#']").length,
        tables,
        images,
      };
    });
    const screenshot = path.join(outputDir, `${theme}-${profile.width}.png`);
    await page.screenshot({ path: screenshot, type: "png", fullPage: true });
    observations.push({ theme, ...profile, ...measurement, screenshot });
    await page.close();
  }
  return observations;
}

async function main() {
  const qaDir = __dirname;
  const postRoot = path.resolve(qaDir, "..", "..");
  const repoRoot = path.resolve(postRoot, "..", "..");
  const slug = "gyeonggi-finance-crisis-fact-check-rich-preview.html";
  const light = path.join(repoRoot, "dist", slug);
  const dark = path.join(postRoot, "artifacts", "qa", "dark-preview", slug);
  const outputDir = path.join(qaDir, "preliminary");
  fs.mkdirSync(outputDir, { recursive: true });
  const systemChrome = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
  const executablePath = process.env.CHROMIUM_PATH ||
    (fs.existsSync(systemChrome) ? systemChrome : chromium.executablePath());
  const browser = await chromium.launch({ executablePath, headless: true });
  try {
    const observations = [
      ...(await capturePage(browser, light, "light", outputDir)),
      ...(await capturePage(browser, dark, "dark", outputDir)),
    ];
    fs.writeFileSync(
      path.join(outputDir, "measurements.json"),
      `${JSON.stringify({ status: "preliminary_only", observations }, null, 2)}\n`,
      "utf8",
    );
  } finally {
    await browser.close();
  }
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
