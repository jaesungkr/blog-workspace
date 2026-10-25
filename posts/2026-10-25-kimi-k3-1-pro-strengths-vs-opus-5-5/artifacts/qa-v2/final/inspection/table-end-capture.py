from pathlib import Path
import sys,base64,json
R=Path('/Users/ja2sng/dev/blog-workspace');P=R/'posts/2026-10-25-kimi-k3-1-pro-strengths-vs-opus-5-5';O=P/'artifacts/qa-v2/final/inspection'
sys.path.insert(0,str(R/'.agents/skills/dev-log-rich-post-workspace-v2/scripts'));import capture_rich_qa_v2 as q
out=[]
for theme in ('light','dark'):
 preview=P/('artifacts/qa-v2/final-rendered' if theme=='light' else 'artifacts/qa-v2/final-dark-rendered')/'kimi-k3-1-pro-strengths-vs-opus-5-5-rich-preview.html'
 with q.ChromeProcess(q.find_chrome(None),20) as chrome:
  with q.WebSocket(chrome.page_websocket_url,30) as ws:
   c=q.CDPClient(ws,30);c.call('Page.enable');c.call('Runtime.enable')
   for width,height in ((360,800),(390,844)):
    q.capture_viewport(c,preview.as_uri(),width,height,O/f'{theme}-{width}-table-top.png',30,20)
    r=c.call('Runtime.evaluate',{'expression':'''(async()=>{let t=[...document.querySelectorAll('table')].at(-1);let p=t.parentElement;p.scrollLeft=p.scrollWidth;p.scrollIntoView({block:'center'});await new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)));return {end:p.scrollLeft,max:p.scrollWidth-p.clientWidth,documentWidth:document.documentElement.scrollWidth,headers:[...t.querySelectorAll('th')].map(x=>x.textContent)};})()''','awaitPromise':True,'returnByValue':True})['result']['value'];r.update(theme=theme,width=width);out.append(r)
    shot=c.call('Page.captureScreenshot',{'format':'png','captureBeyondViewport':False,'fromSurface':True});(O/f'{theme}-{width}-price-table-end.png').write_bytes(base64.b64decode(shot['data']))
(O/'table-end-observations.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print(json.dumps(out,ensure_ascii=False))
