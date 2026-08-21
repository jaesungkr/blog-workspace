const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

(async () => {
  const sourceDir = __dirname;
  const postDir = path.resolve(sourceDir, '../..');
  const rawDir = path.join(sourceDir, 'raw');
  const publishDir = path.join(postDir, 'assets', 'screenshots');
  fs.mkdirSync(rawDir, { recursive: true });
  fs.mkdirSync(publishDir, { recursive: true });

  const browser = await chromium.launch({
    headless: true,
    executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
  });
  const page = await browser.newPage({ viewport: { width: 720, height: 800 }, deviceScaleFactor: 1 });
  await page.goto(`file://${path.join(sourceDir, 'terminal-shots.html')}`);
  await page.evaluate(() => document.fonts.ready);

  const shots = await page.locator('[data-shot]').all();
  for (const shot of shots) {
    const id = await shot.getAttribute('data-shot');
    if (id !== '07-cleanup') continue;
    const rawPath = path.join(rawDir, `${id}-v5.png`);
    const publishPath = path.join(publishDir, `${id}-v5.png`);
    await shot.screenshot({ path: rawPath });
    fs.copyFileSync(rawPath, publishPath);
  }

  await browser.close();
})();
