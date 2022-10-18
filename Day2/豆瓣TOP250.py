import re
import requests
import csv
url = "https://movie.douban.com/top250"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
}
resp = requests.get(url, headers=header)
page_content=resp.text
# print(resp.text)

obj=re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)</span>'
               r'.*?<p class="">.*?<br>(?P<year>.*?)&nbsp'
               r'.*?<span class="rating_num" property="v:average">(?P<score>.*?)</span>'
               r'.*?<span>(?P<num>.*?)人评价</span>',re.S)

result=obj.finditer(page_content)
f=open("data.csv",mode="w",encoding="utf-8")
writer=csv.writer(f)
i=0
for it in result:
    # print(it.group("name"))
    # print(it.group("score"))
    # print(it.group("num")+"人评价")
    # print(it.group("year").strip())
    i=i+1
    dic=it.groupdict()
    dic['year']=dic['year'].strip()
    writer.writerow(dic.values())
f.close()
print(i)
print("over!")
resp.close()