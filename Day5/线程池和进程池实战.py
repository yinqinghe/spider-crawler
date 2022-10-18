import requests
import re
import csv
from concurrent.futures import ThreadPoolExecutor#线程池

f = open("Vegetable_Market.csv", mode="w", encoding="utf-8", newline='')
writer = csv.writer(f)
def download_one_page(url,data):
    resp=requests.post(url,data=data)
    resp.encoding="utf-8"
    dic=resp.json()
    for item in dic['list']:
        name=item['prodName']
        date=item['pubDate']
        prodcat=item['prodCat']
        lowprice=item['lowPrice']
        highprice=item['highPrice']
        avgprice=item['avgPrice']
        place=item['place']
        unitinfo=item['unitInfo']
        message=[]
        message.append(prodcat+','+name+','+lowprice+','+avgprice+','+highprice+','+place+','+unitinfo+','+date)
        writer.writerow(message)
        print(data['current'])



if __name__ == '__main__':
    with ThreadPoolExecutor(5) as t:
        for i in range(1,5):
            data = {
                "limit": "20",
                "current": f"{i}"
            }
            t.submit(download_one_page,"http://www.xinfadi.com.cn/getPriceData.html",data)
    print("全部下载完毕！")

f.close()