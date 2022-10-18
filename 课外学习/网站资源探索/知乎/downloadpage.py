import json
import time

import requests
from lxml import html
etree=html.etree
from bs4 import BeautifulSoup
url='https://www.zhihu.com/people/13990361026'
header={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',

}
# link=open('D:\Pics\sunyunzhu.txt','w+',encoding='utf-8')
def request_d():
    res=requests.get(url,headers=header)
    main_page = BeautifulSoup(res.text, "html.parser")
    workshopItem = main_page.find_all("script", id="js-initialData")
    # print(workshopItem[0].text)
    dicts=json.loads(workshopItem[0].text)
    initialState=dicts['initialState']['entities']['articles']
    arry=[]
    j=0
    for i in initialState:
        arry.append([])
        # print(initialState[i])
        imageUrl=initialState[i]['imageUrl']
        print(imageUrl)
        content=initialState[i]['content']
        title=initialState[i]['title']
        updated=initialState[i]['updated']
        time2 = time.localtime(updated)
        update_time = time.strftime('%Y-%m-%d %H:%M:%S', time2)
        arry[j].append(title)
        arry[j].append(update_time)
        arry[j].append(imageUrl)
        content_b = BeautifulSoup(content, "html.parser")
        img=content_b.find_all("img",class_="origin_image zh-lightbox-thumb")
        # link.write('\n\n\n\n')
        for o in img:
            original=o.get('data-original')
            print(original)
            arry[j].append(original)
            # link.write(original)
            # link.write('\n')
        print(len(img))
        # print(img)
        print("-----------------------------------------")
        while len(arry[j]) != 32:
            arry[j].append(' ')
        print(len(arry[j]))
        j=j+1
    return arry
# request_d()
# workshopItem = main_page.find_all("div", class_="List")
# lists=workshopItem[0].find_all("div",role="list")
# List_item=lists[0].find_all("div",class_="List-item")
# # for l in List_item:
# #     print(l)
# print(List_item[1])
# print(len(List_item))
# # print(workshopItem)
# print(len(workshopItem))


# htmls=etree.HTML(res.text)
# print(res.text)
# print(htmls)
# list=htmls.xpath("/html/body/div/div/main/div/div/div[3]/div/div/div/div/div/div/div[2]/div/div[]/div")
# lists=htmls.xpath("/html/body/div/div/main/div/div/div[3]/div/div/div/div/div/div/div[2]/div/div[5]")
# for l in lists:
#     figure=l.xpath("./div/div/div/div/span/figure")
#     # for f in figure:
#     #     # actualsrc=f.xpath("./img/@data-actualsrc")
#     #     # watermark=f.xpath('./img/@data-default-watermark-src')
#     #     # original = f.xpath('./img/@data-original')
#     #     # print(actualsrc)
#     #     # print(watermark)
#     #     # print(original)
#     #     # src = f.xpath('./img/@src')
#     #     # print(src)
#     #     noscript=f.xpath('./noscript[@class="xh-highlight"]/text()')
#     #     print(noscript)
#     #     # img=f.find("noscript")
#     #     # print(img.text)
#     # print(figure)
#     # print(len(figure))
# # print(Question_main)
# print(len(lists))
# print(lists)
