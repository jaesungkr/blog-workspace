"""Creator-only local preflight; intentionally not a final-page approval."""
import base64
import json
import sys
from pathlib import Path

POST = Path(__file__).resolve().parents[2]
REPO = POST.parents[1]
sys.path.insert(0, str(REPO / '.agents/skills/dev-log-rich-post-workspace-v2/scripts'))
from capture_rich_qa_v2 import ChromeProcess, WebSocket, CDPClient, evaluate_page, find_chrome

def evaluate(client, expression):
    result = client.call('Runtime.evaluate', {'expression': expression, 'returnByValue': True})
    if result.get('exceptionDetails'):
        raise RuntimeError(result['exceptionDetails'])
    return result['result']['value']

records = []
for theme, directory in [('light', 'preflight'), ('dark', 'preflight-dark')]:
    preview = POST / f'artifacts/qa-v2/{directory}/gpt-6-1-sol-vs-opus-5-5-rich-preview.html'
    output = POST / f'artifacts/qa-v2/{directory}/browser'
    output.mkdir(parents=True, exist_ok=True)
    with ChromeProcess(find_chrome(None), 20) as chrome:
        with WebSocket(chrome.page_websocket_url, timeout=30) as ws:
            client = CDPClient(ws, timeout=30)
            client.call('Page.enable')
            client.call('Runtime.enable')
            for width, height in [(1280, 900), (360, 800)]:
                client.call('Emulation.setDeviceMetricsOverride', {'width': width, 'height': height, 'deviceScaleFactor': 1, 'mobile': width < 735})
                client.discard_events('Page.loadEventFired')
                client.call('Page.navigate', {'url': preview.as_uri()})
                client.wait_event('Page.loadEventFired', timeout=30)
                m = evaluate_page(client, 10)
                assert m['scroll_width'] == width, m
                assert m['h1_count'] == 1 and m['toc_targets_unique'] and m['images_loaded'], m
                tables = evaluate(client, """Array.from(document.querySelectorAll('.rich-table-wrap')).map(el => ({client_width:el.clientWidth,scroll_width:el.scrollWidth,overflow:getComputedStyle(el).overflowX,y:el.getBoundingClientRect().top+scrollY,height:el.getBoundingClientRect().height,text:el.innerText}))""")
                m['theme'] = theme
                m['tables'] = tables
                m['review_type'] = 'creator local preflight, not remote/final approval'
                for table in tables:
                    assert table['scroll_width'] <= table['client_width'] or table['overflow'] in ('auto', 'scroll'), table
                m['screenshots'] = []
                page_height = m['scroll_height']
                for index, y in enumerate(range(0, page_height, height)):
                    evaluate(client, f'window.scrollTo(0,{y}); true')
                    client.call('Runtime.evaluate', {'expression':'new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))','awaitPromise':True})
                    shot = client.call('Page.captureScreenshot', {'format':'png','fromSurface':True,'captureBeyondViewport':False})
                    path = output / f'{width}-page-{index:02d}.png'
                    path.write_bytes(base64.b64decode(shot['data']))
                    m['screenshots'].append(path.relative_to(POST).as_posix())
                if width == 360:
                    for index, table in enumerate(tables):
                        evaluate(client, f"document.querySelectorAll('.rich-table-wrap')[{index}].scrollLeft=10000;window.scrollTo(0,{max(0,int(table['y'])-120)});true")
                        client.call('Runtime.evaluate', {'expression':'new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))','awaitPromise':True})
                        shot = client.call('Page.captureScreenshot', {'format':'png','fromSurface':True,'captureBeyondViewport':False})
                        path = output / f'360-table-{index}-right.png'
                        path.write_bytes(base64.b64decode(shot['data']))
                        m['screenshots'].append(path.relative_to(POST).as_posix())
                records.append(m)
(POST / 'artifacts/qa-v2/local-preflight-measurements.json').write_text(json.dumps(records, ensure_ascii=False, indent=2)+'\n')
print(json.dumps([{'theme':r['theme'],'width':r['inner_width'],'page_height':r['scroll_height'],'overflow':r['scroll_width']-r['client_width'],'tables':r['tables'],'screenshots':len(r['screenshots'])} for r in records],ensure_ascii=False,indent=2))
