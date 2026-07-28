const fs = require("node:fs");
const path = require("node:path");
const { pathToFileURL } = require("node:url");
const { chromium } = require("playwright");

const postRoot = path.resolve(__dirname, "..");
const source = path.join(
  __dirname,
  "prompt-injection-defense-infographic.html",
);
const output = path.join(
  postRoot,
  "assets",
  "prompt-injection-defense-infographic-v3.png",
);
const macChrome = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
const launchOptions = fs.existsSync(macChrome)
  ? { headless: true, executablePath: macChrome }
  : { headless: true };

(async () => {
  const browser = await chromium.launch(launchOptions);
  const page = await browser.newPage({
    viewport: { width: 1200, height: 1500 },
    deviceScaleFactor: 1,
  });

  await page.goto(pathToFileURL(source).href, { waitUntil: "load" });
  await page.evaluate(() => document.fonts.ready);
  await page.screenshot({
    path: output,
    clip: { x: 0, y: 0, width: 1200, height: 1500 },
  });

  console.log(JSON.stringify({
    source,
    output,
    width: 1200,
    height: 1500,
    reducedRasterWritten: false,
  }));
  await browser.close();
})();
