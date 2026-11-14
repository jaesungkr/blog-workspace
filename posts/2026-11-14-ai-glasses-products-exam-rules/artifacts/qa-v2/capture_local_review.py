# -*- coding: utf-8 -*-
from pathlib import Path
import base64,json,hashlib,sys,datetime
post=Path(__file__).resolve().parents[2];repo=post.parents[1]
sys.path.insert(0,str(repo/'.agents/skills/dev-log-rich-post-workspace-v2/scripts'))
from capture_rich_qa_v2 import ChromeProcess,find_chrome,WebSocket,CDPClient,evaluate_page
mode=sys.argv[1] if len(sys.argv)>1 else 'creator'
out=post/'artifacts/qa-v2'/('local-browser-'+mode);out.mkdir(parents=True,exist_ok=True)
records=[]
for theme in ('light','dark'):
 preview=post/f'delivery/ai-glasses-products-exam-rules-review-{theme}.html'
 with ChromeProcess(find_chrome(None),20) as chrome:
  with WebSocket(chrome.page_websocket_url,timeout=30) as ws:
   c=CDPClient(ws,timeout=30);c.call('Page.enable');c.call('Runtime.enable')
   for w,h in [(1280,900),(360,800),(390,844)]:
    c.call('Emulation.setDeviceMetricsOverride',{'width':w,'height':h,'deviceScaleFactor':1,'mobile':w<735,'dontSetVisibleSize':False})
    c.discard_events('Page.loadEventFired');c.call('Page.navigate',{'url':preview.as_uri()});c.wait_event('Page.loadEventFired',timeout=30)
    m=evaluate_page(c,15)
    c.call('Runtime.evaluate',{'expression':"(async()=>{await Promise.all(Array.from(document.images).map(i=>i.decode().catch(()=>{})));for(const i of document.images){i.scrollIntoView();await new Promise(requestAnimationFrame);await new Promise(requestAnimationFrame);}window.scrollTo(0,0);await new Promise(requestAnimationFrame);await new Promise(requestAnimationFrame);return true;})()",'awaitPromise':True,'returnByValue':True})
    assert m['inner_width']==w and m['client_width']==w and m['scroll_width']==w,m
    assert m['h1_count']==1 and m['toc_targets_unique'] and m['images_loaded'],m
    assert m['image_count']==3,m
    sizes=c.call('Page.getLayoutMetrics');height=int(sizes['cssContentSize']['height'])
    r=c.call('Page.captureScreenshot',{'format':'png','captureBeyondViewport':True,'clip':{'x':0,'y':0,'width':w,'height':height,'scale':1}},timeout=30)
    name=f'{theme}-{w}-full.png';(out/name).write_bytes(base64.b64decode(r['data']))
    sections=c.call('Runtime.evaluate',{'expression':"JSON.stringify(Array.from(document.querySelectorAll('.devlog-rich__section')).map(x=>({title:x.querySelector('h3')?.innerText,y:x.getBoundingClientRect().top+scrollY,height:x.getBoundingClientRect().height})))",'returnByValue':True})['result']['value']
    tables=c.call('Runtime.evaluate',{'expression':"JSON.stringify(Array.from(document.querySelectorAll('.rich-table-wrap')).map(x=>({clientWidth:x.clientWidth,scrollWidth:x.scrollWidth,overflow:getComputedStyle(x).overflowX})))",'returnByValue':True})['result']['value']
    m['images']=[{'natural_width':x['natural_width'],'natural_height':x['natural_height']} for x in m['images']]
    m.update(theme=theme,width=w,height=h,screenshot=name,preview_sha256=hashlib.sha256(preview.read_bytes()).hexdigest(),sections=json.loads(sections),tables=json.loads(tables))
    records.append(m)
    print(theme,w,'page overflow',m['scroll_width']-w,'images',m['image_count'],'height',height)
(out/'receipt.json').write_text(json.dumps({'scope':'local draft QA, not native Tistory or final remote gate','actor':'Codex '+mode,'checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'records':records},ensure_ascii=False,indent=2)+'\n')
print(str(out/'receipt.json'))
