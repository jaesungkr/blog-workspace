#!/usr/bin/env python3
"""Capture local review previews only; does not record the remote final gate."""
from pathlib import Path
import base64
import hashlib
import json
import sys

REPO = Path(__file__).resolve().parents[4]
POST = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / '.agents/skills/dev-log-rich-post-workspace/scripts'))
from capture_rich_qa import ChromeProcess, WebSocket, CDPClient, find_chrome, evaluate_page

receipt = {'purpose':'local creator preflight; not final remote page approval','actor':'Codex','themes':[]}
with ChromeProcess(find_chrome(None), 20) as chrome:
    receipt['browser'] = chrome.version.get('Browser')
    with WebSocket(chrome.page_websocket_url, timeout=30) as ws:
        c=CDPClient(ws,timeout=30)
        c.call('Page.enable'); c.call('Runtime.enable')
        for theme, folder in [('light','preflight'),('dark','preflight-dark')]:
            out=POST/'artifacts/qa-v2'/folder
            preview=out/'ai-video-tools-guide-rich-preview.html'
            for width,height in [(1280,900),(360,800)]:
                c.call('Emulation.setDeviceMetricsOverride',dict(width=width,height=height,deviceScaleFactor=1,mobile=width<735))
                c.discard_events('Page.loadEventFired')
                c.call('Page.navigate',{'url':preview.as_uri()}); c.wait_event('Page.loadEventFired',timeout=30)
                m=evaluate_page(c,20)
                assert m['scroll_width']==m['client_width']==width, m
                assert m['h1_count']==1 and m['toc_targets_unique'] and m['images_loaded'], m
                def eval_js(expression):
                    r=c.call('Runtime.evaluate',{'expression':expression,'returnByValue':True})
                    assert not r.get('exceptionDetails'),r
                    return r['result'].get('value')
                tables=eval_js("JSON.stringify(Array.from(document.querySelectorAll('table')).map(e=>{let r=e.getBoundingClientRect();return {top:r.top+scrollY,width:r.width,height:r.height,client:e.clientWidth,scroll:e.scrollWidth,text:e.innerText}}))")
                m['tables']=json.loads(tables)
                m['image_count']=eval_js('document.images.length')
                assert m['image_count']==2, m
                image_top=eval_js('document.images[1].getBoundingClientRect().top+scrollY')
                m['theme']=theme
                m['preview_sha256']=hashlib.sha256(preview.read_bytes()).hexdigest()
                shots=[]
                for name,top in [('top',0),('workflow',image_top-120),('services',m['tables'][2]['top']-24),('selection',m['tables'][3]['top']-24),('closing',max(0,m['scroll_height']-height))]:
                    eval_js(f'window.scrollTo(0,{max(0,int(top))})')
                    shot=c.call('Page.captureScreenshot',{'format':'png','fromSurface':True,'captureBeyondViewport':False})
                    dest=out/f'{width}-{name}.png';dest.write_bytes(base64.b64decode(shot['data']));shots.append(dest.name)
                for name,index in ([('services',2),('selection',3)] if width==360 else []):
                    top=max(0,int(m['tables'][index]['top']-24))
                    eval_js(f'window.scrollTo(0,{top});document.querySelectorAll(".rich-table-wrap")[{index}].scrollLeft=10000')
                    shot=c.call('Page.captureScreenshot',{'format':'png','fromSurface':True,'captureBeyondViewport':False})
                    dest=out/f'{width}-{name}-right.png';dest.write_bytes(base64.b64decode(shot['data']));shots.append(dest.name)
                    eval_js(f'document.querySelectorAll(".rich-table-wrap")[{index}].scrollLeft=0')
                eval_js('window.scrollTo(0,0)')
                shot=c.call('Page.captureScreenshot',{'format':'png','captureBeyondViewport':True,'clip':{'x':0,'y':0,'width':width,'height':m['scroll_height'],'scale':1}})
                dest=out/f'{width}-full.png';dest.write_bytes(base64.b64decode(shot['data']));shots.append(dest.name)
                m['screenshots']=shots
                receipt['themes'].append(m)
(POST/'artifacts/qa-v2/local-preflight-measurements.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'browser':receipt['browser'],'profiles':len(receipt['themes']),'checks':'no page overflow; one H1; all TOC targets resolve; image loaded'},ensure_ascii=False))
