from pathlib import Path
from playwright.sync_api import sync_playwright
import json,hashlib
p=Path(__file__).resolve().parent.parent
out=p/'artifacts/qa-v2/local-inspection';out.mkdir(exist_ok=True)
records=[]
with sync_playwright() as pw:
 for theme,folder in [('light','preflight'),('dark','preflight-dark')]:
  browser=pw.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
  for width,height in [(1280,900),(360,800)]:
   page=browser.new_page(viewport={'width':width,'height':height},device_scale_factor=1)
   source=p/f'artifacts/qa-v2/{folder}/gpt-6-1-terra-work-rich-preview.html'
   page.goto(source.as_uri(),wait_until='networkidle');page.evaluate('document.fonts.ready');page.screenshot(path=str(out/f'{theme}-{width}.png'),full_page=True)
   data=page.evaluate('''() => ({viewport:innerWidth,scrollWidth:document.documentElement.scrollWidth,h1:document.querySelectorAll('h1').length,images:[...document.images].map(i=>({loaded:i.complete&&i.naturalWidth>0,width:i.naturalWidth,height:i.naturalHeight,displayWidth:i.getBoundingClientRect().width})),unresolved:document.body.innerText.includes('{{media:'),brokenAnchors:[...document.querySelectorAll('a[href^="#"]')].filter(a=>!document.getElementById(a.hash.slice(1))).length})''')
   data.update(theme=theme,width=width,preview_sha256=hashlib.sha256(source.read_bytes()).hexdigest());records.append(data)
   page.close()
  browser.close()
(out/'measurements.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(records,ensure_ascii=False,indent=2))
