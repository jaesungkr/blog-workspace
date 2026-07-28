// Archived renderer for the v4 full-size raster.
const fs = require("node:fs");
const path = require("node:path");
const { pathToFileURL } = require("node:url");
const { chromium } = require("playwright");

const postRoot = path.resolve(__dirname, "..");
const source = path.join(
  __dirname,
  "wsl-containers-layers-infographic.html",
);
const output = path.join(
  postRoot,
  "assets",
  "wsl-containers-layers-infographic-v4.png",
);
const macChrome = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
const launchOptions = fs.existsSync(macChrome)
  ? { headless: true, executablePath: macChrome }
  : { headless: true };

(async () => {
  const browser = await chromium.launch(launchOptions);
  const page = await browser.newPage({
    viewport: { width: 1080, height: 1350 },
    deviceScaleFactor: 1,
  });

  await page.goto(pathToFileURL(source).href, { waitUntil: "load" });
  await page.screenshot({
    path: output,
    clip: { x: 0, y: 0, width: 1080, height: 1350 },
  });

  await browser.close();
})();
