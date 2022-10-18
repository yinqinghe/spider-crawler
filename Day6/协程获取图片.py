import requests
from bs4 import BeautifulSoup
import time
import csv
import re
import asyncio
import aiohttp
import aiofiles

t1 = time.time()
url = "https://www.umei.cc/meinvtupian/xingganmeinv/"
domain = "https://www.umei.cc/"
resp = requests.get(url)
resp.encoding = 'utf-8'
# print(resp.text)
f = open("Picture_link.csv", mode="w", encoding="utf-8", newline='')
writer = csv.writer(f)
obj1 = re.compile(r'<a href="(?P<href>.*?)">下一页</a>', re.S)
obj2 = re.compile(r'(?<=<a href=")(?![\w\W]*?<a href=")[\w\W]*', re.S)
global i
i = 0

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
async def get_next(href_next, j):
    tasks=[]
    print("传进来的参数地址", href_next)
    child_page_resp1 = requests.get(href_next)  # 获取到子页面
    child_page_resp1.encoding = 'utf-8'
    child_page_text1 = child_page_resp1.text
    ii = get_next.count + j
    print("函数调用次数：", get_next.count)
    child_page1 = BeautifulSoup(child_page_text1, "html.parser")
    p = child_page1.find("div", class_="ImageBody")
    try:
        img1 = p.find("img")
        src1 = img1.get("src")  # 获取到子页面的图片下载链接
        # img_resp1 = requests.get(src1)  # 得到图片

        async with aiohttp.ClientSession() as session:
            img_name1 = str(j) + "_" + str(get_next.name) + "_" + str(ii) + ".jpg"
            async with session.get(src1) as resp:
                async with aiofiles.open("img2/" + img_name1, mode="wb") as f:
                    await f.write(await resp.content.read())

        # with  open("img/" + img_name1, mode="wb") as f:
        #     f.write(img_resp1.content)
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
    tasks.append(get_next(href_next_1, j))
    await asyncio.wait(tasks)
async def main():
    tasks=[]
    j = 0
    async for a in alist:
        child_href = domain + a.get('href')  # 获取到主页面的子链接
        # print(a.get('href'))
        # print(child_href)
        time.sleep(0.5)
        child_page_resp = requests.get(child_href)  # 获取到子页面
        # async with aiohttp.ClientSession() as session:
        #     async with session.get(child_href) as child_page_resp:

        j = j + 1
        child_page_resp.encoding = 'utf-8'
        child_page_text = child_page_resp.text
        child_page = BeautifulSoup(child_page_text, "html.parser")
        p = child_page.find("div", class_="ImageBody")
        pp = child_page.find("div", class_="NewPages").find_all("a")
        print("主程序循环次数:", j)
  # 获取子页面图片更多的链接
        try:
            img = p.find("img")
            src = img.get("src")  # 获取到子页面的图片下载链接
            # img_resp = requests.get(src)  # 得到图片
            async with aiohttp.ClientSession() as session:
                img_name = str(j) + "_" + str(1) + "_" + str(get_next.count + j) + ".jpg"
                async with session.get(src) as resp:
                    with open("img2/" + img_name, mode="wb") as f:
                        f.write(await resp.content.read())
            # with  open("img2/" + img_name, mode="wb") as f:
            #     f.write(img_resp.content)
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
        tasks.append(asyncio.create_task(get_next(child_href_next, j)))
        print(web)
    # for url in urls:
    # tasks.append(get_next(child_href_next, j))

    await asyncio.wait(tasks)

if __name__ == '__main__':
    asyncio.run(main())


t2 = time.time()
print("程序运行消耗时间为:", t2 - t1)
resp.close()
