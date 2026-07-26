const fs = require("node:fs");
const path = require("node:path");
const sharp = require("sharp");

async function main() {
  const postRoot = path.resolve(__dirname, "..");
  const source = path.join(
    postRoot,
    "assets",
    "per-pbr-eps-choice-map-infographic-v6.png",
  );
  const outputDir = path.join(__dirname, "infographic-qa-v6");
  fs.mkdirSync(outputDir, { recursive: true });

  await sharp(source)
    .resize({ width: 360 })
    .png()
    .toFile(path.join(outputDir, "mobile-360x450.png"));

  const crops = {
    "header.png": { left: 0, top: 0, width: 1080, height: 320 },
    "top-left.png": { left: 0, top: 320, width: 540, height: 390 },
    "top-right.png": { left: 540, top: 320, width: 540, height: 390 },
    "bottom-left.png": { left: 0, top: 710, width: 540, height: 390 },
    "bottom-right.png": { left: 540, top: 710, width: 540, height: 390 },
    "axes-center.png": { left: 390, top: 560, width: 300, height: 300 },
    "caveat.png": { left: 0, top: 1100, width: 1080, height: 250 },
  };

  for (const [name, region] of Object.entries(crops)) {
    await sharp(source)
      .extract(region)
      .png()
      .toFile(path.join(outputDir, name));
  }
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
