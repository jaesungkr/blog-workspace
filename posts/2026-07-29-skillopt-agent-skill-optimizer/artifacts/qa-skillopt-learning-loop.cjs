const fs = require("node:fs");
const path = require("node:path");
const { chromium } = require("playwright");
const sharp = require("sharp");

(async () => {
  const candidate = path.resolve(
    __dirname,
    "..",
    "assets",
    "skillopt-learning-loop-v5.png",
  );
  const output = "/private/tmp/skillopt-learning-loop-v5-browser-360.png";
  const encoded = fs.readFileSync(candidate).toString("base64");

  const browser = await chromium.launch({
    headless: true,
    executablePath: "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
  });
  const page = await browser.newPage({
    viewport: { width: 420, height: 640 },
    deviceScaleFactor: 1,
  });

  await page.setContent(`
    <!doctype html>
    <html lang="ko">
      <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
          html, body { margin: 0; background: #d7d4cd; }
          body { padding: 30px; }
          img { display: block; width: 360px; height: auto; }
        </style>
      </head>
      <body>
        <img
          alt="SkillOpt 학습 루프 360px 브라우저 검수"
          src="data:image/png;base64,${encoded}"
        >
      </body>
    </html>
  `);
  await page.waitForFunction(() => {
    const image = document.querySelector("img");
    return image.complete && image.naturalWidth === 1080;
  });

  const metrics = await page.locator("img").evaluate((image) => ({
    cssWidth: image.getBoundingClientRect().width,
    cssHeight: image.getBoundingClientRect().height,
    naturalWidth: image.naturalWidth,
    naturalHeight: image.naturalHeight,
  }));
  console.log(JSON.stringify(metrics));
  await page.screenshot({ path: output, fullPage: true });
  await browser.close();

  const crops = [
    ["header", 0, 260],
    ["stage1", 250, 430],
    ["stage2", 660, 430],
    ["stage3", 1080, 330],
    ["stage4", 1330, 370],
  ];
  await Promise.all(crops.map(([name, top, height]) => (
    sharp(candidate)
      .extract({ left: 0, top, width: 1080, height })
      .png()
      .toFile(`/private/tmp/skillopt-v5-crop-${name}.png`)
  )));
})();
