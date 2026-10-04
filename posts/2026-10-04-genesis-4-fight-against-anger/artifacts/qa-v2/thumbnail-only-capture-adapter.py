from pathlib import Path
import sys, importlib.util, base64
ROOT=Path('/Users/ja2sng/dev/blog-workspace')
SKILL=ROOT/'.agents/skills/dev-log-rich-post-workspace-v2/scripts'
sys.path.insert(0,str(SKILL))
import capture_rich_qa_v2 as c
POST=ROOT/'posts/2026-10-04-genesis-4-fight-against-anger'

def validate(m,uri,width,height):
    failures=[]
    for key,want in [('ready_state','complete'),('location',uri),('inner_width',width),('inner_height',height),('client_width',width),('h1_count',1),('toc_targets_unique',True),('image_count',0)]:
        if m.get(key)!=want: failures.append(f'{key}: {m.get(key)!r} != {want!r}')
    if m.get('scroll_width')!=m.get('client_width'): failures.append('horizontal overflow')
    if m.get('images') != []: failures.append('unexpected body media')
    if failures: raise c.CaptureError('; '.join(failures))
c.validate_page_measurements=validate
original=c.capture_viewport

def capture(*args,**kwargs):
    rec=original(*args,**kwargs)
    client=args[0]; width=args[2]; height=rec['scroll_height']; staged=args[4]
    target=POST/c.MODE_PATHS[current_mode]['screenshot_root']/staged.name.replace('.png','-full.png')
    result=client.call('Page.captureScreenshot',{'format':'png','fromSurface':True,'captureBeyondViewport':True,'clip':{'x':0,'y':0,'width':width,'height':height,'scale':1}},timeout=30)
    target.write_bytes(base64.b64decode(result['data'],validate=True))
    dims=c.image_dimensions(target)
    if dims!=(width,height): raise c.CaptureError(f'full raster size {dims}')
    rec['full_screenshot']=target.relative_to(POST).as_posix()
    rec['full_screenshot_sha256']=c.sha256_file(target)
    rec['full_screenshot_pixel_width']=width
    rec['full_screenshot_pixel_height']=height
    rec['body_media']='not_applicable_by_user_instruction'
    return rec
c.capture_viewport=capture
for current_mode in ['final-light','final-dark']:
    c.MODE_PATHS[current_mode]['receipt']=c.MODE_PATHS[current_mode]['receipt'].replace('browser-capture.json','thumbnail-only-browser-capture.json')
    args=c.build_parser().parse_args([str(POST),'--mode',current_mode,'--by','thumbnail_review'])
    path=c.run_capture(args)
    import json
    data=json.loads(path.read_text())
    data['scope']='user-requested-thumbnail-only'
    data['strict_v2_media_gate']='not_applicable_by_user_instruction'
    data['adapter_sha256']=c.sha256_file(Path(__file__))
    data['excluded_stock_failures']=['one or more remote images did not load','preview contains no images']
    c.atomic_write_json(path,data)
    print(path)
