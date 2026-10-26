from pathlib import Path
import sys,json,base64,hashlib
B=Path(__file__).resolve().parents[3]
R=B.parents[1]
sys.path.insert(0,str(R/'.agents/skills/dev-log-rich-post-workspace/scripts'))
from capture_rich_qa import ChromeProcess,WebSocket,CDPClient,find_chrome
D=Path(__file__).resolve().parent
H=D/'visual-inspection-v1.html'
receipt={'reviewer':'/root/hero_review','purpose':'Independent supporting-image actual-size display and enlarged regions; untouched original image, not a reduced derivative','source_sha256':hashlib.sha256((B/'assets/ai-video-workflow-v1.png').read_bytes()).hexdigest(),'captures':[]}
with ChromeProcess(find_chrome(None),20) as ch:
 receipt['browser']=ch.version.get('Browser')
 with WebSocket(ch.page_websocket_url,timeout=30) as ws:
  c=CDPClient(ws,timeout=30);c.call('Page.enable');c.call('Runtime.enable')
  c.call('Emulation.setDeviceMetricsOverride',{'width':1500,'height':1200,'deviceScaleFactor':1,'mobile':False})
  c.discard_events('Page.loadEventFired');c.call('Page.navigate',{'url':H.as_uri()});c.wait_event('Page.loadEventFired',30)
  r=c.call('Runtime.evaluate',{'expression':"Promise.all(Array.from(document.images).map(i=>i.decode())).then(()=>Array.from(document.images).map(i=>{let r=i.getBoundingClientRect();return {src:i.src,width:r.width,height:r.height,x:r.x,y:r.y,naturalWidth:i.naturalWidth,naturalHeight:i.naturalHeight}}))",'awaitPromise':True,'returnByValue':True})
  recs=r['result']['value'];receipt['displays']=recs
  assert recs[0]['width']==320 and recs[0]['height']==240,recs
  def shot(name,x,y,w,h,scale=1):
   r=c.call('Page.captureScreenshot',{'format':'png','captureBeyondViewport':True,'clip':{'x':x,'y':y,'width':w,'height':h,'scale':scale}})
   p=D/name;p.write_bytes(base64.b64decode(r['data']));receipt['captures'].append({'file':name,'clip':[x,y,w,h],'scale':scale,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
  shot('actual-320-browser-viewport-v1.png',0,0,360,315)
  native=recs[1];x,y=native['x'],native['y']
  # Focus each exact source region at 1.5x without touching publication bytes.
  for name,box in [('preparation-label-and-scene',(0,0,555,350)),('generation-label-and-frames',(330,345,790,250)),('editing-label-and-timeline',(915,620,525,440)),('connector-preparation-generation',(515,250,170,110)),('connector-generation-editing',(1095,515,170,125))]:
   bx,by,bw,bh=box;shot(name+'-enlarged-v1.png',x+bx,y+by,bw,bh,1.5)
(D/'independent-display-receipt-v1.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'source_sha256':receipt['source_sha256'],'display':receipt['displays'][0],'captures':len(receipt['captures'])},ensure_ascii=False))
