const {chromium}=require('/Users/ja2sng/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const fs=require('fs');
(async()=>{
const root='/Users/ja2sng/dev/blog-workspace/posts/2026-10-24-matthew-5-fight-against-lust';
const q=root+'/artifacts/qa-v2/infographic/heart-and-word';
const browser=await chromium.launch({headless:true,executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'});
const page=await browser.newPage({viewport:{width:1000,height:1200},deviceScaleFactor:2});
await page.goto('file://'+q+'/heart-and-word-diagram-v1.html');await page.evaluate(()=>document.fonts.ready);
await page.locator('svg').screenshot({path:root+'/assets/heart-and-word-diagram-v1.png'});
const metrics=await page.locator('svg text').evaluateAll(es=>es.map(e=>({text:e.textContent,font:getComputedStyle(e).fontFamily,size:getComputedStyle(e).fontSize,bbox:{x:e.getBBox().x,y:e.getBBox().y,width:e.getBBox().width,height:e.getBBox().height}})));
const cdp=await page.context().newCDPSession(page);await cdp.send('DOM.enable');await cdp.send('CSS.enable');
const {root:doc}=await cdp.send('DOM.getDocument');const {nodeId}=await cdp.send('DOM.querySelector',{nodeId:doc.nodeId,selector:'svg text'});
const fonts=await cdp.send('CSS.getPlatformFontsForNode',{nodeId});
fs.writeFileSync(q+'/render-metrics.json',JSON.stringify({renderer:'Playwright Node Chromium',canvas:[480,520],raster:[960,1040],metrics,actualFonts:fonts.fonts},null,2));
await browser.close();console.log('Rendered PNG and measured text.');
})();
