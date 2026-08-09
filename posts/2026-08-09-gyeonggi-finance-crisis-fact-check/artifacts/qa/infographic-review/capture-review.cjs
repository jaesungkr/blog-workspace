const fs = require("node:fs");
const path = require("node:path");
const { pathToFileURL } = require("node:url");
const { chromium } = require("playwright");

async function main() {
  const reviewDir = __dirname;
  const postRoot = path.resolve(reviewDir, "..", "..", "..");
  const candidate = path.join(postRoot, "assets", "infographics", "gyeonggi-finance-pressure-v1.png");
  const systemChrome = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
  const executablePath = fs.existsSync(systemChrome) ? systemChrome : chromium.executablePath();
  const browser = await chromium.launch({ executablePath, headless: true });
  try {
    const full = await browser.newPage({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: 1 });
    await full.setContent(`<style>*{box-sizing:border-box}html,body{margin:0;width:1080px;height:1350px;overflow:hidden}img{display:block;width:1080px;height:1350px}</style><img id="candidate" src="${pathToFileURL(candidate).href}">`);
    await full.locator("#candidate").waitFor({ state: "visible" });
    await full.locator("#candidate").screenshot({ path: path.join(reviewDir, "full-raster-browser.png") });

    const crops = [
      ["header", { x: 48, y: 25, width: 984, height: 240 }],
      ["verdict", { x: 48, y: 270, width: 984, height: 165 }],
      ["pressure-left", { x: 48, y: 450, width: 500, height: 250 }],
      ["pressure-right", { x: 532, y: 450, width: 500, height: 250 }],
      ["connector-center", { x: 420, y: 500, width: 240, height: 155 }],
      ["fiscal-room", { x: 48, y: 735, width: 984, height: 385 }],
      ["reading-rule", { x: 70, y: 1090, width: 940, height: 150 }],
      ["caveat", { x: 48, y: 1240, width: 984, height: 105 }],
    ];
    for (const [name, clip] of crops) {
      await full.screenshot({ path: path.join(reviewDir, `crop-${name}.png`), clip });
    }

    const mobile = await browser.newPage({ viewport: { width: 360, height: 450 }, deviceScaleFactor: 2 });
    await mobile.setContent(`<meta name="viewport" content="width=device-width,initial-scale=1"><style>*{box-sizing:border-box}html,body{margin:0;width:360px;background:#fff}img{display:block;width:360px;height:auto}</style><img id="candidate" src="${pathToFileURL(candidate).href}">`);
    await mobile.locator("#candidate").waitFor({ state: "visible" });
    const measurements = await mobile.evaluate(() => {
      const img = document.querySelector("#candidate");
      const r = img.getBoundingClientRect();
      return { viewport: { width: innerWidth, height: innerHeight, devicePixelRatio }, image: { width: r.width, height: r.height, naturalWidth: img.naturalWidth, naturalHeight: img.naturalHeight } };
    });
    fs.writeFileSync(path.join(reviewDir, "mobile-measurements.json"), JSON.stringify(measurements, null, 2) + "\n");
    await mobile.locator("#candidate").screenshot({ path: path.join(reviewDir, "css-360-browser-display.png") });
  } finally {
    await browser.close();
  }
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
