const fs = require("node:fs");
const path = require("node:path");
const { chromium } = require("playwright");

const postDir = path.resolve(__dirname, "..");
const repoDir = path.resolve(postDir, "..", "..");
const fragmentPath = path.join(
  repoDir,
  "dist",
  "breastfeeding-cold-medicine.html",
);
const fragment = fs.readFileSync(fragmentPath, "utf8");
const qaRoot = "/tmp/breastfeeding-cold-article-qa";
fs.mkdirSync(qaRoot, { recursive: true });

const targets = [
  "집에 있는 약은 세 칸으로 먼저 분류",
  "기침·콧물·코막힘약은 증상별로 선택",
  "판피린티정은 먼저 확인, 액티피드정은 복용하지 않기",
  "이미 먹었다면 제품명·먹은 양·시간부터 기록",
];

async function renderAt(browser, width, height, padding) {
  const outputDir = path.join(qaRoot, String(width));
  fs.mkdirSync(outputDir, { recursive: true });
  const page = await browser.newPage({
    viewport: { width, height },
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
            width: ${width}px;
            padding: ${padding}px;
            color: #222222;
            font-family: -apple-system, BlinkMacSystemFont, "Apple SD Gothic Neo",
              "Noto Sans KR", sans-serif;
            font-size: ${width === 360 ? 16 : 17}px;
          }
          a { overflow-wrap: anywhere; }
        </style>
      </head>
      <body>${fragment}</body>
    </html>`,
    { waitUntil: "load" },
  );
  await page.evaluate(() => document.fonts.ready);

  const layout = await page.evaluate(() => {
    const body = document.body;
    const viewportWidth = document.documentElement.clientWidth;
    const tables = [...document.querySelectorAll("table")];
    const links = [...document.querySelectorAll("a")];
    return {
      totalHeight: Math.ceil(document.documentElement.scrollHeight),
      bodyScrollWidth: body.scrollWidth,
      bodyClientWidth: body.clientWidth,
      headingCount: document.querySelectorAll("h3").length,
      tableCount: tables.length,
      linkCount: links.length,
      linksWithBlankTarget: links.filter(
        (link) => link.getAttribute("target") === "_blank",
      ).length,
      tableMetrics: tables.map((table) => {
        const rect = table.getBoundingClientRect();
        return {
          left: Math.floor(rect.left),
          right: Math.ceil(rect.right),
          width: Math.ceil(rect.width),
          scrollWidth: table.scrollWidth,
          clientWidth: table.clientWidth,
          overflowX: getComputedStyle(table).overflowX,
        };
      }),
      overflowingBodyChildren: [...body.children]
        .filter((element) => element.getBoundingClientRect().right > viewportWidth)
        .map((element) => ({
          tag: element.tagName,
          right: Math.ceil(element.getBoundingClientRect().right),
          text: element.textContent.trim().replace(/\s+/g, " ").slice(0, 100),
        })),
    };
  });

  await page.screenshot({
    path: path.join(outputDir, "opening.png"),
    fullPage: false,
  });

  for (const [index, heading] of targets.entries()) {
    const locator = page.getByRole("heading", { name: heading, exact: true });
    await locator.evaluate((element) => {
      element.scrollIntoView({ block: "start", behavior: "instant" });
    });
    await page.screenshot({
      path: path.join(outputDir, `focus-${index + 1}.png`),
      fullPage: false,
    });
  }

  for (const [index, table] of (await page.locator("table").all()).entries()) {
    await table.screenshot({
      path: path.join(outputDir, `table-${index + 1}.png`),
    });
  }

  await page.close();
  return { width, outputDir, ...layout };
}

async function main() {
  const systemChrome =
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
  const executablePath =
    process.env.CHROMIUM_PATH ||
    (fs.existsSync(systemChrome) ? systemChrome : chromium.executablePath());
  const browser = await chromium.launch({ executablePath, headless: true });
  try {
    const natural = await renderAt(browser, 760, 1600, 32);
    const mobile = await renderAt(browser, 360, 1200, 18);
    console.log(JSON.stringify({ natural, mobile }, null, 2));
  } finally {
    await browser.close();
  }
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
