from pathlib import Path
import sys,re,json,hashlib,html
from html.parser import HTMLParser
from PIL import Image
REPO=Path('/workspace/blog-workspace')
SCRIPTS=REPO/'.agents/skills/dev-log-rich-post-workspace-v2/scripts'
sys.path.insert(0,str(SCRIPTS))
from render_rich_post_v2 import render_outputs
from md2tistory import convert,split_frontmatter
OUT=Path(__file__).parent
class Content(HTMLParser):
 def __init__(self):super().__init__();self.skip=0;self.text=[];self.links=[];self.alts=[];self.cells=[];self.cell=None
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag in ('style','nav','script'):self.skip+=1
  if self.skip:return
  if tag=='a':self.links.append((a.get('href'),))
  if tag=='img':self.alts.append(a.get('alt'))
  if tag in ('td','th'):self.cell=[]
 def handle_endtag(self,tag):
  if tag in ('style','nav','script'):self.skip-=1
  if tag in ('td','th') and self.cell is not None:self.cells.append(''.join(self.cell));self.cell=None
 def handle_data(self,s):
  if not self.skip:
   self.text.append(s)
   if self.cell is not None:self.cell.append(s)
 def norm(self):return re.sub(r'\s+','', ''.join(self.text))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
reports=[]
for num,slug in [(161,'diagram-design'),(162,'gemini-4-carbon-vs-claude-opus-5-5')]:
 post=REPO/f'posts/2026-10-29-{slug}'; out=OUT/str(num);out.mkdir(exist_ok=True)
 source=(post/'article-draft.md').read_text(); original_body=source.split('\n',1)[1].lstrip('\n')
 meta,_=split_frontmatter((post/'article.md').read_text())
 items=[];lines=[]
 for line in original_body.splitlines():
  m=re.fullmatch(r'!\[(.*?)\]\((.*?)\)',line)
  if m:
   alt,path=m.groups();path=str(Path(path).with_suffix('.png')) if path.endswith('.svg') else path
   file=post/path;w,h=Image.open(file).size; ident=f'post-{num}-image-{len(items)+1}'
   items.append(dict(id=ident,alt=alt,caption='',width=w,height=h,display_width=min(w,916),publish_path=path,tistory_embed=f'<!--REPLACE_NATIVE_{ident}-->',sha256=sha(file)))
   lines.append('{{media:'+ident+'}}')
  else:
   if re.match(r'^#{2,} ',line):line='#'+line
   lines.append(line)
 body='\n'.join(lines)+'\n';(out/'renderer-input.md').write_text(body)
 result={'body':body,'meta':meta,'manifest':{'lead_id':items[0]['id']},'items_by_id':{x['id']:x for x in items},'post_dir':post}
 preview,fragment=render_outputs(result,out)
 dark,_=render_outputs(result,out,preview_theme='dark')
 (out/'rich-preview.html').write_text(preview);(out/'rich-preview-dark.html').write_text(dark);(out/'native-replacement-fragment.html').write_text(fragment)
 # Compare source body and final rich output excluding automatic TOC and media pixels.
 baseline=re.sub(r'^!\[.*?\]\(.*?\)\s*$','',original_body,flags=re.M)
 a=Content();a.feed(convert(baseline));b=Content();b.feed(fragment)
 assert a.norm()==b.norm(),f'{num}: text differs'
 assert a.links==b.links,f'{num}: links differ'
 assert a.cells==b.cells,f'{num}: table cells differ'
 p=Content();p.feed(preview)
 assert p.alts==[x['alt'] for x in items]
 report={'post_id':num,'source_sha256':sha(post/'article-draft.md'),'renderer':'render_rich_post_v2.render_outputs','renderer_sha256':sha(SCRIPTS/'render_rich_post_v2.py'),'css_sha256':sha(SCRIPTS.parent/'assets/rich-post-v2.css'),'markdown_renderer_sha256':sha(REPO/'scripts/md2tistory.py'),'fragment_sha256':sha(out/'native-replacement-fragment.html'),'visible_text_excluding_template_toc':'pass','original_links_order_and_targets':'pass','table_cells_order_and_values':'pass','image_alt_order':'pass','image_count':len(items),'media':items,'status':'provisional native binding and browser QA pending','validation_boundary':'Actual canonical renderer API invoked, not CLI/finalizer pass. Preserve approved prose; do not fabricate canonical source/media/QA records. Automatic TOC repeats existing headings as template navigation. Captions retain original inline formatting and links as original paragraphs; generated caption slots are empty.'}
 (out/'provenance-parity.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');reports.append({k:v for k,v in report.items() if k!='media'})
print(json.dumps(reports,ensure_ascii=False,indent=2))
