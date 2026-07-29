const path = require("node:path");
const { pathToFileURL } = require("node:url");
const { chromium } = require("playwright");

(async () => {
  const postRoot = path.resolve(__dirname, "..");
  const source = path.join(
    __dirname,
    "skillopt-learning-loop-infographic.html",
  );
  const output = path.join(
    postRoot,
    "assets",
    "skillopt-learning-loop-v5.png",
  );

  const browser = await chromium.launch({
    headless: true,
    executablePath: "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
  });
  const page = await browser.newPage({
    viewport: { width: 1080, height: 1700 },
    deviceScaleFactor: 1,
  });

  await page.goto(pathToFileURL(source).href, { waitUntil: "load" });
  await page.evaluate(() => document.fonts.ready);
  await page.screenshot({
    path: output,
    clip: { x: 0, y: 0, width: 1080, height: 1700 },
  });
  await browser.close();
})();
