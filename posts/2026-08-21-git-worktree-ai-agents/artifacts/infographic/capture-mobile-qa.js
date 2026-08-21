const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

(async () => {
  const browser = await chromium.launch({
    headless: true,
    executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
  });
  const page = await browser.newPage({ viewport: { width: 360, height: 360 }, deviceScaleFactor: 1 });
  const imagePath = path.resolve(__dirname, '../../assets/graphics/worktree-map-infographic-v5.png');
  const imageUrl = `data:image/png;base64,${fs.readFileSync(imagePath).toString('base64')}`;
  await page.setContent(`<!doctype html><html><head><meta charset="utf-8"><style>*{box-sizing:border-box}html,body{margin:0;width:360px;height:360px;overflow:hidden;background:#fff}img{display:block;width:360px;height:360px}</style></head><body><img src="${imageUrl}" alt="worktree infographic"></body></html>`);
  await page.waitForFunction(() => {
    const img = document.querySelector('img');
    return img.complete && img.naturalWidth === 1080 && img.naturalHeight === 1080;
  });
  await page.screenshot({ path: path.join(__dirname, 'worktree-map-v5-mobile-360.png') });
  const metrics = await page.evaluate(() => {
    const img = document.querySelector('img');
    const rect = img.getBoundingClientRect();
    return {
      viewport: [window.innerWidth, window.innerHeight],
      document: [document.documentElement.clientWidth, document.documentElement.scrollWidth],
      imageDisplay: [rect.width, rect.height],
      imageNatural: [img.naturalWidth, img.naturalHeight],
    };
  });
  process.stdout.write(`${JSON.stringify(metrics)}\n`);
  await browser.close();
})();
