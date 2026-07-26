const fs = require("fs");
const path = require("path");
const { chromium } = require("playwright");

const postDir = path.resolve(__dirname, "..");
const repoDir = path.resolve(postDir, "..", "..");
const fragmentPath = path.join(
  repoDir,
  "dist",
  "per-pbr-eps-valuation-guide.html",
);
const outputDir = path.join(__dirname, "article-preview-760");

fs.mkdirSync(outputDir, { recursive: true });
const fragment = fs.readFileSync(fragmentPath, "utf8");

(async () => {
  const systemChrome =
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
  const executablePath =
    process.env.CHROMIUM_PATH ||
    (fs.existsSync(systemChrome) ? systemChrome : chromium.executablePath());
  const browser = await chromium.launch({ executablePath, headless: true });
  const page = await browser.newPage({
    viewport: { width: 760, height: 1600 },
    deviceScaleFactor: 1,
  });

  await page.setContent(
    `<!doctype html>
    <html lang="ko">
      <head>
        <meta charset="utf-8">
        <style>
          * { box-sizing: border-box; }
          html, body { margin: 0; background: #ffffff; }
          body {
            width: 760px;
            padding: 32px;
            color: #222222;
            font-family: -apple-system, BlinkMacSystemFont, "Apple SD Gothic Neo",
              "Noto Sans KR", sans-serif;
            font-size: 17px;
          }
          a { overflow-wrap: anywhere; }
        </style>
      </head>
      <body>${fragment}</body>
    </html>`,
    { waitUntil: "load" },
  );
  await page.evaluate(() => document.fonts.ready);

  const totalHeight = await page.evaluate(() =>
    Math.ceil(document.documentElement.scrollHeight),
  );
  await page.screenshot({
    path: path.join(outputDir, "full.png"),
    fullPage: true,
  });

  const segmentHeight = 1500;
  let segment = 1;
  for (let y = 0; y < totalHeight; y += segmentHeight) {
    await page.evaluate((scrollY) => window.scrollTo(0, scrollY), y);
    await page.screenshot({
      path: path.join(
        outputDir,
        `section-${String(segment).padStart(2, "0")}.png`,
      ),
      fullPage: false,
    });
    segment += 1;
  }

  console.log(
    JSON.stringify({
      width: 760,
      totalHeight,
      segments: segment - 1,
      outputDir,
    }),
  );
  await browser.close();
})();
