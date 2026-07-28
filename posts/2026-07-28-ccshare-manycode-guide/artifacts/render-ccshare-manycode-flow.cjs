const fs = require("node:fs");
const path = require("node:path");
const { Resvg } = require("@resvg/resvg-js");

const postRoot = path.resolve(__dirname, "..");
const source = path.join(
  __dirname,
  "ccshare-manycode-flow-infographic.html",
);
const output = path.join(
  postRoot,
  "assets",
  "ccshare-manycode-flow-v2.png",
);

const page = fs.readFileSync(source, "utf8");
const styleMatch = page.match(/<style>([\s\S]*?)<\/style>/i);
const svgMatch = page.match(/(<svg[\s\S]*<\/svg>)/i);

if (!styleMatch || !svgMatch) {
  throw new Error("The HTML source must contain one style block and one SVG.");
}

const svg = svgMatch[1].replace(
  /<svg([^>]*)>/i,
  `<svg$1 xmlns="http://www.w3.org/2000/svg"><style>${styleMatch[1]}</style>`,
);

const renderer = new Resvg(svg, {
  fitTo: { mode: "width", value: 1080 },
  font: {
    loadSystemFonts: true,
    defaultFontFamily: "Apple SD Gothic Neo",
  },
});

fs.writeFileSync(output, renderer.render().asPng());
