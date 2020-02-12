import requests
from bs4 import BeautifulSoup

url="https://www.ptt.cc/bbs/nCoV2019/index.html"
page=requests.get(url)
soup=BeautifulSoup(page.text,"html5lib")
#若為亂碼(page.content.decode("utf-8"),"html5lib")
lines=soup.find_all(class_="title")

s=""
for le in lines:
    s+=le.text+"\n"
print(s)

f1=open(input(""),"w",encoding="utf-8")
s=f1.write(s)
f1.close()
