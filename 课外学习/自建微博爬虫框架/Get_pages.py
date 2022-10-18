import time
import random
import requests
from urllib.parse import urlencode
tem_ff=open("D:\C#\python\爬虫\课外学习\cookie.txt",mode='r',encoding='utf-8')

cookie=tem_ff.readlines()

UA=open("D:\C#\python\爬虫\课外学习\Agent.txt",mode='r',encoding='utf-8')
U_a=UA.readlines()[random.randint(0,7)]
U_a=U_a.split('\n')[0]
def Get_page(page, uid,displayYear,curMonth,stat_date):
    cookie_F = cookie[1]
    # print(cookie_F)
    cookie_F = cookie_F.split('\n')[0]
    headers = {
        'user-agent': f'{U_a}',
        'accept': 'application/json,text/plain,*/*',
        'accept-encoding': 'gzip,deflate,br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'x-requested-with': 'XMLHttpRequest',
        'x-xsrf-token': 'cvk-RVYhyoTZvJpXapAAgQon',
        # 'referer': 'https://weibo.com/u/5901859174?lpage=profileRecom',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'Connection':'close',
        'cookie':f'{cookie_F}',
        # 'cookie': 'SINAGLOBAL=35583908945.38466.1632662233304; XSRF-TOKEN=cvk-RVYhyoTZvJpXapAAgQon; SSOLoginState=1642034409; login_sid_t=95f3b9a1768ec4223239e6afdf96ca14; cross_origin_proto=SSL; _s_tentry=login.sina.com.cn; Apache=7587051160949.691.1642166916527; UOR=,,login.sina.com.cn; ULV=1642166916531:2:1:1:7587051160949.691.1642166916527:1632662233311; appkey=; TC-V-WEIBO-G0=b09171a17b2b5a470c42e2f713edace0; wb_view_log=1536*8641.25; SUB=_2A25PI3v2DeRhGeFN41sU9yjKyzuIHXVsWeo-rDV8PUNbmtANLWXakW9NQ6osNSgcGhIYbfxvS9etcnOlnJuC8buI; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFuaaOUryMCMwq33V2cq8pK5JpX5KzhUgL.FoM01h.fS0qcehM2dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMNe0n4SKMcSo5N; ALF=1678262054; WBPSESS=4ARBQ_XtZWWBs3-KYnu7gm4XOt6WLsK6JFPrdZ5S1AWknhzC8DsYuOZm4LaVZJu47zs0LRAq-rZcYE5Fti8Mf0PqcEmeHGRTGwZmXkxBeIafhWkF_rqx8_zTKTtwHkLPAfZ9uq_RpjVXp7x3tMgFqw=='
    }
    params = {
        'uid': uid,
        'page': page,
        'feature':'0',
        'displayYear': displayYear,
        'curMonth': curMonth ,
        'stat_date': stat_date,
    }
    #https://weibo.com/ajax/statuses/mymblog?uid=5901859174&page=1&feature=0&displayYear=2022&curMonth=12&stat_date=202212
    url = 'https://weibo.com/ajax/statuses/mymblog?' + urlencode(params)
    print(url)
    response = requests.get(url,headers=headers)
    # with requests.get(url,headers=headers) as res:
    #     response=res
    re=response.json()
    response.close()
    # print(re)
    try:
        if response.status_code == 200:
            return re
    except requests.ConnectionError as e:
        print("error", e.args)

