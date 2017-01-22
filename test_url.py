import urllib.request,re
from bs4 import BeautifulSoup

zz = r'vjread\.aspx\?id=.{8}-.{4}-.{4}-.{4}-.{0,19}'
tar1 = 'vjread.aspx?id=6a77f370-12ca-47cc-846d-554a20dca536&vj'
tar2 = "vjread.aspx?id=ab5f62eb-c79f-4c97-9dae-b43e67110d92&amp;vj"
##59
##59

ful_url = 'http://scc.whut.edu.cn/'
res = re.search(zz,tar1)
res1 = re.search(zz,tar2)
print(res)
print(res1)
