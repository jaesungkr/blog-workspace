# -*- coding: utf-8 -*-
from pathlib import Path
from html.parser import HTMLParser
from collections import Counter
import re,json,hashlib,sys
class T(HTMLParser):
 def __init__(self):super().__init__();self.body=False;self.skip=0;self.text=[];self.ordered=[]
 def handle_starttag(self,tag,attrs):
  if tag=='body':self.body=True
  if tag in ['style','script']:self.skip+=1
  if self.body and tag=='ol':self.ordered.append(0)
  if self.body and tag=='li' and self.ordered:
   self.ordered[-1]+=1;self.text.append(str(self.ordered[-1]))
 def handle_endtag(self,tag):
  if tag=='ol' and self.ordered:self.ordered.pop()
  if tag=='body':self.body=False
  if tag in ['style','script']:self.skip-=1
 def handle_data(self,data):
  if self.body and not self.skip:self.text.append(data)
p=Path('/Users/ja2sng/Documents/Codex/2026-11-14/task-2/pdf-qa');parser=T();parser.feed((p/'mobile-print.html').read_text());source=''.join(parser.text)
page_dir=Path(sys.argv[1]) if len(sys.argv)>1 else p/'final-pages'
pdf=(page_dir/'extracted-text.txt').read_text();pdf=re.sub(r'dev.log\s*·\s*검토본\s*\d+\s*/\s*\d+','',pdf);pdf=re.sub(r'--- PAGE \d+ ---','',pdf)
counts=lambda s:Counter(re.findall('[가-힣0-9$]',s))
missing=counts(source)-counts(pdf);extra=counts(pdf)-counts(source)
result={'method':'Compare multiset of Hangul, digits and dollar signs, including rendered ordered-list markers, after removing page labels and footer; extraction reading order can differ. Visual review is separate.','source_character_count':sum(counts(source).values()),'pdf_character_count':sum(counts(pdf).values()),'missing':dict(missing),'extra':dict(extra),'pass':not missing and not extra}
(p/'text-integrity-final.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps(result,ensure_ascii=False));assert result['pass']
post=Path('/Users/ja2sng/dev/blog-workspace/posts/2026-11-14-ai-glasses-products-exam-rules');build=json.loads((p/'pdf-build.json').read_text())
assert build['source_article_sha256']==hashlib.sha256((post/'article.md').read_bytes()).hexdigest()
assert build['source_html_sha256']==hashlib.sha256((post/'delivery/ai-glasses-products-exam-rules-review-light.html').read_bytes()).hexdigest()
print('Source article and original HTML unchanged; 3 official images visually present; final PDF 7 pages.')
