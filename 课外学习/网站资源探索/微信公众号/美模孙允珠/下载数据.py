import requests
from urllib.parse import quote
import time
import random
with open('../cookie2.txt','r',encoding='utf-8') as f:
    cookie=f.read()
# print(cookie)
random.seed(time.time())
cookie=cookie.split('\n')[0]

url = 'https://mp.weixin.qq.com/cgi-bin/appmsg?'
def downloadPage(num):
    UA = open("D:\C#\python\爬虫\课外学习\Agent.txt", mode='r', encoding='utf-8')
    U_a = UA.readlines()[random.randint(0,9)]
    U_a = U_a.split('\n')[0]
    header = {
        # 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
        'user-agent': f'{U_a}',
        'cookie': cookie,
    }
    params={
        'action': 'list_ex',
        'begin': f'{num}',  #236   527    52
        'count': '5',
        'fakeid':'MzkyMTE4NDk3MA==',      #Mzg3MzY2MjIwNw==   ，MzkzNjE0MjY2OA==   ，MzkwNjMyOTA2Mw==     ，Mzg3ODY1NDQyOA== 孙允珠名模
        'type': '9',                      #MzU5NDkzODM4Nw==孙允珠图鉴
        'query': '',
        'token':'1009187860',
        'lang': 'zh_CN',
        'f': 'json',
        'ajax': '1',
    }
    res = requests.get(url, headers=header,params=params).json()
    # print(res)
    # print(res.request.headers)
    app_msg_list=res['app_msg_list']
    # print(app_msg_list)
    message=[]
    i=0
    for a in app_msg_list:
        message.append([])
        item=a['create_time']
        time1 = time.localtime(item)
        t=time.strftime('%Y-%m-%d %H:%M:%S', time1)
        # print(t)
        link=a['link']
        title=a['title']
        aid=a['aid']
        update_time=a['update_time']
        time2 = time.localtime(update_time)
        update_time=time.strftime('%Y-%m-%d %H:%M:%S', time2)
        time1 = time.localtime(time.time())
        nowtime = time.strftime('%Y-%m-%d %H:%M:%S', time1)
        message[i].append(link)
        message[i].append(t)
        message[i].append(title)
        message[i].append(aid)
        message[i].append(update_time)
        message[i].append(nowtime)
        i=i+1
    print(len(app_msg_list))
    print(message)
    return message

downloadPage(496)