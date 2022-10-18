import requests
from bs4 import BeautifulSoup
import time
import csv
import re
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
    "referer": "https://www.umeitu.com/meinvtupian/waiguomeinv/208331.htm"
}

url="https://www.umeitu.com/meinvtupian/waiguomeinv/208331_3.htm"
domain="https://www.umei.cc/"
resp=requests.get(url,headers=header)
resp.encoding='utf-8'
print(resp.headers)
# src="http://kr.shanghai-jiuxin.com/file/mm/20211130/dgb3meirq21.jpg"
# img_resp = requests.get(src,headers=header)  # 得到图片
# img_name="first.jpg"
# with  open("img/" + img_name, mode="wb") as f:
#     f.write(img_resp.content)