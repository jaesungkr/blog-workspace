from pathlib import Path
import sys,json,base64
ROOT=Path('/Users/ja2sng/dev/blog-workspace')
POST=ROOT/'posts/2026-10-25-kimi-k3-1-pro-strengths-vs-opus-5-5'
sys.path.insert(0,str(ROOT/'.agents/skills/dev-log-rich-post-workspace-v2/scripts'))
import capture_rich_qa_v2 as q
OUT=POST/'artifacts/qa-v2/final/inspection'
OUT.mkdir(exist_ok=True)
records=[]
def ev(c,js):
 r=c.call('Runtime.evaluate',{'expression':js,'awaitPromise':True,'returnByValue':True})
 if r.get('exceptionDetails'):raise RuntimeError(str(r))
 return r['result'].get('value')
for theme in ('light','dark'):
 preview=POST/('artifacts/qa-v2/final-rendered' if theme=='light' else 'artifacts/qa-v2/final-dark-rendered')/'kimi-k3-1-pro-strengths-vs-opus-5-5-rich-preview.html'
 with q.ChromeProcess(q.find_chrome(None),20) as chrome:
  with q.WebSocket(chrome.page_websocket_url,timeout=30) as ws:
   c=q.CDPClient(ws,timeout=30)
   c.call('Page.enable');c.call('Runtime.enable');c.call('Network.enable');c.call('Network.setCacheDisabled',{'cacheDisabled':True})
   for width,height in ((1280,900),(360,800),(390,844)):
    start=OUT/f'{theme}-{width}-top.png'
    m=q.capture_viewport(c,preview.as_uri(),width,height,start,30,20)
    detail=ev(c,'''(() => {
      const rect=e=>{let r=e.getBoundingClientRect();return {x:r.x,y:r.y+scrollY,w:r.width,h:r.height}};
      const style=e=>{let s=getComputedStyle(e);return {color:s.color,bg:s.backgroundColor,overflowX:s.overflowX,filter:s.filter,opacity:s.opacity,mixBlendMode:s.mixBlendMode}};
      return {paragraphs:document.querySelectorAll('.devlog-rich p').length,images:[...document.images].map(e=>({alt:e.alt,rect:rect(e),style:style(e),parentStyle:style(e.parentElement)})),tables:[...document.querySelectorAll('table')].map(e=>({rect:rect(e),parentClass:e.parentElement.className,parentWidth:e.parentElement.clientWidth,parentScroll:e.parentElement.scrollWidth,style:style(e.parentElement)})),scrolls:[...document.querySelectorAll('*')].filter(e=>e.scrollWidth>e.clientWidth+1&&['auto','scroll'].includes(getComputedStyle(e).overflowX)).map(e=>({tag:e.tagName,cls:e.className,width:e.clientWidth,scrollWidth:e.scrollWidth,rect:rect(e)})),lists:[...document.querySelectorAll('ul,ol')].map(e=>({rect:rect(e),style:getComputedStyle(e).listStyleType,items:e.children.length})),bodyStyle:style(document.body),articleStyle:style(document.querySelector('.devlog-rich'))};
    })()''')
    m.update(theme=theme,detail=detail)
    full=OUT/f'{theme}-{width}-full.png'
    shot=c.call('Page.captureScreenshot',{'format':'png','captureBeyondViewport':True,'fromSurface':True,'clip':{'x':0,'y':0,'width':width,'height':m['scroll_height'],'scale':1}})
    full.write_bytes(base64.b64decode(shot['data']));m['full']=str(full.relative_to(POST))
    # Test every horizontal region mechanically; focus the price table and image scroll state once per narrow width.
    m['scroll_tests']=ev(c,'''(() => [...document.querySelectorAll('*')].filter(e=>e.scrollWidth>e.clientWidth+1&&['auto','scroll'].includes(getComputedStyle(e).overflowX)).map(e=>{e.scrollLeft=e.scrollWidth;let end=e.scrollLeft;let out={cls:e.className,start:0,end,max:e.scrollWidth-e.clientWidth,documentWidth:document.documentElement.scrollWidth};e.scrollLeft=0;return out}))()''')
    # Independent full-page inspection uses unmodified browser clips, rather than resized image derivatives.
    m['segments']=[]
    for y in range(0,m['scroll_height'],1800):
     part=OUT/f'{theme}-{width}-y{y}.png'
     shot=c.call('Page.captureScreenshot',{'format':'png','captureBeyondViewport':True,'fromSurface':True,'clip':{'x':0,'y':y,'width':width,'height':min(1800,m['scroll_height']-y),'scale':1}})
     part.write_bytes(base64.b64decode(shot['data']));m['segments'].append(str(part.relative_to(POST)))
    if width<500:
     # Native-like image scrollers are a new component of this final remote candidate.
     for index in (1,2,3,4):
      region=ev(c,f'''(async()=>{{let image=document.images[{index}];let p=image.parentElement;while(p&&!['auto','scroll'].includes(getComputedStyle(p).overflowX))p=p.parentElement;if(!p)return null;p.scrollLeft=p.scrollWidth;image.scrollIntoView({{block:'center'}});await new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)));return {{scrollLeft:p.scrollLeft,max:p.scrollWidth-p.clientWidth,docWidth:document.documentElement.scrollWidth}}}})()''')
      shot=c.call('Page.captureScreenshot',{'format':'png','captureBeyondViewport':False,'fromSurface':True})
      (OUT/f'{theme}-{width}-image{index}-end.png').write_bytes(base64.b64decode(shot['data']))
     m['toc_jump']=ev(c,'''(()=>{let a=[...document.querySelectorAll('.devlog-rich__toc a')].at(-1);a.click();let target=document.getElementById(decodeURIComponent(a.hash.slice(1)));return {target:target.id,exists:!!target,hash:location.hash};})()''')
    records.append(m)
    print(theme,width,m['scroll_height'],'done',flush=True)
(OUT/'observations.json').write_text(json.dumps({'reviewer':'/root/source_cold_review','records':records},ensure_ascii=False,indent=2)+'\n')
