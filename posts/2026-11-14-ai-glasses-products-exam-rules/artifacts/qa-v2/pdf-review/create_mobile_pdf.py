# -*- coding: utf-8 -*-
from pathlib import Path
import sys,base64,json,hashlib
repo=Path('/Users/ja2sng/dev/blog-workspace');post=repo/'posts/2026-11-14-ai-glasses-products-exam-rules';task=Path('/Users/ja2sng/Documents/Codex/2026-11-14/task-2')
sys.path.insert(0,str(repo/'.agents/skills/dev-log-rich-post-workspace-v2/scripts'))
from capture_rich_qa_v2 import ChromeProcess,find_chrome,WebSocket,CDPClient,evaluate_page
q=task/'pdf-qa';q.mkdir(exist_ok=True)
original=post/'delivery/ai-glasses-products-exam-rules-review-light.html'
html=original.read_text().replace(' 모바일에서는 표를 좌우로 밀어 나머지 열을 볼 수 있다.','')
css='''
@page { size:420pt 760pt; margin:24pt 23pt 32pt; }
@media print {
 html,body { background:white !important; color:#202124 !important; }
 .rich-preview-header { width:100% !important; padding:4pt 0 18pt !important; margin:0 !important; }
 .rich-preview-header p { font-size:10pt !important; margin-bottom:8pt !important; }
 .rich-preview-header h1 { font-size:24pt !important; line-height:1.3 !important; }
 .devlog-rich { width:100% !important; max-width:none !important; font-size:13pt !important; line-height:1.65 !important; }
 .devlog-rich__section { padding:16pt 0 !important; background:white !important; }
 .devlog-rich__section > * { width:100% !important; max-width:none !important; }
 .devlog-rich p, .devlog-rich li { font-size:13pt !important; line-height:1.65 !important; widows:3; orphans:3; break-inside:avoid; }
 .devlog-rich p { margin:0 0 12pt !important; }
 .devlog-rich h2, .devlog-rich h3 { font-size:18pt !important; line-height:1.35 !important; margin:12pt 0 !important; break-after:avoid; }
 .devlog-rich__toc { padding:12pt 14pt !important; margin:14pt 0 !important; break-inside:avoid; }
 .devlog-rich__toc li { font-size:11pt !important; line-height:1.5 !important; }
 .devlog-rich__toc p { font-size:11pt !important; }
 .devlog-rich__figure { width:100% !important; max-width:100% !important; margin:14pt 0 !important; break-inside:avoid; }
 .devlog-rich__image { width:100% !important; max-width:100% !important; height:auto !important; }
 .devlog-rich__caption { font-size:10pt !important; line-height:1.5 !important; margin-top:7pt !important; }
 .devlog-rich .rich-table-wrap { width:100% !important; overflow:visible !important; margin:12pt 0 !important; break-inside:avoid !important; }
 .devlog-rich .rich-table-wrap table { width:100% !important; min-width:0 !important; max-width:100% !important; table-layout:fixed !important; font-size:10.5pt !important; break-inside:avoid !important; page-break-inside:avoid !important; }
 .devlog-rich .rich-table-wrap td,.devlog-rich .rich-table-wrap th { padding:7pt 6pt !important; font-size:10.5pt !important; line-height:1.5 !important; overflow-wrap:anywhere !important; word-break:normal !important; }
 .devlog-rich table th:first-child,.devlog-rich table td:first-child { width:28% !important; }
 .devlog-rich table thead { display:table-header-group !important; }
 .devlog-rich table tr { break-inside:avoid !important; }
 .devlog-rich a { color:#0066aa !important; }
}
'''
html=html.replace('</head>','<style>'+css+'</style></head>')
preview=q/'mobile-print.html';preview.write_text(html)
output=task/'exports/ai-glasses-products-exam-rules-mobile-review.pdf'
with ChromeProcess(find_chrome(None),20) as chrome:
 with WebSocket(chrome.page_websocket_url,timeout=45) as ws:
  c=CDPClient(ws,timeout=45);c.call('Page.enable');c.call('Runtime.enable')
  c.call('Emulation.setDeviceMetricsOverride',{'width':560,'height':1013,'deviceScaleFactor':1,'mobile':False,'dontSetVisibleSize':False})
  c.discard_events('Page.loadEventFired');c.call('Page.navigate',{'url':preview.as_uri()});c.wait_event('Page.loadEventFired',timeout=30)
  evaluate_page(c,15)
  c.call('Runtime.evaluate',{'expression':"(async()=>{await document.fonts.ready;await Promise.all(Array.from(document.images).map(i=>i.decode()));for(const i of document.images){i.scrollIntoView();await new Promise(requestAnimationFrame);await new Promise(requestAnimationFrame);}window.scrollTo(0,0);await new Promise(requestAnimationFrame);await new Promise(requestAnimationFrame);return true})()",'awaitPromise':True,'returnByValue':True})
  c.call('Emulation.setEmulatedMedia',{'media':'print'})
  r=c.call('Page.printToPDF',{'printBackground':True,'preferCSSPageSize':True,'displayHeaderFooter':True,'headerTemplate':'<span></span>','footerTemplate':'<div style="font-size:9px;width:100%;text-align:center;color:#777;font-family:sans-serif">dev.log · 검토본 &nbsp; <span class="pageNumber"></span> / <span class="totalPages"></span></div>','marginTop':0.333,'marginBottom':0.444,'marginLeft':0.319,'marginRight':0.319},timeout=45)
  output.write_bytes(base64.b64decode(r['data']))
record={'source_article_sha256':hashlib.sha256((post/'article.md').read_bytes()).hexdigest(),'source_html_sha256':hashlib.sha256(original.read_bytes()).hexdigest(),'pdf_sha256':hashlib.sha256(output.read_bytes()).hexdigest(),'pdf_bytes':output.stat().st_size,'page_points':[420,760],'pdf_only_changes':['print typography/spacing/pagination','table min-width removed so every column fits','HTML-only swipe-table hint removed'],'source_html_unchanged':True,'images_embedded':3}
(q/'pdf-build.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
print(output,output.stat().st_size)
