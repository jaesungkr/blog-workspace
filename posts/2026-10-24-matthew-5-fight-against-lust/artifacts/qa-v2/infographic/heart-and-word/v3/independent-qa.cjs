const {chromium}=require('/Users/ja2sng/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const sharp=require('/Users/ja2sng/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/sharp');
const fs=require('fs');const path=require('path');
(async()=>{
 const q=__dirname,img=path.resolve(q,'../../../../../assets/heart-and-word-diagram-v3.png');
 const browser=await chromium.launch({headless:true,executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'});
 const page=await browser.newPage({deviceScaleFactor:1});
 for(const [name,width,margin] of [['publication-320',320,0],['mobile-360',360,20]]){
  const file=path.join(q,'independent-'+name+'.html');
  fs.writeFileSync(file,'<!doctype html><html lang="ko"><meta charset="utf-8"><title>Untouched original raster QA</title><style>body{margin:'+margin+'px;background:white}img{display:block;width:320px;height:512px}</style><img src="file://'+img+'" alt="마음에 말씀을 두기">');
  await page.setViewportSize({width,height:512+margin*2});await page.goto('file://'+file);await page.locator('img').evaluate(e=>e.decode());
  await page.screenshot({path:path.join(q,'independent-'+name+'.png'),fullPage:true});
 }
 await page.setViewportSize({width:640,height:1024});
 await page.setContent('<style>body{margin:0}img{display:block;width:640px;height:1024px}</style><img src="file://'+img+'">');await page.locator('img').evaluate(e=>e.decode());
 for(const [name,y,height] of [['title',0,160],['first-state',190,160],['first-transition',340,160],['second-state',490,140],['second-transition',630,160],['final-state',775,190]])await page.screenshot({path:path.join(q,'independent-crop-'+name+'.png'),clip:{x:40,y,width:560,height}});
 await browser.close();
 const {data,info}=await sharp(img).ensureAlpha().raw().toBuffer({resolveWithObject:true});
 const bounds=[];
 for(const [name,x,y,w,h,bg]of [['title',70,40,500,100,[245,245,245]],['first-transition',350,390,210,45,[245,245,245]],['second-transition',350,680,210,45,[245,245,245]],['middle-line1',210,510,220,45,[245,245,245]],['middle-line2',210,560,220,45,[245,245,245]],['final-main',140,810,360,50,[241,231,228]],['final-support',170,875,300,50,[241,231,228]]]){
  let minX=Infinity,minY=Infinity,maxX=-1,maxY=-1;for(let yy=y;yy<y+h;yy++)for(let xx=x;xx<x+w;xx++){let p=(yy*info.width+xx)*4;if(Math.abs(data[p]-bg[0])+Math.abs(data[p+1]-bg[1])+Math.abs(data[p+2]-bg[2])>110){minX=Math.min(minX,xx);minY=Math.min(minY,yy);maxX=Math.max(maxX,xx);maxY=Math.max(maxY,yy);}}
  bounds.push({name,logical:{left:minX/2,top:minY/2,right:(maxX+1)/2,bottom:(maxY+1)/2,height:(maxY-minY+1)/2}});
 }
 fs.writeFileSync(path.join(q,'independent-painted-metrics.json'),JSON.stringify({method:'Original pixels, summed RGB distance >110; viewBox logical units are half raster pixels.',bounds},null,2));
})();
