const {chromium}=require('/Users/ja2sng/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const fs=require('fs');
const path=require('path');
(async()=>{
  const q=__dirname;
  const img=path.resolve(q,'../../../../assets/heart-and-word-diagram-v1.png');
  const browser=await chromium.launch({headless:true,executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'});
  const page=await browser.newPage({deviceScaleFactor:1});
  for(const [name,width,imageWidth] of [['publication-480',520,480],['mobile-360',360,320]]){
    const html='<!doctype html><html lang="ko"><meta charset="utf-8"><title>Original publication raster QA</title><style>body{margin:20px;background:#fff}img{display:block;width:'+imageWidth+'px;height:auto}</style><img src="file://'+img+'" alt="비워 낸 마음에 말씀을 두기">';
    const file=path.join(q,'independent-'+name+'.html');fs.writeFileSync(file,html);
    await page.setViewportSize({width,height:Math.ceil(imageWidth*1040/960)+40});
    await page.goto('file://'+file);await page.locator('img').evaluate(e=>e.decode());
    await page.screenshot({path:path.join(q,'independent-'+name+'.png'),fullPage:true});
  }
  await page.setViewportSize({width:1000,height:1100});
  await page.setContent('<style>body{margin:0}img{display:block;width:960px;height:1040px}</style><img src="file://'+img+'">');
  // File loading stays on the previously opened file-origin QA page.
  await page.locator('img').evaluate(e=>e.decode());
  for(const [name,y,height] of [['headline',0,160],['hidden-heart-and-first-arrow',160,300],['repentance-and-second-arrow',450,290],['word-filled-heart',730,310]]){
    await page.screenshot({path:path.join(q,'independent-crop-'+name+'.png'),clip:{x:0,y,width:960,height}});
  }
  await browser.close();
})();
