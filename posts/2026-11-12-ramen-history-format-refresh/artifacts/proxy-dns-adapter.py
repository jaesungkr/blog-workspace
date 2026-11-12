# Runtime-only DNS compatibility adapter: validates actual public DoH answers;
# canonical validator/network request code remains unchanged.
import socket,urllib.request,json,sys,runpy,ipaddress
original=socket.getaddrinfo
def resolve(host,port,*args,**kwargs):
 try:return original(host,port,*args,**kwargs)
 except socket.gaierror:
  if host!='blog.kakaocdn.net':raise
  with urllib.request.urlopen('https://dns.google/resolve?name=blog.kakaocdn.net&type=A',timeout=10) as r:d=json.load(r)
  ips=[x['data'] for x in d.get('Answer',[]) if x['type']==1]
  if not ips or any(not ipaddress.ip_address(i).is_global for i in ips):raise ValueError('Invalid public DNS result')
  return [(socket.AF_INET,socket.SOCK_STREAM,6,'',(i,port)) for i in ips]
socket.getaddrinfo=resolve
script=sys.argv.pop(1);sys.path.insert(0,str(__import__('pathlib').Path(script).resolve().parent));runpy.run_path(script,run_name='__main__')
