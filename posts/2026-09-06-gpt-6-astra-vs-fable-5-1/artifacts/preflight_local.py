"""Creator-only local preview observations; never writes a final approval."""
import base64
import json
import sys
from pathlib import Path

POST = Path(__file__).resolve().parents[1]
REPO = POST.parents[1]
sys.path.insert(0, str(REPO / '.agents/skills/dev-log-rich-post-workspace-v2/scripts'))
from capture_rich_qa_v2 import ChromeProcess, WebSocket, CDPClient, find_chrome, evaluate_page

def capture(theme):
    directory = 'preflight' if theme == 'light' else 'preflight-dark'
    preview = POST / 'artifacts/qa-v2' / directory / (POST.name[11:] + '-rich-preview.html')
    out = POST / 'artifacts/qa-v2/preflight-observations' / theme
    out.mkdir(parents=True, exist_ok=True)
    observations = []
    with ChromeProcess(find_chrome(None), 20) as chrome:
        with WebSocket(chrome.page_websocket_url, 30) as ws:
            client = CDPClient(ws, 30)
            client.call('Page.enable')
            client.call('Runtime.enable')
            for width in (1280, 360):
                client.call('Emulation.setDeviceMetricsOverride', {
                    'width': width, 'height': 900, 'deviceScaleFactor': 1,
                    'mobile': width == 360})
                client.discard_events('Page.loadEventFired')
                client.call('Page.navigate', {'url': preview.as_uri()})
                client.wait_event('Page.loadEventFired', 30)
                m = evaluate_page(client, 20)
                assert m['scroll_width'] == width, m
                assert m['images_loaded'] and m['h1_count'] == 1 and m['toc_targets_unique'], m
                m['tables'] = client.call('Runtime.evaluate', {
                    'expression': "JSON.stringify(Array.from(document.querySelectorAll('table')).map(t=>({width:t.getBoundingClientRect().width,scroll:t.scrollWidth,text:t.innerText})))",
                    'returnByValue': True})['result']['value']
                observations.append(m)
                height = m['scroll_height']
                cuts = [(0, height, 'full')]
                if width == 360:
                    cuts += [(y, min(1800, height-y), f'part-{y//1800+1:02d}') for y in range(0, height, 1800)]
                for y, h, name in cuts:
                    shot = client.call('Page.captureScreenshot', {
                        'format': 'png', 'captureBeyondViewport': True,
                        'clip': {'x': 0, 'y': y, 'width': width, 'height': h, 'scale': 1}}, 30)
                    (out / f'{width}-{name}.png').write_bytes(base64.b64decode(shot['data']))
    (out / 'observations.json').write_text(json.dumps(observations, ensure_ascii=False, indent=2)+'\n')
    print(theme, [(m['inner_width'], m['scroll_height'], m['images_loaded']) for m in observations])

if __name__ == '__main__':
    capture('light')
    capture('dark')
