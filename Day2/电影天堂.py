import requests
import re
import csv
from bs4 import BeautifulSoup
domain="https://www.dy2018.com/"
resp=requests.get(domain)
resp.encoding='gb2312'
# print(resp.text)

obj1=re.compile(r"2022必看热片.*?<ul>(?P<ul>.*?)</ul>",re.S)
obj2=re.compile(r"<a href='(?P<href>.*?)'",re.S)
obj3=re.compile(r'◎片　　名(?P<movie>.*?)<br />'
                r'.*?<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<download>.*?)">',re.S)
result1=obj1.finditer(resp.text)
child_href_list=[]
for it in result1:
    ul=it.group('ul')
    # print(ul)
    result2=obj2.finditer(ul)
    for itt in result2:
        child_href=domain+itt.group('href').strip("/")
        child_href_list.append(child_href)
        # print(itt.group('href'))

f=open("Movie.csv",mode="w",encoding="utf-8",newline='')
writer=csv.writer(f)
for href in child_href_list:
    child_resp=requests.get(href)
    child_resp.encoding='gb2312'
    # print(child_resp.text)
    result3=obj3.search(child_resp.text)
    dic=result3.groupdict()
    writer.writerow(dic.values())
    print(result3.group("movie"))
    print(result3.group("download"))
    # break
resp.close()