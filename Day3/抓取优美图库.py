import requests
from bs4 import BeautifulSoup
import time
url="https://www.umei.cc/bizhitupian/meinvbizhi/yangyanmeinv.htm"
domain="https://www.umei.cc/"
resp=requests.get(url)
resp.encoding='utf-8'
# print(resp.text)

main_page=BeautifulSoup(resp.text,"html.parser")
alist=main_page.find("div",class_='TypeList').find_all("a")
# print(alist)
for a in alist:
    child_href = domain + a.get('href')
    # print(a.get('href'))
    # print(child_href)
    child_page_resp=requests.get(child_href)
    child_page_resp.encoding='utf-8'
    child_page_text=child_page_resp.text

    child_page=BeautifulSoup(child_page_text,"html.parser")
    p=child_page.find("div",class_="ImageBody")
    try:
        img=p.find("img")
        src=img.get("src")
        print(src)
    except:
        print("None")

    img_resp=requests.get(src)#得到图片
    # img_resp.content
    img_name=src.split("/")[-1]
    with  open("img/"+img_name,mode="wb") as f:
        f.write(img_resp.content)

    print("over!!!",img_name)
    time.sleep(1)

    # break

print("allover!!!")
resp.close()