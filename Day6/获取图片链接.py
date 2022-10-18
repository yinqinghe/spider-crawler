import requests
from bs4 import BeautifulSoup
import time
import csv
import re
import asyncio
import aiohttp
header={
     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
}
t1 = time.time()
url = "https://www.umeitu.com/meinvtupian/xingganmeinv/index.htm"
domain = "https://www.umeitu.com/"
resp = requests.get(url,headers=header)
resp.encoding = 'utf-8'
# print(resp.text)
f = open("Picture_link.csv", mode="w", encoding="utf-8", newline='')
writer = csv.writer(f)
obj1 = re.compile(r'<a href="(?P<href>.*?)">下一页</a>', re.S)
obj2 = re.compile(r'(?<=<a href=")(?![\w\W]*?<a href=")[\w\W]*', re.S)
global i
i = 0
j = 0
main_page = BeautifulSoup(resp.text, "html.parser")
alist = main_page.find("div", class_='TypeList').find_all("a")


class CallingCounter(object):
    def __init__(self, func):
        self.func = func
        self.count = 0
        self.name = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        self.name += 1
        return self.func(*args, **kwargs)


# print(alist)
@CallingCounter
def get_next(href_next, j):
    print("传进来的参数地址", href_next)
    child_page_resp1 = requests.get(href_next,headers=header)  # 获取到子页面
    child_page_resp1.encoding = 'utf-8'
    child_page_text1 = child_page_resp1.text
    ii = get_next.count + j
    print("函数调用次数：", get_next.count)
    child_page1 = BeautifulSoup(child_page_text1, "html.parser")
    p = child_page1.find("div", class_="ImageBody")
    try:
        img1 = p.find("img")
        src1 = img1.get("src")  # 获取到子页面的图片下载链接
        img_resp1 = requests.get(src1,headers=header)  # 得到图片
        img_name1 = str(j) +"_"+ str(get_next.name)+"_" + str(ii) + ".jpg"
        with  open("img/" + img_name1, mode="wb") as f:
            f.write(img_resp1.content)
        # print("函数调用",src)
        print(img_name1)
    except:
        print("None")
    pp1 = child_page1.find("div", class_="NewPages").find_all("a")  # 下面使用正则获取url
    web = obj1.search(pp1.__str__())
    try:
        web1 = obj2.search(web.group('href'))
        # print(web1.group())
    except:
        return
    href_next_1 = domain + web1.group()
    get_next(href_next_1, j)


if __name__ == '__main__':

    for a in alist:
        child_href = domain + a.get('href')  # 获取到主页面的子链接
        # print(a.get('href'))
        # print(child_href)
        time.sleep(0.5)
        child_page_resp = requests.get(child_href,headers=header)  # 获取到子页面
        child_page_resp.encoding = 'utf-8'
        child_page_text = child_page_resp.text
        j = j + 1
        print("主程序循环次数:", j)
        child_page = BeautifulSoup(child_page_text, "html.parser")
        p = child_page.find("div", class_="ImageBody")
        pp = child_page.find("div", class_="NewPages").find_all("a")  # 获取子页面图片更多的链接
        try:
            img = p.find("img")
            src = img.get("src")  # 获取到子页面的图片下载链接
            img_resp = requests.get(src,headers=header)  # 得到图片
            img_name = str(j) + "_" + str(1)+ "_" + str(get_next.count + j)+ ".jpg"
            with  open("img/" + img_name, mode="wb") as f:
                f.write(img_resp.content)
            print(src)
        except:
            print("None")

        web = obj1.search(pp.__str__())
        web1 = obj2.search(web.group('href'))
        # web = pp[5].get('href')  # 得到下一页的页面链接
        child_href_next = domain + web1.group()
        print(child_href_next)
        get_next.name = 0
        get_next(child_href_next, j)
        print(web)

t2 = time.time()
print("程序运行消耗时间为:", t2 - t1)
resp.close()
