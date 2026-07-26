const path = require("node:path");
const { pathToFileURL } = require("node:url");
const fs = require("node:fs");
const { chromium } = require("playwright");

async function main() {
  const postRoot = path.resolve(__dirname, "..");
  const source = path.join(__dirname, "duckdb-analysis-flow-infographic.html");
  const output = path.join(
    postRoot,
    "assets",
    "duckdb-analysis-flow-infographic.png",
  );

  const systemChrome =
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
  const executablePath =
    process.env.CHROMIUM_PATH ||
    (fs.existsSync(systemChrome) ? systemChrome : chromium.executablePath());
  const browser = await chromium.launch({ executablePath, headless: true });
  try {
    const page = await browser.newPage({
      viewport: { width: 1200, height: 1500 },
      deviceScaleFactor: 1,
    });
    await page.goto(pathToFileURL(source).href, { waitUntil: "networkidle" });
    await page.evaluate(() => document.fonts.ready);
    await page.screenshot({
      path: output,
      type: "png",
      fullPage: false,
    });
  } finally {
    await browser.close();
  }
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
