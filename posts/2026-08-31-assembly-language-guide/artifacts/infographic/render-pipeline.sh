#!/bin/zsh
set -euo pipefail

script_dir="$(cd "$(dirname "$0")" && pwd)"
bundle_dir="$(cd "$script_dir/../.." && pwd)"
chrome_bin="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
source_html="$script_dir/assembly-language-pipeline-v3.html"
output_png="$bundle_dir/assets/assembly-language-pipeline-v3.png"

"$chrome_bin" \
  --headless=new \
  --disable-gpu \
  --hide-scrollbars \
  --force-device-scale-factor=1 \
  --window-size=700,980 \
  --screenshot="$output_png" \
  "file://$source_html"

sips -g pixelWidth -g pixelHeight "$output_png"
shasum -a 256 "$output_png"
