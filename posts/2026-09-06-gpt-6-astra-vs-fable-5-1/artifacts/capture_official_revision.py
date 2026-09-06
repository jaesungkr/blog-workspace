"""Capture unmodified public publisher pages through Chrome CDP."""
import base64
import json
import sys
from pathlib import Path

POST = Path(__file__).resolve().parents[1]
REPO = POST.parents[1]
sys.path.insert(0, str(REPO / '.agents/skills/dev-log-rich-post-workspace-v2/scripts'))
from capture_rich_qa_v2 import ChromeProcess, WebSocket, CDPClient, find_chrome

PAGES = {
    'openai-astra': 'https://openai.com/index/gpt-6-astra/',
    'anthropic-fable': 'https://www.anthropic.com/claude/fable',
}

def run():
    out = POST / 'artifacts/captures/revision'
    out.mkdir(parents=True, exist_ok=True)
    with ChromeProcess(find_chrome(None), 20) as chrome:
        with WebSocket(chrome.page_websocket_url, 30) as ws:
            client = CDPClient(ws, 30)
            client.call('Page.enable')
            client.call('Runtime.enable')
            client.call('Emulation.setDeviceMetricsOverride', {'width': 1440, 'height': 1000, 'deviceScaleFactor': 1, 'mobile': False})
            for name, url in PAGES.items():
                client.discard_events('Page.loadEventFired')
                client.call('Page.navigate', {'url': url})
                client.wait_event('Page.loadEventFired', 30)
                client.call('Runtime.evaluate', {'expression': 'document.fonts.ready.then(()=>true)', 'awaitPromise': True})
                result = client.call('Runtime.evaluate', {'expression': "JSON.stringify({url:location.href,title:document.title,text:document.body.innerText,headings:Array.from(document.querySelectorAll('h1,h2,h3')).map(e=>({text:e.innerText,y:e.getBoundingClientRect().y+scrollY})),images:Array.from(document.images).map(e=>({src:e.currentSrc,alt:e.alt,width:e.naturalWidth,height:e.naturalHeight,y:e.getBoundingClientRect().y+scrollY})),tables:Array.from(document.querySelectorAll('table')).map(e=>({text:e.innerText,y:e.getBoundingClientRect().y+scrollY,width:e.getBoundingClientRect().width,height:e.getBoundingClientRect().height}))})", 'returnByValue': True})['result']['value']
                (out / f'{name}-page.json').write_text(result+'\n')
                shot = client.call('Page.captureScreenshot', {'format':'png'})
                (out / f'{name}-viewport.png').write_bytes(base64.b64decode(shot['data']))
                print(name, result[:300])

if __name__ == '__main__':
    run()
