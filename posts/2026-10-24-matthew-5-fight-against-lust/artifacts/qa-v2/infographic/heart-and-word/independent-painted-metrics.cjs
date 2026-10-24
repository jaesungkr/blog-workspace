const sharp=require('/Users/ja2sng/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/sharp');
const fs=require('fs');const path=require('path');
(async()=>{
 const img=path.resolve(__dirname,'../../../../assets/heart-and-word-diagram-v1.png');
 const {data,info}=await sharp(img).ensureAlpha().raw().toBuffer({resolveWithObject:true});
 const bounds=[];
 const regions=[['headline',50,40,850,90],['hidden-main',300,200,620,65],['hidden-support',300,285,620,65],['repent-main',300,480,620,65],['repent-support',300,565,620,65],['word-main',300,760,620,65],['word-support',300,845,620,65]];
 for(const [name,x,y,w,h] of regions){
  let minX=Infinity,minY=Infinity,maxX=-1,maxY=-1;
  for(let yy=y;yy<y+h;yy++)for(let xx=x;xx<x+w;xx++){
   const p=(yy*info.width+xx)*4;
   if(Math.abs(data[p]-247)+Math.abs(data[p+1]-244)+Math.abs(data[p+2]-238)>100){minX=Math.min(minX,xx);minY=Math.min(minY,yy);maxX=Math.max(maxX,xx);maxY=Math.max(maxY,yy);}
  }
  bounds.push({name,source_pixels:{left:minX,top:minY,right:maxX,bottom:maxY,width:maxX-minX+1,height:maxY-minY+1},logical:{left:minX/2,top:minY/2,right:(maxX+1)/2,bottom:(maxY+1)/2,height:(maxY-minY+1)/2}});
 }
 const gaps=[0,1,2].map(i=>{const main=bounds[1+i*2],support=bounds[2+i*2];return{group:i+1,gap:support.logical.top-main.logical.bottom,smaller_height:Math.min(main.logical.height,support.logical.height),ratio:(support.logical.top-main.logical.bottom)/Math.min(main.logical.height,support.logical.height)};});
 fs.writeFileSync(path.join(__dirname,'independent-painted-metrics.json'),JSON.stringify({method:'Direct pixel bounds of original raster, distance from #f7f4ee greater than 100 summed RGB; no derivative image produced.',bounds,gaps},null,2));
})();
