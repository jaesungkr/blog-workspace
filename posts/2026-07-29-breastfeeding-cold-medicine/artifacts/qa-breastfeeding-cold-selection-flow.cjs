const fs = require("node:fs");
const path = require("node:path");
const { pathToFileURL } = require("node:url");
const { chromium } = require("playwright");

async function main() {
  const postRoot = path.resolve(__dirname, "..");
  const imagePath = path.join(
    postRoot,
    "assets",
    "breastfeeding-cold-selection-flow-v4.png",
  );
  const imageUrl = pathToFileURL(imagePath).href;
  const qaRoot = "/tmp/breastfeeding-cold-selection-flow-qa";
  fs.mkdirSync(qaRoot, { recursive: true });

  const systemChrome =
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
  const executablePath =
    process.env.CHROMIUM_PATH ||
    (fs.existsSync(systemChrome) ? systemChrome : chromium.executablePath());
  const browser = await chromium.launch({ executablePath, headless: true });

  try {
    const mobile = await browser.newPage({
      viewport: { width: 400, height: 520 },
      deviceScaleFactor: 1,
    });
    await mobile.goto(imageUrl, { waitUntil: "load" });
    await mobile.evaluate(() => {
      document.documentElement.style.background = "#ffffff";
      document.body.style.margin = "20px";
      document.body.style.width = "360px";
      const image = document.querySelector("img");
      image.style.width = "360px";
      image.style.height = "auto";
      image.style.display = "block";
    });
    await mobile.screenshot({
      path: path.join(qaRoot, "mobile-360-css.png"),
      fullPage: true,
    });

    const full = await browser.newPage({
      viewport: { width: 1080, height: 1350 },
      deviceScaleFactor: 1,
    });
    await full.goto(imageUrl, { waitUntil: "load" });
    await full.evaluate(() => {
      document.body.style.margin = "0";
      const image = document.querySelector("img");
      image.style.width = "1080px";
      image.style.height = "1350px";
      image.style.display = "block";
    });

    const crops = [
      ["header", { x: 40, y: 30, width: 1000, height: 230 }],
      ["step-1", { x: 50, y: 260, width: 980, height: 350 }],
      ["step-2", { x: 50, y: 620, width: 980, height: 405 }],
      ["step-3", { x: 50, y: 1020, width: 980, height: 273 }],
      ["caveat", { x: 0, y: 1288, width: 1080, height: 62 }],
    ];
    for (const [name, clip] of crops) {
      await full.screenshot({
        path: path.join(qaRoot, `${name}.png`),
        clip,
      });
    }
  } finally {
    await browser.close();
  }
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
