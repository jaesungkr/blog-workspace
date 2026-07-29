const fs = require("node:fs");
const path = require("node:path");
const { pathToFileURL } = require("node:url");
const { chromium } = require("playwright");

async function main() {
  const postRoot = path.resolve(__dirname, "..");
  const imagePath = path.join(
    postRoot,
    "assets",
    "breastfeeding-cold-selection-flow-v6.png",
  );
  const imageUrl = pathToFileURL(imagePath).href;
  const qaRoot = "/tmp/breastfeeding-cold-selection-flow-v6-qa";
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
      document.documentElement.style.margin = "0";
      document.documentElement.style.background = "#ffffff";
      document.body.style.margin = "20px";
      document.body.style.width = "360px";
      document.body.style.background = "#ffffff";
      document.body.style.lineHeight = "0";
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
      ["header", { x: 38, y: 28, width: 1004, height: 225 }],
      ["source-and-branch", { x: 42, y: 255, width: 340, height: 735 }],
      ["green-lane", { x: 350, y: 260, width: 690, height: 235 }],
      ["amber-lane", { x: 350, y: 512, width: 690, height: 235 }],
      ["red-lane", { x: 350, y: 764, width: 690, height: 235 }],
      ["exceptions", { x: 50, y: 1040, width: 980, height: 260 }],
      ["aspirin-caveat", { x: 0, y: 1305, width: 1080, height: 45 }],
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
