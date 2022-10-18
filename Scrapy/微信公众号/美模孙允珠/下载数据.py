import requests
from urllib.parse import quote
import time
import random
with open('../cookie3.txt','r',encoding='utf-8') as f:
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
        'fakeid':'Mzg4MzAzNTIxNQ==',      #Mzg3MzY2MjIwNw==美模孙允珠   ，MzkzNjE0MjY2OA==孙允珠合集   ，MzkwNjMyOTA2Mw==孙允珠定拍     ，Mzg3ODY1NDQyOA== 孙允珠名模
        # 'fakeid': 'MzkzNjMzOTk5Nw==',
        'type': '9',                      #MzU5NDkzODM4Nw==孙允珠图鉴   ，MzkyMTE4NDk3MA==孙允珠工作室精选    ，Mzg4OTcyNDY3OA==大姬姬    , MzkwMTIwMjk2NA==孙允珠sonyoonjoo
        'query': '',                      #MzkzMTI2ODQ1Mg==孙允珠包臀裙    ， MzkxNzE5MTc4Mg==名模孙允珠分享    , MzIyNTI1NDc3NA==女神孙允珠   , Mzg3ODY0NjQ5OA==韩模孙允珠合集
        'token':'2136953398',             #MzU4MTA1MTk4OQ== 韩美女孙允珠    , MzkyNDI2Mjc5NQ==孙允珠    , MzkwNzI0NDk0NQ==孙允珠穿搭    , MzAwOTM4NzA1OQ== 孙允珠颜值女神
        'lang': 'zh_CN',                  #Mzg3MzY2NjE5Nw==孙允珠时尚达人    , MzUyNjMxMTY2NQ==孙允珠名模秀    ， MzkzODI2Njc5Ng==孙允珠最新动态   ,MzkyNjI2ODc1Mg==孙允珠穿搭潮
        'f': 'json',                      #Mzg3MDU4OTUwMw==孙允珠吧    , MzkyMzIxNjI1NQ==孙允珠丝韤穿搭   , MzUyNjcxNjQxMQ==美丽漂亮的孙允珠     ， Mzg5MzczOTkzOA==孙允珠官微
        'ajax': '1',                      #Mzk0NTMxNjg0Nw==孙允珠热门全集    ， MzkxMzMxNDk4MQ==孙允珠热门合集    , Mzg5ODc0MTI1Mg==孙允珠穿搭集    , MzkzMTM0NzkyMQ==孙允珠合集选
    }                                     #Mzg2Njc3MDQ1MA==孙允珠名模集     , Mzg4MTY3NjUwNQ== 孙允珠时尚馆    ， MzkwNzM0MTA4MQ==孙允珠美照     ， MzkzMTI0ODUzNg== 背影如诗
    res = requests.get(url, headers=header,params=params).json()
    # print(res)                          #MzA5Nzk2MTM1MA==菲菲酱TV   , MzkyNjI1MjcxNQ==浮力喵喵    , MzkxNzI3NDYxMw== 光阴图集    , Mzg5NzcyNzkyMQ==京西大小姐
    # print(res.request.headers)          #MzI1MTQwMTAwNQ==每日图集社     , Mzg3MzcxNzc4NQ==蜜汁大团团    ，Mzg5MzM3NTYzOQ==你我终会相遇   ， MzkzNTMxMjI5OA== 庆元春
    app_msg_list=res['app_msg_list']      #MzUyMzI4MTQxMw== 裙秀风姿   ， Mzg5NzY3NDI1Mw==软萌菇凉    ， Mzg2NzY2Njk1Mw==收罗好笑图     ， Mzg4NjcxNjkyNw== 四海珏
    # print(app_msg_list)                 #Mzg5MzczOTY5Mg==图图软件   ， Mzg2NzcxOTM5Mg== 云良阁    ， MzkxNzMwMTc5MA==宅猫图集    ， MzkzNjMzOTk5Nw==姊妹馆
    message=[]                            #Mzg4MzAzNTIxNQ==
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

# downloadPage(0)