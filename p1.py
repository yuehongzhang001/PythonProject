import requests
from bs4 import BeautifulSoup

content=requests.get('http://www.qiushibaike.com').content
soup=BeautifulSoup(content,'html.parser')

for a in soup.find_all('a',{'class':'recmd-content'}):
    print a.text.strip()