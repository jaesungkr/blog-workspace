const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');
const crypto = require('crypto');

(async () => {
  const bundleDir = path.resolve(__dirname, '../..');
  const repoDir = path.resolve(bundleDir, '../..');
  const previews = {
    light: path.join(repoDir, 'dist', 'git-worktree-ai-agents-rich-preview.html'),
    dark: path.join(__dirname, 'dark-preview', 'git-worktree-ai-agents-rich-preview.html'),
  };
  const profiles = [
    { width: 1280, height: 900 },
    { width: 390, height: 844 },
    { width: 360, height: 800 },
  ];
  const browser = await chromium.launch({
    headless: true,
    executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
  });
  const receipt = {
    checkedAt: new Date().toISOString(),
    checkedBy: 'Codex local supplemental browser QA',
    session: crypto.randomUUID(),
    browser: browser.version(),
    note: 'Local-media supplemental QA only; this does not replace required remote-media creator or independent QA.',
    profiles: [],
  };

  for (const [theme, previewPath] of Object.entries(previews)) {
    for (const profile of profiles) {
      const page = await browser.newPage({ viewport: profile, deviceScaleFactor: 1 });
      await page.goto(`file://${previewPath}`, { waitUntil: 'load' });
      const imageCount = await page.locator('img').count();
      for (let i = 0; i < imageCount; i += 1) {
        const currentImage = page.locator('img').nth(i);
        await currentImage.scrollIntoViewIfNeeded();
        await currentImage.evaluate((img) => {
          if (img.complete && img.naturalWidth > 0) return;
          return new Promise((resolve) => {
            img.addEventListener('load', resolve, { once: true });
            img.addEventListener('error', resolve, { once: true });
          });
        });
      }
      await page.evaluate(() => window.scrollTo(0, 0));
      await page.waitForFunction(
        () => [...document.images].every((img) => img.complete && img.naturalWidth > 0),
        null,
        { timeout: 5000 },
      ).catch(() => {});
      const metrics = await page.evaluate(() => ({
        clientWidth: document.documentElement.clientWidth,
        scrollWidth: document.documentElement.scrollWidth,
        scrollHeight: document.documentElement.scrollHeight,
        h1Count: document.querySelectorAll('h1').length,
        images: [...document.images].map((img) => {
          const r = img.getBoundingClientRect();
          return { alt: img.alt, displayWidth: r.width, displayHeight: r.height, naturalWidth: img.naturalWidth, naturalHeight: img.naturalHeight };
        }),
        tables: [...document.querySelectorAll('table')].map((table) => {
          const wrapper = table.parentElement;
          return { wrapperClientWidth: wrapper.clientWidth, wrapperScrollWidth: wrapper.scrollWidth, overflowX: getComputedStyle(wrapper).overflowX };
        }),
        codeBlocks: [...document.querySelectorAll('pre')].map((pre) => ({ clientWidth: pre.clientWidth, scrollWidth: pre.scrollWidth, overflowX: getComputedStyle(pre).overflowX })),
      }));
      const stem = `local-${theme}-${profile.width}`;
      await page.screenshot({ path: path.join(__dirname, `${stem}-full.png`), fullPage: true });
      if (profile.width === 360) {
        const figures = await page.locator('figure').all();
        for (let i = 0; i < figures.length; i += 1) {
          await figures[i].screenshot({ path: path.join(__dirname, `${stem}-figure-${String(i + 1).padStart(2, '0')}.png`) });
        }
        const tables = await page.locator('table').all();
        for (let i = 0; i < tables.length; i += 1) {
          const wrapper = tables[i].locator('..');
          await wrapper.evaluate((el) => { el.scrollLeft = 0; });
          await wrapper.screenshot({ path: path.join(__dirname, `${stem}-table-${String(i + 1).padStart(2, '0')}-left.png`) });
          await wrapper.evaluate((el) => { el.scrollLeft = el.scrollWidth; });
          await wrapper.screenshot({ path: path.join(__dirname, `${stem}-table-${String(i + 1).padStart(2, '0')}-right.png`) });
        }
        const overflowCode = page.locator('pre').filter({ has: page.locator('code') });
        const codeCount = await overflowCode.count();
        for (let i = 0; i < codeCount; i += 1) {
          const block = overflowCode.nth(i);
          const sizes = await block.evaluate((el) => ({ client: el.clientWidth, scroll: el.scrollWidth }));
          if (sizes.scroll <= sizes.client) continue;
          await block.evaluate((el) => { el.scrollLeft = 0; });
          await block.screenshot({ path: path.join(__dirname, `${stem}-code-${String(i + 1).padStart(2, '0')}-left.png`) });
          await block.evaluate((el) => { el.scrollLeft = el.scrollWidth; });
          await block.screenshot({ path: path.join(__dirname, `${stem}-code-${String(i + 1).padStart(2, '0')}-right.png`) });
        }
      }
      receipt.profiles.push({ theme, ...profile, screenshot: `${stem}-full.png`, metrics });
      await page.close();
    }
  }
  fs.writeFileSync(path.join(__dirname, 'local-browser-qa.json'), `${JSON.stringify(receipt, null, 2)}\n`);
  process.stdout.write(`${JSON.stringify(receipt, null, 2)}\n`);
  await browser.close();
})();
