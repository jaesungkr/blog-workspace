const fs = require("node:fs");
const path = require("node:path");
const { pathToFileURL } = require("node:url");
const { chromium } = require("playwright");

async function main() {
  const postRoot = path.resolve(__dirname, "..");
  const source = path.join(__dirname, "gyeonggi-finance-pressure.html");
  const rawDir = path.join(postRoot, "artifacts", "captures", "raw");
  const publishDir = path.join(postRoot, "assets", "infographics");
  const raw = path.join(rawDir, "gyeonggi-finance-pressure-v1.png");
  const output = path.join(publishDir, "gyeonggi-finance-pressure-v1.png");
  const systemChrome = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
  const executablePath = process.env.CHROMIUM_PATH ||
    (fs.existsSync(systemChrome) ? systemChrome : chromium.executablePath());

  fs.mkdirSync(rawDir, { recursive: true });
  fs.mkdirSync(publishDir, { recursive: true });

  const browser = await chromium.launch({ executablePath, headless: true });
  try {
    const page = await browser.newPage({
      viewport: { width: 1080, height: 1350 },
      deviceScaleFactor: 1,
    });
    await page.goto(pathToFileURL(source).href, { waitUntil: "networkidle" });
    await page.evaluate(() => document.fonts.ready);
    await page.screenshot({ path: raw, type: "png", fullPage: false });
    fs.copyFileSync(raw, output);
  } finally {
    await browser.close();
  }
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
