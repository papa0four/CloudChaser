import urllib.request
from pprint import pprint
from html_table_parser import HTMLTableParser
import pandas as pd

def url_get_contents(url):
    req = urllib.request.Request(url=url)
    f = urllib.request.urlopen(req)
    return f.read()

xhtml = url_get_contents('https://myip.ms/view/ip_owners/106784/Baidu_Inc.html').decode('utf-8')

p = HTMLTableParser()
p.feed(xhtml)

pprint(p.tables)
print(pd.DataFrame(p.tables))
