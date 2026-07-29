const fs = require("node:fs");
const path = require("node:path");
const { chromium } = require("playwright");

const repositoryRoot = path.resolve(__dirname, "..", "..", "..");
const renderedPath = path.join(
  repositoryRoot,
  "dist",
  "skillopt-agent-skill-optimizer.html",
);
const rendered = fs.readFileSync(renderedPath, "utf8");

async function inspectAtWidth(browser, label, contentWidth, viewportWidth) {
  const page = await browser.newPage({
    viewport: { width: viewportWidth, height: 900 },
    deviceScaleFactor: 1,
  });
  await page.setContent(`
    <!doctype html>
    <html lang="ko">
      <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
          html, body { margin: 0; background: #ecebe7; }
          body {
            color: #222;
            font-family: "Apple SD Gothic Neo", "AppleGothic", sans-serif;
            font-size: 18px;
          }
          article {
            width: ${contentWidth}px;
            margin: 0 auto;
            padding: 42px 0 80px;
            background: #fff;
          }
        </style>
      </head>
      <body><article>${rendered}</article></body>
    </html>
  `);
  await page.evaluate(() => document.fonts.ready);

  const metrics = await page.evaluate(() => ({
    bodyClientWidth: document.body.clientWidth,
    bodyScrollWidth: document.body.scrollWidth,
    articleClientWidth: document.querySelector("article").clientWidth,
    articleScrollWidth: document.querySelector("article").scrollWidth,
    headings: [...document.querySelectorAll("h3")].map((node) => node.textContent),
    tables: [...document.querySelectorAll("table")].map((node, index) => ({
      index,
      clientWidth: node.clientWidth,
      scrollWidth: node.scrollWidth,
      left: node.getBoundingClientRect().left,
      right: node.getBoundingClientRect().right,
    })),
    codeBlocks: [...document.querySelectorAll("pre")].map((node, index) => ({
      index,
      clientWidth: node.clientWidth,
      scrollWidth: node.scrollWidth,
      overflowX: getComputedStyle(node).overflowX,
    })),
    links: [...document.querySelectorAll("a")].map((node) => ({
      text: node.textContent,
      href: node.href,
      target: node.target,
    })),
  }));

  console.log(`${label} ${JSON.stringify(metrics)}`);
  await page.screenshot({
    path: `/private/tmp/skillopt-article-${label}.png`,
    fullPage: true,
  });

  for (const [index, table] of (await page.locator("table").all()).entries()) {
    await table.screenshot({
      path: `/private/tmp/skillopt-article-${label}-table-${index + 1}.png`,
    });
  }
  for (const [index, block] of (await page.locator("pre").all()).entries()) {
    await block.screenshot({
      path: `/private/tmp/skillopt-article-${label}-code-${index + 1}.png`,
    });
  }
  await page.close();
}

(async () => {
  const browser = await chromium.launch({
    headless: true,
    executablePath: "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
  });
  await inspectAtWidth(browser, "desktop", 760, 920);
  await inspectAtWidth(browser, "mobile", 360, 390);
  await browser.close();
})();
