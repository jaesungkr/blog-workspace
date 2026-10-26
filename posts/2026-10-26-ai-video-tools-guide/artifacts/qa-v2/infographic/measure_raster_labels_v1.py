from pathlib import Path
import struct,zlib,json
D=Path(__file__).resolve().parent
P=D.parents[2]/'assets/ai-video-workflow-v1.png'
b=P.read_bytes();w,h,depth,ct,*_=struct.unpack('>IIBBBBB',b[16:29]);assert depth==8 and ct==2
idat=bytearray();o=8
while o<len(b):
 n=struct.unpack('>I',b[o:o+4])[0];kind=b[o+4:o+8];v=b[o+8:o+8+n]
 if kind==b'IDAT':idat.extend(v)
 o+=12+n
raw=zlib.decompress(idat);stride=w*3;rows=[];prev=bytearray(stride);i=0
for y in range(h):
 f=raw[i];i+=1;cur=bytearray(raw[i:i+stride]);i+=stride
 for x in range(stride):
  a=cur[x-3] if x>=3 else 0;up=prev[x];ul=prev[x-3] if x>=3 else 0
  if f==1:v=a
  elif f==2:v=up
  elif f==3:v=(a+up)//2
  elif f==4:
   p=a+up-ul;pa=abs(p-a);pb=abs(p-up);pc=abs(p-ul);v=a if pa<=pb and pa<=pc else up if pb<=pc else ul
  else:v=0
  cur[x]=(cur[x]+v)&255
 rows.append(cur);prev=cur
labels=[]
for label,(x0,y0,x1,y1) in [('자료 준비',(160,5,350,75)),('클립 생성',(630,345,815,410)),('최종 편집',(1080,620,1275,680))]:
 pts=[]
 for y in range(y0,y1):
  for x in range(x0,x1):
   rgb=rows[y][x*3:x*3+3]
   if max(rgb)<130:pts.append((x,y))
 box=[min(p[0] for p in pts),min(p[1] for p in pts),max(p[0] for p in pts)+1,max(p[1] for p in pts)+1]
 labels.append({'text':label,'painted_bounds_px':box,'painted_width_px':box[2]-box[0],'painted_height_px':box[3]-box[1],'painted_height_at_320_css_px':round((box[3]-box[1])*320/w,2),'method':'Dark-pixel bounds within isolated label ROI (all RGB channels <130); no font-size inference.'})
result={'source':[w,h],'source_font_sizes':'unavailable, generated raster','labels':labels}
(D/'label-measurements-v1.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps(result,ensure_ascii=False))
