const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');
const crypto = require('crypto');

(async () => {
  const independentDir = __dirname;
  const qaDir = path.resolve(independentDir, '..');
  const previews = {
    light: path.join(qaDir, 'independent-rendered', 'git-worktree-ai-agents-rich-preview.html'),
    dark: path.join(qaDir, 'dark-rendered', 'git-worktree-ai-agents-rich-preview.html'),
  };
  const browser = await chromium.launch({
    headless: true,
    executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
  });
  const receipt = {
    checkedAt: new Date().toISOString(),
    checkedBy: 'Helmholtz independent QA',
    session: crypto.randomUUID(),
    browser: browser.version(),
    note: 'Focused visual review captures from the strict remote-media candidate; dark mode is supplemental.',
    profiles: [],
  };

  for (const [theme, previewPath] of Object.entries(previews)) {
    const page = await browser.newPage({ viewport: { width: 360, height: 800 }, deviceScaleFactor: 1 });
    await page.goto(`file://${previewPath}`, { waitUntil: 'load' });
    const images = page.locator('img');
    for (let index = 0; index < await images.count(); index += 1) {
      const image = images.nth(index);
      await image.scrollIntoViewIfNeeded();
      await image.evaluate((element) => {
        if (element.complete && element.naturalWidth > 0) return;
        return new Promise((resolve) => {
          element.addEventListener('load', resolve, { once: true });
          element.addEventListener('error', resolve, { once: true });
        });
      });
    }
    await page.evaluate(() => window.scrollTo(0, 0));
    const metrics = await page.evaluate(() => ({
      clientWidth: document.documentElement.clientWidth,
      scrollWidth: document.documentElement.scrollWidth,
      scrollHeight: document.documentElement.scrollHeight,
      h1Count: document.querySelectorAll('h1').length,
      figures: [...document.querySelectorAll('figure')].map((figure) => {
        const image = figure.querySelector('img');
        const caption = figure.querySelector('figcaption');
        const rect = image.getBoundingClientRect();
        return {
          mediaId: figure.dataset.mediaId,
          alt: image.alt,
          caption: caption ? caption.textContent.trim() : '',
          displayed: [rect.width, rect.height],
          natural: [image.naturalWidth, image.naturalHeight],
          loaded: image.complete && image.naturalWidth > 0,
        };
      }),
      tables: [...document.querySelectorAll('.rich-table-wrap')].map((wrapper) => ({
        clientWidth: wrapper.clientWidth,
        scrollWidth: wrapper.scrollWidth,
        overflowX: getComputedStyle(wrapper).overflowX,
      })),
      codeBlocks: [...document.querySelectorAll('pre')].map((block, index) => ({
        index: index + 1,
        clientWidth: block.clientWidth,
        scrollWidth: block.scrollWidth,
        overflowX: getComputedStyle(block).overflowX,
        text: block.textContent.trim().slice(0, 120),
      })),
      headings: [...document.querySelectorAll('h2, h3')].map((heading) => heading.textContent.trim()),
      links: [...document.querySelectorAll('article a')].map((link) => ({
        text: link.textContent.trim(),
        href: link.href,
      })),
      lists: [...document.querySelectorAll('article ul, article ol')].map((list) => ({
        items: list.querySelectorAll(':scope > li').length,
        marker: getComputedStyle(list.querySelector(':scope > li'), '::marker').content,
        listStyle: getComputedStyle(list).listStyleType,
      })),
    }));

    await page.screenshot({ path: path.join(independentDir, `${theme}-360-full.png`), fullPage: true });
    const figures = page.locator('figure');
    for (let index = 0; index < await figures.count(); index += 1) {
      await figures.nth(index).screenshot({
        path: path.join(independentDir, `${theme}-360-figure-${String(index + 1).padStart(2, '0')}.png`),
      });
    }
    const headings = page.locator('article h2');
    for (let index = 0; index < await headings.count(); index += 1) {
      await headings.nth(index).scrollIntoViewIfNeeded();
      await page.screenshot({
        path: path.join(independentDir, `${theme}-360-section-${String(index + 1).padStart(2, '0')}.png`),
      });
    }
    const tables = page.locator('.rich-table-wrap');
    for (let index = 0; index < await tables.count(); index += 1) {
      const wrapper = tables.nth(index);
      await wrapper.evaluate((element) => { element.scrollLeft = 0; });
      await wrapper.screenshot({
        path: path.join(independentDir, `${theme}-360-table-${String(index + 1).padStart(2, '0')}-left.png`),
      });
      await wrapper.evaluate((element) => { element.scrollLeft = element.scrollWidth; });
      await wrapper.screenshot({
        path: path.join(independentDir, `${theme}-360-table-${String(index + 1).padStart(2, '0')}-right.png`),
      });
    }
    const codeBlocks = page.locator('pre');
    for (let index = 0; index < await codeBlocks.count(); index += 1) {
      const block = codeBlocks.nth(index);
      const dimensions = await block.evaluate((element) => ({ client: element.clientWidth, scroll: element.scrollWidth }));
      if (dimensions.scroll <= dimensions.client) continue;
      await block.evaluate((element) => { element.scrollLeft = 0; });
      await block.screenshot({
        path: path.join(independentDir, `${theme}-360-code-${String(index + 1).padStart(2, '0')}-left.png`),
      });
      await block.evaluate((element) => { element.scrollLeft = element.scrollWidth; });
      await block.screenshot({
        path: path.join(independentDir, `${theme}-360-code-${String(index + 1).padStart(2, '0')}-right.png`),
      });
    }
    receipt.profiles.push({ theme, metrics });
    await page.close();
  }
  fs.writeFileSync(path.join(independentDir, 'focused-browser-qa.json'), `${JSON.stringify(receipt, null, 2)}\n`);
  process.stdout.write(`${JSON.stringify(receipt, null, 2)}\n`);
  await browser.close();
})();
