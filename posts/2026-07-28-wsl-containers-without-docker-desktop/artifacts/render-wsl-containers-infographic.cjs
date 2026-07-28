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
const mobileOutput = path.join(
  __dirname,
  "wsl-containers-layers-infographic-v4-mobile.png",
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

  await page.setViewportSize({ width: 360, height: 450 });
  await page.evaluate(() => {
    document.documentElement.style.width = "360px";
    document.documentElement.style.height = "450px";
    document.body.style.width = "360px";
    document.body.style.height = "450px";
    const svg = document.querySelector("svg");
    svg.style.width = "360px";
    svg.style.height = "450px";
  });
  await page.screenshot({
    path: mobileOutput,
    clip: { x: 0, y: 0, width: 360, height: 450 },
  });

  await browser.close();
})();
