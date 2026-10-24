"""Creator-only local preflight; this does not write final-page approvals."""
import base64
import json
import sys
from pathlib import Path

post = Path(__file__).resolve().parents[2]
repo = post.parents[1]
sys.path.insert(0, str(repo / '.agents/skills/dev-log-rich-post-workspace-v2/scripts'))
from capture_rich_qa_v2 import ChromeProcess, WebSocket, CDPClient, find_chrome, evaluate_page

out = post / 'artifacts/qa-v2/local-screenshots'
out.mkdir(exist_ok=True)
records = []
with ChromeProcess(find_chrome(None), 20) as chrome:
    with WebSocket(chrome.page_websocket_url, timeout=30) as ws:
        client = CDPClient(ws, timeout=30)
        client.call('Page.enable')
        client.call('Runtime.enable')
        for theme, folder in [('light', 'preflight'), ('dark', 'preflight-dark')]:
            uri = (post / 'artifacts/qa-v2' / folder / 'gemini-4-argon-vs-gpt-6-astra-rich-preview.html').as_uri()
            for width, height in [(1280, 900), (360, 800)]:
                client.call('Emulation.setDeviceMetricsOverride', {'width':width,'height':height,'deviceScaleFactor':1,'mobile':width < 735})
                client.discard_events('Page.loadEventFired')
                client.call('Page.navigate', {'url':uri})
                client.wait_event('Page.loadEventFired', timeout=30)
                m = evaluate_page(client, 20)
                assert m['images_loaded'], 'Unloaded image'
                assert m['scroll_width'] == m['client_width'] == width, 'Horizontal overflow'
                assert m['h1_count'] == 1 and m['toc_targets_unique'], 'Heading/TOC problem'
                layout = client.call('Page.getLayoutMetrics')['cssContentSize']
                full_height = int(layout['height'])
                def shot(name, y, shot_height):
                    result = client.call('Page.captureScreenshot', {'format':'png','fromSurface':True,'captureBeyondViewport':True,'clip':{'x':0,'y':y,'width':width,'height':shot_height,'scale':1}}, timeout=30)
                    (out / name).write_bytes(base64.b64decode(result['data']))
                shot(f'{theme}-{width}-full.png', 0, full_height)
                shot(f'{theme}-{width}-top.png', 0, height)
                if width == 360:
                    positions = client.call('Runtime.evaluate', {'expression':"JSON.stringify(Array.from(document.querySelectorAll('h2')).map(h=>({text:h.innerText,y:Math.floor(h.getBoundingClientRect().top+scrollY)})))",'returnByValue':True})
                    headings = json.loads(positions['result']['value'])
                    for label, needle in [('benchmark', '같은 종합'), ('choice', 'Astra를 쓰고')]:
                        y = max(0,next(h['y'] for h in headings if needle in h['text']) - 20)
                        shot(f'{theme}-{width}-{label}.png', y, min(1800,full_height-y))
                m.update(theme=theme,width=width,height=height,full_height=full_height,scope='creator_local_preflight_only',browser=chrome.version.get('Browser'))
                records.append(m)
(out / 'measurements.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
print(json.dumps([{'theme':r['theme'],'width':r['width'],'full_height':r['full_height'],'overflow':r['scroll_width']-r['client_width'],'images_loaded':r['images_loaded']} for r in records],indent=2))
