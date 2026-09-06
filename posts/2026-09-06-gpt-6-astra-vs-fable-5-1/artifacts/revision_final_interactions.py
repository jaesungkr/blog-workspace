"""Independent revision QA: exact remote page, scroll endpoints and component structure."""
import base64
import json
import sys
from pathlib import Path
POST = Path(__file__).resolve().parents[1]
REPO = POST.parents[1]
sys.path.insert(0, str(REPO / '.agents/skills/dev-log-rich-post-workspace-v2/scripts'))
from capture_rich_qa_v2 import ChromeProcess, WebSocket, CDPClient, find_chrome, evaluate_page
OUT = POST / 'artifacts/qa-v2/final-observations'

def js(client, expression):
    return client.call('Runtime.evaluate', {'expression':expression, 'returnByValue':True})['result'].get('value')

results = []
for theme in ('light', 'dark'):
    directory = 'final-rendered' if theme == 'light' else 'final-dark-rendered'
    preview = POST / 'artifacts/qa-v2' / directory / (POST.name[11:] + '-rich-preview.html')
    with ChromeProcess(find_chrome(None), 20) as chrome:
        with WebSocket(chrome.page_websocket_url, 30) as ws:
            c = CDPClient(ws, 30)
            c.call('Page.enable'); c.call('Runtime.enable')
            for width in (1280,360):
                c.call('Emulation.setDeviceMetricsOverride', {'width':width,'height':800,'deviceScaleFactor':1,'mobile':width==360})
                c.discard_events('Page.loadEventFired')
                c.call('Page.navigate', {'url':preview.as_uri()})
                c.wait_event('Page.loadEventFired',30)
                evaluate_page(c,20)
                data = js(c, """(() => {
const rect=e=>{const r=e.getBoundingClientRect();return {x:r.x,y:r.y,width:r.width,height:r.height}};
return {width:innerWidth, pageWidth:document.documentElement.scrollWidth,
tables:[...document.querySelectorAll('table')].map(t=>({rows:[...t.rows].map(r=>[...r.cells].map(c=>c.innerText)),width:t.offsetWidth,scrollWidth:t.scrollWidth,wrapperWidth:t.parentElement.clientWidth,wrapperScrollWidth:t.parentElement.scrollWidth})),
figures:[...document.querySelectorAll('figure')].map(f=>({id:f.dataset.mediaId,caption:!!f.querySelector('figcaption'),imageWidth:f.querySelector('img').offsetWidth,filter:getComputedStyle(f.querySelector('img')).filter,mixBlendMode:getComputedStyle(f.querySelector('img')).mixBlendMode,rect:rect(f)})),
preCount:document.querySelectorAll('pre').length,codeCount:document.querySelectorAll('code').length,
listMarkers:[...document.querySelectorAll('ol,ul')].map(e=>({type:getComputedStyle(e).listStyleType,count:e.children.length})),
toc:[...document.querySelectorAll('.devlog-rich__toc a')].map(a=>({text:a.innerText,target:!!document.getElementById(decodeURIComponent(a.hash.slice(1)))}))};})()""")
                data['theme']=theme
                graph=js(c,"""(() => {const s=document.querySelector('.devlog-rich__media-scroll');s.scrollLeft=0;const r=s.getBoundingClientRect();return {clientWidth:s.clientWidth,scrollWidth:s.scrollWidth,imageWidth:s.querySelector('img').getBoundingClientRect().width,overflowX:getComputedStyle(s).overflowX,x:r.x,y:r.y+scrollY,width:r.width,height:r.height};})()""")
                if width==360:
                    for position in ('left','right'):
                        end = js(c, "(() => {const s=document.querySelector('.devlog-rich__media-scroll');s.scrollLeft=" + ('0' if position=='left' else 's.scrollWidth') + ";return {actual:s.scrollLeft,max:s.scrollWidth-s.clientWidth,pageWidth:document.documentElement.scrollWidth}})()")
                        graph[position]=end
                        c.call('Runtime.evaluate', {'expression':"new Promise(resolve=>{document.querySelector('.devlog-rich__media-scroll').scrollIntoView({block:'center'});requestAnimationFrame(()=>requestAnimationFrame(resolve));})",'awaitPromise':True})
                        shot=c.call('Page.captureScreenshot',{'format':'png','captureBeyondViewport':True,'clip':{'x':0,'y':graph['y']-10,'width':360,'height':graph['height']+130,'scale':1}},30)
                        (OUT/theme/f'360-graph-{position}.png').write_bytes(base64.b64decode(shot['data']))
                    assert graph['imageWidth']==560 and graph['right']['actual']==graph['right']['max']==240, graph
                data['graph']=graph
                assert data['pageWidth']==width
                assert len(data['tables'][0]['rows'])==10 and len(data['tables'][1]['rows'])==5
                assert all(len(row)==3 for table in data['tables'] for row in table['rows'])
                results.append(data)
(OUT/'revision-interactions.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
print(json.dumps([{'theme':r['theme'],'width':r['width'],'graph':r['graph'],'table_rows':[len(t['rows'])-1 for t in r['tables']],'pre_count':r['preCount']} for r in results],ensure_ascii=False,indent=2))
