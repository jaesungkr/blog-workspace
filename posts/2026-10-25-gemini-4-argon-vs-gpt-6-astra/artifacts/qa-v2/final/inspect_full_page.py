"""Independent supplementary inspection of the exact remote final previews."""
import base64,json,sys
from pathlib import Path
post=Path(__file__).resolve().parents[3]
repo=post.parents[1]
sys.path.insert(0,str(repo/'.agents/skills/dev-log-rich-post-workspace-v2/scripts'))
from capture_rich_qa_v2 import ChromeProcess,WebSocket,CDPClient,find_chrome,evaluate_page,sha256_file
out=post/'artifacts/qa-v2/final/inspection';out.mkdir(exist_ok=True)
records=[]
for theme,folder in [('light','final-rendered'),('dark','final-dark-rendered')]:
 with ChromeProcess(find_chrome(None),20) as chrome:
  with WebSocket(chrome.page_websocket_url,timeout=30) as ws:
   client=CDPClient(ws,timeout=30);client.call('Page.enable');client.call('Runtime.enable')
   html=post/'artifacts/qa-v2'/folder/'gemini-4-argon-vs-gpt-6-astra-rich-preview.html'
   for width,height in [(1280,900),(360,800)]:
    client.call('Emulation.setDeviceMetricsOverride',{'width':width,'height':height,'deviceScaleFactor':1,'mobile':width<735})
    client.discard_events('Page.loadEventFired');client.call('Page.navigate',{'url':html.as_uri()});client.wait_event('Page.loadEventFired',timeout=30)
    m=evaluate_page(client,20)
    assert m['images_loaded'] and m['scroll_width']==width and m['toc_targets_unique']
    data=client.call('Runtime.evaluate',{'expression':"JSON.stringify({headings:Array.from(document.querySelectorAll('h2')).map(h=>({text:h.innerText,y:Math.floor(h.getBoundingClientRect().top+scrollY)})),tables:Array.from(document.querySelectorAll('table')).map(e=>({width:e.getBoundingClientRect().width,scrollWidth:e.scrollWidth,font:getComputedStyle(e.querySelector('td')).fontSize,color:getComputedStyle(e.querySelector('td')).color})),listMarkers:Array.from(document.querySelectorAll('ul')).map(e=>({type:getComputedStyle(e).listStyleType,items:e.children.length})),images:Array.from(document.images).map(e=>({alt:e.alt,filter:getComputedStyle(e).filter,width:e.getBoundingClientRect().width})),styles:{bodyColor:getComputedStyle(document.body).color,bodyBackground:getComputedStyle(document.body).backgroundColor}})",'returnByValue':True})
    d=json.loads(data['result']['value']);full_height=int(client.call('Page.getLayoutMetrics')['cssContentSize']['height'])
    def shot(name,y,h):
     result=client.call('Page.captureScreenshot',{'format':'png','fromSurface':True,'captureBeyondViewport':True,'clip':{'x':0,'y':y,'width':width,'height':h,'scale':1}},timeout=30)
     p=out/name;p.write_bytes(base64.b64decode(result['data']));return {'path':str(p.relative_to(post)),'sha256':sha256_file(p)}
    shots=[shot(f'{theme}-{width}-full.png',0,full_height)]
    for part,y in enumerate(range(700 if width==360 else 800,full_height,1800),1):
     shots.append(shot(f'{theme}-{width}-reading-{part}.png',y,min(1800,full_height-y)))
    if width==360:
     for label,needle,shot_height in [('table','같은 종합',1500),('ending','Astra를 쓰고',min(2000,full_height))]:
      y=max(0,next(x['y'] for x in d['headings'] if needle in x['text'])-15)
      shots.append(shot(f'{theme}-{width}-{label}.png',y,min(shot_height,full_height-y)))
    records.append({'theme':theme,'width':width,'preview_sha256':sha256_file(html),'browser':chrome.version.get('Browser'),'scope':'independent_supplementary_full_page_inspection','measurements':m,'details':d,'screenshots':shots})
(out/'inspection.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
print(json.dumps([{'theme':x['theme'],'width':x['width'],'height':x['measurements']['scroll_height'],'tables':x['details']['tables'],'listMarkers':x['details']['listMarkers'],'images':x['details']['images']} for x in records],ensure_ascii=False,indent=2))
