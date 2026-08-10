const { spawn } = require('child_process');
const fs = require('fs');
const path = require('path');

(async () => {
  const root = path.resolve(__dirname, '..');
  const source = path.join(__dirname, 'plain-cracker-calorie-map-v2.svg');
  const output = path.join(root, 'assets', 'plain-cracker-calorie-map-v2.png');
  if (fs.existsSync(output)) {
    throw new Error(`refusing to overwrite versioned candidate: ${output}`);
  }
  const chrome = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
  const profile = '/tmp/codex-plain-cracker-render';
  const child = spawn(chrome, [
    '--headless=new',
    '--disable-gpu',
    '--disable-background-networking',
    '--no-first-run',
    '--no-default-browser-check',
    `--user-data-dir=${profile}`,
    '--window-size=1080,1350',
    `--screenshot=${output}`,
    `file://${source}`,
  ], { stdio: 'ignore' });

  const deadline = Date.now() + 15000;
  while (!fs.existsSync(output) && Date.now() < deadline) {
    await new Promise(resolve => setTimeout(resolve, 200));
  }
  child.kill('SIGTERM');
  if (!fs.existsSync(output)) throw new Error(`render failed: ${output}`);
})();
