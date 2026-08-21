const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const browser = await chromium.launch({
    headless: true,
    executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
  });
  const page = await browser.newPage({ viewport: { width: 1080, height: 1080 }, deviceScaleFactor: 1 });
  const source = path.join(__dirname, 'worktree-map-v5.svg');
  const output = path.resolve(__dirname, '../../assets/graphics/worktree-map-infographic-v5.png');
  await page.goto(`file://${source}`);
  await page.evaluate(() => document.fonts.ready);
  await page.screenshot({ path: output });
  await browser.close();
})();
