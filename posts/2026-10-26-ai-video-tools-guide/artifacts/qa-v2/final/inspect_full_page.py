from pathlib import Path
import sys,json,base64
root=Path('/Users/ja2sng/dev/blog-workspace')
sys.path.insert(0,str(root/'.agents/skills/dev-log-rich-post-workspace-v2/scripts'))
from capture_rich_qa_v2 import ChromeProcess,WebSocket,CDPClient,find_chrome,evaluate_page
p=root/'posts/2026-10-26-ai-video-tools-guide'
out=p/'artifacts/qa-v2/final/inspection';out.mkdir(exist_ok=True)
records=[]
for theme,folder in [('light','final-rendered'),('dark','final-dark-rendered')]:
 preview=p/'artifacts/qa-v2'/folder/'ai-video-tools-guide-rich-preview.html'
 with ChromeProcess(find_chrome(None),20) as chrome:
  with WebSocket(chrome.page_websocket_url,timeout=30) as ws:
   c=CDPClient(ws,timeout=30)
   c.call('Page.enable');c.call('Runtime.enable');c.call('Network.enable');c.call('Network.setCacheDisabled',{'cacheDisabled':True})
   def ev(expr):
    v=c.call('Runtime.evaluate',{'expression':expr,'returnByValue':True,'awaitPromise':True})
    if v.get('exceptionDetails'):raise RuntimeError(v['exceptionDetails'])
    return v['result'].get('value')
   def shot(path,clip=None):
    args={'format':'png','fromSurface':True,'captureBeyondViewport':bool(clip)}
    if clip:args['clip']=dict(clip,scale=1)
    (out/path).write_bytes(base64.b64decode(c.call('Page.captureScreenshot',args)['data']))
   for width,height in [(1280,900),(360,800)]:
    c.call('Emulation.setDeviceMetricsOverride',{'width':width,'height':height,'deviceScaleFactor':1,'mobile':width<735})
    c.discard_events('Page.loadEventFired');c.call('Page.navigate',{'url':preview.as_uri()});c.wait_event('Page.loadEventFired',timeout=30)
    m=evaluate_page(c,20)
    doc=ev("({height:document.documentElement.scrollHeight,width:document.documentElement.scrollWidth})")
    shot(f'{theme}-{width}-full.png',{'x':0,'y':0,'width':width,'height':doc['height']})
    details=ev("""(()=>{let rect=e=>{let r=e.getBoundingClientRect();let s=getComputedStyle(e);return {x:r.x,y:r.y+scrollY,width:r.width,height:r.height,color:s.color,background:s.backgroundColor,filter:s.filter}};return {figures:[...document.querySelectorAll('[data-media-id]')].map(e=>({id:e.dataset.mediaId,...rect(e),caption:e.querySelector('.devlog-rich__caption')?.textContent,img:rect(e.querySelector('img'))})),tables:[...document.querySelectorAll('.rich-table-wrap')].map(e=>({width:e.clientWidth,scrollWidth:e.scrollWidth,height:e.clientHeight,tableRows:e.querySelectorAll('tbody tr').length})),headings:[...document.querySelectorAll('h3')].map(e=>({text:e.textContent,...rect(e)})),lists:[...document.querySelectorAll('ul,ol')].map(e=>({items:e.children.length,style:getComputedStyle(e).listStyleType,...rect(e)})),link:getComputedStyle(document.querySelector('.devlog-rich a')).color}})()""")
    records.append({'theme':theme,'width':width,'height':height,'page':m,'details':details})
    for fig in details['figures']:
     if width==360 or fig['id']=='workflow':
      y=max(0,fig['y']-35)
      ev(f'window.scrollTo(0,{y});new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))')
      shot(f"{theme}-{width}-{fig['id']}.png")
    if width==360:
     ev("""(()=>{const e=document.querySelectorAll('.rich-table-wrap')[1];e.scrollLeft=e.scrollWidth;window.scrollTo(0,e.getBoundingClientRect().top+scrollY-24)})();new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))""")
     shot(f'{theme}-{width}-service-table-right.png')
    ev('window.scrollTo(0,document.documentElement.scrollHeight);new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))')
    shot(f'{theme}-{width}-ending.png')
(out/'observations.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
print('full-page inspection captures:',out)
