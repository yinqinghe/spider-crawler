# from xml import etree

import requests
from lxml import html
etree=html.etree
url="https://beijing.zbj.com/search/f/?kw=saas"
resp=requests.get(url)
# print(resp.text)

html=etree.HTML(resp.text)

divs=html.xpath("/html/body/div[6]/div/div/div[2]/div[5]/div[1]/div")
i=0
for div in divs:
    price=div.xpath("./div/div/a[2]/div[2]/div[1]/span[1]/text()")[0].strip("¥")
    title=div.xpath("./div/div/a[2]/div[2]/div[2]/p/text()")
    company = div.xpath("./div/div/a[1]/div[1]/p/text()")[0]
    location = div.xpath("./div/div/a[1]/div[1]/div/span/text()")[0]
    i=i+1
    # print(title)
    print(price)
    # print(company)
    # print(location)

print("收集的数据数："+str(i))
resp.close()