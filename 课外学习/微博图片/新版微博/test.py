import gzip
import urllib.request
import random
import requests
from urllib.parse import urlencode
tem_ff=open("D:\C#\python\爬虫\课外学习\cookie.txt",mode='r',encoding='utf-8')
cookie=tem_ff.readlines()
cookie_F=cookie[1]
print(cookie_F)
cookie_F=cookie_F.split('\n')[0]
UA=open("D:\C#\python\爬虫\课外学习\Agent.txt",mode='r',encoding='utf-8')
U_a=UA.readlines()[random.randint(0,7)]
print(U_a)
U_a=U_a.split('\n')[0]
# print(U_a)
def down(cookie):
    headers = {
        # 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
       # 这个可以从你的浏览器里检查网页里面找 目的是模拟浏览器申请页面
        'user-agent': f'{U_a}',
        'accept':'application/json,text/plain,*/*',
        'accept-encoding': 'gzip,deflate,br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'x-requested-with': 'XMLHttpRequest',
        'x-xsrf-token': 'cvk-RVYhyoTZvJpXapAAgQon',
        'referer': 'https://weibo.com/u/5901859174?lpage=profileRecom',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'cookie':f'{cookie}',
        # 'cookie': 'SINAGLOBAL=35583908945.38466.1632662233304; XSRF-TOKEN=cvk-RVYhyoTZvJpXapAAgQon; SSOLoginState=1642034409; login_sid_t=95f3b9a1768ec4223239e6afdf96ca14; cross_origin_proto=SSL; _s_tentry=login.sina.com.cn; Apache=7587051160949.691.1642166916527; UOR=,,login.sina.com.cn; ULV=1642166916531:2:1:1:7587051160949.691.1642166916527:1632662233311; appkey=; TC-V-WEIBO-G0=b09171a17b2b5a470c42e2f713edace0; wb_view_log=1536*8641.25; SUB=_2A25PI3v2DeRhGeFN41sU9yjKyzuIHXVsWeo-rDV8PUNbmtANLWXakW9NQ6osNSgcGhIYbfxvS9etcnOlnJuC8buI; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFuaaOUryMCMwq33V2cq8pK5JpX5KzhUgL.FoM01h.fS0qcehM2dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMNe0n4SKMcSo5N; ALF=1678262054; WBPSESS=4ARBQ_XtZWWBs3-KYnu7gm4XOt6WLsK6JFPrdZ5S1AWknhzC8DsYuOZm4LaVZJu47zs0LRAq-rZcYE5Fti8Mf0PqcEmeHGRTGwZmXkxBeIafhWkF_rqx8_zTKTtwHkLPAfZ9uq_RpjVXp7x3tMgFqw=='
        # 'cookie': 'SINAGLOBAL=35583908945.38466.1632662233304; XSRF-TOKEN=cvk-RVYhyoTZvJpXapAAgQon; SSOLoginState=1642034409; login_sid_t=95f3b9a1768ec4223239e6afdf96ca14; cross_origin_proto=SSL; _s_tentry=login.sina.com.cn; Apache=7587051160949.691.1642166916527; UOR=,,login.sina.com.cn; ULV=1642166916531:2:1:1:7587051160949.691.1642166916527:1632662233311; appkey=; TC-V-WEIBO-G0=b09171a17b2b5a470c42e2f713edace0; SCF=Aumg2f5Y26rzSqRY9YyhyKbNEXgg32VhSINhjFBDMr0nwS_TpROcSMujJsJmbY4T0L2ekKX_cSyfdH2m9Lz2seM.; SUB=_2A25PPHlHDeRhGeFN41sU9yjKyzuIHXVsSO2PrDV8PUNbmtB-LXPBkW9NQ6osNSRSZbOSVD260Do1dgn4-WLoYDF2; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFuaaOUryMCMwq33V2cq8pK5JpX5KMhUgL.FoM01h.fS0qcehM2dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMNe0n4SKMcSo5N; ALF=1679375511; WBPSESS=4ARBQ_XtZWWBs3-KYnu7gm4XOt6WLsK6JFPrdZ5S1AWknhzC8DsYuOZm4LaVZJu47zs0LRAq-rZcYE5Fti8Mf3__uo5szrRNPkP9vK1csWMehkR-g4tON6bFMaV2ScIMGG74HmtdvAD4gjCf2pX4Ww=='
        # 'cookie': 'SINAGLOBAL=35583908945.38466.1632662233304; XSRF-TOKEN=cvk-RVYhyoTZvJpXapAAgQon; SSOLoginState=1642034409; login_sid_t=95f3b9a1768ec4223239e6afdf96ca14; cross_origin_proto=SSL; _s_tentry=login.sina.com.cn; Apache=7587051160949.691.1642166916527; UOR=,,login.sina.com.cn; ULV=1642166916531:2:1:1:7587051160949.691.1642166916527:1632662233311; appkey=; TC-V-WEIBO-G0=b09171a17b2b5a470c42e2f713edace0; SUB=_2A25PLsc8DeRhGeFN41sU9yjKyzuIHXVsXb_0rDV8PUNbmtANLRnDkW9NQ6osNQnoWbQewI4vRlgHg0DDhy4ExBd7; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFuaaOUryMCMwq33V2cq8pK5JpX5KzhUgL.FoM01h.fS0qcehM2dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMNe0n4SKMcSo5N; ALF=1678502636; WBPSESS=4ARBQ_XtZWWBs3-KYnu7gm4XOt6WLsK6JFPrdZ5S1AWknhzC8DsYuOZm4LaVZJu47zs0LRAq-rZcYE5Fti8Mf7wpFhr1AmwAV_cg9m1-2HcOPTscOvYH0CprYdM9seUFb5CZ0RPIlDPNf64oMq7fLA=='
        # 'Cookie': 'SINAGLOBAL=35583908945.38466.1632662233304; XSRF-TOKEN=cvk-RVYhyoTZvJpXapAAgQon; SSOLoginState=1642034409; login_sid_t=95f3b9a1768ec4223239e6afdf96ca14; cross_origin_proto=SSL; _s_tentry=login.sina.com.cn; Apache=7587051160949.691.1642166916527; UOR=,,login.sina.com.cn; ULV=1642166916531:2:1:1:7587051160949.691.1642166916527:1632662233311; appkey=; TC-V-WEIBO-G0=b09171a17b2b5a470c42e2f713edace0; ALF=1678011891; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9W5NGliR4X6oUDwjC3raLI69; SUB=_2AkMVeAMNf8NxqwJRmfsSym3rb4xwzw3EieKjJPLWJRMxHRl-yT8XqlwDtRB6Pvgt4nYBFh6IuvbkZBBNkNMU4Vl2JLJK; WBPSESS=mm07v0uQ8nV44TNSi6a9LZ151QYbMD66m1ODu9mMYkUgvqw3i-njBUAH8buPJv_2LcdG9yNm0jFlhlBqYsQ_a9zFBGl9XxhS33pc5ZUjmj3u59WPFpTYECpDhB7CC4ymB58DVEOBs0vvqYEhJH1o7mmL2Qa9fJJPgm-A5bW7CIs=; wb_view_log=1536*8641.25'
    }
    params = {
        'uid': 'uid',
        'page': 'page',
        'feature': '0'
    }
    # https://weibo.com/ajax/statuses/mymblog?uid=6448920093&page=1&feature=0
    # url = 'https://weibo.com/ajax/statuses/mymblog?' + urlencode(params)
    #旧版URL
    # url='https://m.weibo.cn/api/container/getIndex?uid=1192515960&t=0&luicode=10000011&lfid=100103&containerid=1076031192515960&page=198'
    #新版URL
    # url='https://weibo.com/ajax/statuses/mymblog?uid=6448920093&page=1&feature=0&displayYear=2021&curMonth=7&stat_date=202107'
    # url='https://weibo.com/u/6448920093?filter=1&page=1'
    # url='https://weibo.com/u/6448920093?filter=1&page=1&display=0&retcode=6102'
    # url='https://m.weibo.cn/profile/info?uid=6448920093'
    # url='https://weibo.com/ajax/statuses/likelist?uid=6915153646&page=1&feature=0'
    # url='https://weibo.com/ajax/profile/myhot?uid=6915153646&page=1&feature=2'
    # url='https://weibo.com/ajax/statuses/mymblog?uid=6915153646&page=20&feature=0'
    # url='https://weibo.com/ajax/statuses/mymblog?uid=6915153646&page=2&feature=17'
    # url='https://weibo.com/ajax/statuses/mymblog?uid=3224882012&page=5&feature=0&displayYear=2021&curMonth=7&stat_date=202107'
    url='https://weibo.com/ajax/statuses/mymblog?uid=5901859174&page=1&feature=0&displayYear=2022&curMonth=02&stat_date=202202'
    print(url)
    response = requests.get(url,headers=headers)
    return response
# page=urllib.request.Request(url,headers=headers)
# response=urllib.request.urlopen(page).read(10000)
# page_info=gzip.decompress(response).decode('utf-8')
res=down(cookie_F)
print(res.json())
a=res.json()
lists=a.get('ok')
# if lists==-100:
#     print(lists)
while(lists==-100):
    cookie_S = cookie[random.randint(0, 1)]
    cookie_S= cookie_S.split('\n')[0]
    res= down(cookie_S)
    aa = res.json()
    # print(aa)
    #     lists = aa.get('ok')
    # print(aa)
# print(len(lists))
tem_ff.close()




