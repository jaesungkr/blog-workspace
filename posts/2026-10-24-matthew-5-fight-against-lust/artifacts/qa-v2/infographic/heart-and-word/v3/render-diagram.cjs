const {chromium}=require('/Users/ja2sng/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const fs=require('fs');
const path=require('path');
(async()=>{
const root='/Users/ja2sng/dev/blog-workspace/posts/2026-10-24-matthew-5-fight-against-lust';
const q=root+'/artifacts/qa-v2/infographic/heart-and-word/v3';
const browser=await chromium.launch({headless:true,executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'});
const page=await browser.newPage({viewport:{width:640,height:900},deviceScaleFactor:2});
const failures=[]; page.on('requestfailed',r=>failures.push({url:r.url(),error:r.failure()?.errorText}));
await page.goto('file://'+q+'/heart-and-word-diagram-v3.html',{waitUntil:'networkidle'});
await page.evaluate(()=>document.fonts.ready);
const metrics=await page.locator('svg text').evaluateAll(es=>es.map(e=>({text:e.textContent,family:getComputedStyle(e).fontFamily,size:getComputedStyle(e).fontSize,bbox:{x:e.getBBox().x,y:e.getBBox().y,width:e.getBBox().width,height:e.getBBox().height}})));
const cdp=await page.context().newCDPSession(page);await cdp.send('DOM.enable');await cdp.send('CSS.enable');
const {root:doc}=await cdp.send('DOM.getDocument');const fonts=[];
for(const selector of ['svg>text:first-of-type','svg g[font-size="16"] text','svg g[font-size="12"] text']){
const {nodeId}=await cdp.send('DOM.querySelector',{nodeId:doc.nodeId,selector});fonts.push({selector,...await cdp.send('CSS.getPlatformFontsForNode',{nodeId})});}
await page.locator('svg').screenshot({path:root+'/assets/heart-and-word-diagram-v3.png',omitBackground:true});
fs.writeFileSync(q+'/render-metrics.json',JSON.stringify({renderer:'Host-provisioned Node Playwright and Google Chrome; no runtime installation',viewport:[640,900],viewBox:[320,512],raster:[640,1024],metrics,fonts,failures},null,2));
await page.setViewportSize({width:360,height:700});
await page.screenshot({path:q+'/creator-mobile-360.png',fullPage:true});
await browser.close();console.log(JSON.stringify({rendered:true,failures,fonts}));
})();
