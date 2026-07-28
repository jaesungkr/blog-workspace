const fs = require("fs");
const path = require("path");
const { chromium } = require("playwright");

const postDir = path.resolve(__dirname, "..");
const repoDir = path.resolve(postDir, "..", "..");
const fragmentPath = path.join(
  repoDir,
  "dist",
  "wsl-containers-without-docker-desktop.html",
);
const outputDir = path.join(__dirname, "article-preview-360");

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
    viewport: { width: 360, height: 1200 },
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
            width: 360px;
            padding: 18px;
            color: #222222;
            font-family: -apple-system, BlinkMacSystemFont, "Apple SD Gothic Neo",
              "Noto Sans KR", sans-serif;
            font-size: 16px;
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
    const codeBlocks = [...document.querySelectorAll("pre")];
    return {
      totalHeight: Math.ceil(document.documentElement.scrollHeight),
      bodyScrollWidth: body.scrollWidth,
      bodyClientWidth: body.clientWidth,
      tableOverflows: tables.filter(
        (element) => element.scrollWidth > element.clientWidth,
      ).length,
      codeBlocksWithScroll: codeBlocks.filter(
        (element) => element.scrollWidth > element.clientWidth,
      ).length,
      codeBlocksWithoutOverflowRule: codeBlocks.filter(
        (element) => getComputedStyle(element).overflowX !== "auto",
      ).length,
      overflowingBodyChildren: [...body.children]
        .filter((element) => element.getBoundingClientRect().right > viewportWidth)
        .map((element) => ({
          tag: element.tagName,
          right: Math.ceil(element.getBoundingClientRect().right),
          scrollWidth: element.scrollWidth,
          clientWidth: element.clientWidth,
          text: element.textContent.trim().replace(/\s+/g, " ").slice(0, 100),
        })),
    };
  });

  await page.screenshot({
    path: path.join(outputDir, "full.png"),
    fullPage: true,
  });

  const targetHeadings = [
    "WSL2 Docker 구성: Windows·Ubuntu·Docker Engine·컨테이너",
    "3. Ubuntu에 Docker Engine·Buildx·Compose 설치",
    "7. WSL2 Docker 오류를 WSL·서비스·권한·경로로 진단",
    "WSL2 Docker 보안: docker 그룹·포트·업데이트 관리",
  ];
  for (const [index, heading] of targetHeadings.entries()) {
    const locator = page.getByRole("heading", { name: heading, exact: true });
    await locator.scrollIntoViewIfNeeded();
    await page.screenshot({
      path: path.join(
        outputDir,
        `focus-${String(index + 1).padStart(2, "0")}.png`,
      ),
      fullPage: false,
    });
  }

  console.log(
    JSON.stringify({
      width: 360,
      focusedScreenshots: targetHeadings.length,
      outputDir,
      ...layout,
    }),
  );
  await browser.close();
})();
