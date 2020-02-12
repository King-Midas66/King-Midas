import requests
from bs4 import BeautifulSoup

url="https://jgirl.ddns.net/WebPages/%E9%95%B7%E6%81%A8%E6%AD%8C.htm"
page=requests.get(url)
soup=BeautifulSoup(page.text,"html5lib")
#若為亂碼(page.content.decode("utf-8"),"html5lib")
lines=soup.find_all(class_="MsoNormal")

s=""
for le in lines:
    s+=le.text+"\n"
print(s)
