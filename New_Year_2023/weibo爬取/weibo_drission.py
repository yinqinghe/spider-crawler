from datetime import datetime
import string
import random
from DrissionPage import WebPage,SessionPage,SessionOptions

# 定义随机字符串的可选字符集
characters = string.ascii_letters + string.digits

so=SessionOptions()
cookies="XSRF-TOKEN=HFVN75npxEc6HCEJfTLJ0CmJ; SSOLoginState=1678761231; _s_tentry=www.weibo.com; Apache=5110636533571.143.1679715960822; SINAGLOBAL=5110636533571.143.1679715960822; ULV=1679715960907:1:1:1:5110636533571.143.1679715960822:; UPSTREAM-V-WEIBO-COM=b09171a17b2b5a470c42e2f713edace0; PC_TOKEN=2d865a583e; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFRkM7ofXBqTSG-KTYyorpe5JpX5KMhUgL.FoMNSo.01Kq4She2dJLoI7pSIg_LIJvE9s8Vehzt; ALF=1682427260; SCF=AspUIZKFp_dZvFulvONf1yrz8X5_NrEbOusV9VJkBZ8Xe_bdGRK0GIa8fU8F9yEzgQ0cueUJ9aJkVNv-eFd7cZM.; SUB=_2A25JJDAvDeRhGeFJ7VsS-SjFzz-IHXVqUCbnrDV8PUNbmtAGLUPMkW9Nf1XPsQ1TH2YiZVTcGB_C-2h4jT5Robcl; WBPSESS=DQswqYJs0y3GED0LZ7HfbTR1Mj06ey6K7vktgXD4vvvVsZUvYx-3oqHJUkE1hTTlbzDsdcs9XAipWb8v3RhZoNqTtZgOe7hKwwViYJFalZ317PfJBqSqR4DxeM3oUiFJgC7vjgK-mw4MmAzht7s_Rg=="
so.set_cookies(cookies.split(';'))
page=SessionPage(session_or_options=so)

url='https://weibo.com/ajax/statuses/mymblog?uid=7743317355&page=1'
headers={
    "referer":"https://weibo.com/u/3845052579",
    "x-xsrf-token":"HFVN75npxEc6HCEJfTLJ0CmJ",
    "x-requested-with":"XMLHttpRequest",
    "Accept":"application/json, text/plain, */*",
}
# res=page.get('https://weibo.com/u/7743317355',cookies=cookies)
page.get(url,headers=headers)
print(url.split('page=')[-1]=='1')
# print(page.json)
page_json=page.json
page_info=page_json['data']['list']
print(len(page_info))
print(page_json['data']['since_id'])
for i in page_info:
    created_at=i['created_at']
    dt = datetime.strptime(created_at, '%a %b %d %H:%M:%S %z %Y')
    created_at=dt.date()
    print(dt.date())
    # if 'page_info' in i:
    #     if 'media_info' in i['page_info']:
    #         media_url=i['page_info']['media_info']['playback_list'][0]['play_info']
    #         video_url=media_url['url']
    #         # print(video_url,'\n')
    #         # rename=f"{created_at}_{''.join(random.choices(characters, k=8))}"
    #         # page.download(video_url,goal_path='vedio',rename=rename)
    #     else:
    #         print(i['page_info'])
    #
    # else:
    #     if 'pic_infos' in i:
    #         pic_infos=i['pic_infos']
    #         print('存在图片，图片数量为',len(pic_infos))
    #         # for ii in pic_infos.values():
    #         #     print(ii['largest'])
    #         #     pic_url=ii['largest']['url']
    #         #     rename=f"{created_at}_{pic_url.split('/')[-1][14:24]}"
    #         #     page.download(pic_url,goal_path='pics',rename=rename)
    #     else:
    #         print("不存在pic_infos")
    #         print(i)
