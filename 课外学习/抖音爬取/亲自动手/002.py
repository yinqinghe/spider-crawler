import requests
import time
import json
# from lxml import html
# etree=html.etree
# url="https://v.douyin.com/JWTACSX/"
url='https://www.iesdouyin.com/web/api/v2/aweme/post/?sec_uid=MS4wLjABAAAAxLux6r_y0s8aC7Jw2O1KHtqh6CeWr18p8mVO3_oyjCU&max_cursor=0&count=2000'
header = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'upgrade-insecure-requests': '1',
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",

}

params= None
# response = requests.get(url, params=params, headers=self.headers, timeout=10)
print(url)
response=requests.get(url=url,headers=header,params=params,timeout=10)
html = json.loads(response.content.decode())
print(html)
