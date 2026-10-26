"""Local-only review captures; never a final-page or remote-media approval."""
from pathlib import Path
import base64
import hashlib
import json
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[3]/'.agents/skills/dev-log-rich-post-workspace-v2/scripts'))
from capture_rich_qa_v2 import ChromeProcess,WebSocket,CDPClient,find_chrome,evaluate_page
bundle=Path(__file__).resolve().parents[1]
qa=bundle/'artifacts/qa-v2'
records=[]
for theme,preview_dir in [('light','preflight'),('dark','preflight-dark')]:
 out=qa/f'preflight-captures/{theme}'
 out.mkdir(parents=True,exist_ok=True)
 preview=qa/preview_dir/'smoking-cessation-month-3-rich-preview.html'
 with ChromeProcess(find_chrome(None),20) as chrome:
  with WebSocket(chrome.page_websocket_url,30) as ws:
   c=CDPClient(ws,30);c.call('Page.enable');c.call('Runtime.enable')
   for width,height in [(1280,900),(360,800)]:
    c.call('Emulation.setDeviceMetricsOverride',{'width':width,'height':height,'deviceScaleFactor':1,'mobile':width<735})
    c.discard_events('Page.loadEventFired');c.call('Page.navigate',{'url':preview.as_uri()});c.wait_event('Page.loadEventFired',30)
    measured=evaluate_page(c,20);measured.update(width=width,height=height)
    assert measured['images_loaded'] and measured['scroll_width']==width and measured['toc_targets_unique'] and measured['h1_count']==1,measured
    shot=c.call('Page.captureScreenshot',{'format':'png','captureBeyondViewport':False})
    (out/f'{width}-top.png').write_bytes(base64.b64decode(shot['data']))
    details=c.call('Runtime.evaluate',{'expression':'''JSON.stringify({tables:[...document.querySelectorAll('.rich-table-wrap')].map(e=>({clientWidth:e.clientWidth,scrollWidth:e.scrollWidth,rect:e.getBoundingClientRect().toJSON(),overflow:getComputedStyle(e).overflowX,td:[...e.querySelectorAll('th')].map(t=>({width:t.getBoundingClientRect().width,font:getComputedStyle(t).fontSize}))})),bodyFont:getComputedStyle(document.querySelector('article p')).fontSize})''','returnByValue':True})
    measured['layout']=json.loads(details['result']['value']);measured['theme']=theme
    total=measured['scroll_height']
    screenshot=c.call('Page.captureScreenshot',{'format':'png','captureBeyondViewport':True,'clip':{'x':0,'y':0,'width':width,'height':total,'scale':1}})
    (out/f'{width}-full.png').write_bytes(base64.b64decode(screenshot['data']))
    if width==360:
     for idx,table in enumerate(measured['layout']['tables']):
      y=max(0,table['rect']['y']-180)
      c.call('Runtime.evaluate',{'expression':f'window.scrollTo(0,{y});'})
      c.call('Runtime.evaluate',{'expression':'new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))','awaitPromise':True})
      shot=c.call('Page.captureScreenshot',{'format':'png','captureBeyondViewport':False})
      (out/f'360-table-{idx+1}-left.png').write_bytes(base64.b64decode(shot['data']))
      c.call('Runtime.evaluate',{'expression':f"document.querySelectorAll('.rich-table-wrap')[{idx}].scrollLeft=10000"})
      shot=c.call('Page.captureScreenshot',{'format':'png','captureBeyondViewport':False})
      (out/f'360-table-{idx+1}-right.png').write_bytes(base64.b64decode(shot['data']))
    records.append(measured)
(qa/'local-preflight-browser.json').write_text(json.dumps({'purpose':'local preflight, not final-page approval','reviewer':'Codex /root','records':records},ensure_ascii=False,indent=2)+'\n')
print(json.dumps([{'theme':r['theme'],'width':r['width'],'scroll_width':r['scroll_width'],'scroll_height':r['scroll_height'],'images_loaded':r['images_loaded'],'h1':r['h1_count'],'toc_ok':r['toc_targets_unique'],'tables':r['layout']['tables']} for r in records],ensure_ascii=False,indent=2))
