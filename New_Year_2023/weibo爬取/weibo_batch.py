import time
from datetime import datetime, timedelta
import string
import random
from DrissionPage import WebPage,SessionPage,SessionOptions
import requests
# 定义随机字符串的可选字符集
characters = string.ascii_letters + string.digits

so=SessionOptions()
cookies="XSRF-TOKEN=HFVN75npxEc6HCEJfTLJ0CmJ; SSOLoginState=1678761231; _s_tentry=www.weibo.com; Apache=5110636533571.143.1679715960822; SINAGLOBAL=5110636533571.143.1679715960822; ULV=1679715960907:1:1:1:5110636533571.143.1679715960822:; PC_TOKEN=fd36359aff; login_sid_t=cb49de5de0559fa8c4435283aaa32a18; cross_origin_proto=SSL; WBStorage=4d96c54e|undefined; UOR=,,login.sina.com.cn; wb_view_log=1536*8641.25; SCF=AspUIZKFp_dZvFulvONf1yrz8X5_NrEbOusV9VJkBZ8XP6grp0cqQX7KkNERjbNTMskcoEZxolMuzW80IMbq_ok.; SUB=_2A25JrUtHDeRhGeFJ7VsQ-C7OzDyIHXVq2zuPrDV8PUNbmtAGLXLBkW9Nf1XN0Em-T-T7w37XogM_vP0wPAEMtg2a; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFnu--_lOqChWhFuKYAayRj5JpX5KzhUgL.FoMNSo.p1h5ES052dJLoI7DSIg_LIJvE9s8V; ALF=1720348311; WBPSESS=DQswqYJs0y3GED0LZ7HfbXlMSOy27EoOdSL0frr8krMDkrdzNSeQkW16Tf49dOOrB8eo5xG1501yGEXfxHa1dhNYLxtnsqddraw40GVO4zdwZdx_BAlJ2wc0j2Tu4gjY0LrQmxhd2UtYbbXT6w1xIg=="
so.set_cookies(cookies.split(';'))
page=SessionPage(session_or_options=so)

users="是那只壶啊_all"
def download(url,headers,last_time):
    page.get(url, headers=headers)

    page_json = page.json
    if url.split('page=')[-1]=='1':
        with open(f'{users}/last_posttime.txt',mode='a+') as f:
            d=page_json['data']['list'][1]['created_at']
            dt = datetime.strptime(d, '%a %b %d %H:%M:%S %z %Y')
            f.write('last_posttime:'+str(dt.date())+'\n')
        # return 1
    page_info = page_json['data']['list']
    print(len(page_info))
    page.download_set.if_file_exists.skip()  # 遇到同名文件跳过
    if len(page_info)==0:
        return 1
    for i in page_info:
        created_at = i['created_at']
        dt = datetime.strptime(created_at, '%a %b %d %H:%M:%S %z %Y')
        created_at = dt.date()
        print(dt.date())
        print(dt.date(),last_time)
        if dt.date() < last_time:
            return 1
        if 'page_info' in i:
            if 'media_info' in i['page_info']:
                media_url = i['page_info']['media_info']['playback_list'][0]['play_info']
                video_url = media_url['url']
                # print(video_url,'\n')
                rename = f"{created_at}_{video_url.split('/')[-1][14:24]}"
                page.download.add(video_url, goal_path=rf'{users}\vedio', rename=rename)
            else:
                print(i['page_info'])

        else:
            if 'pic_infos' in i:
                pic_infos = i['pic_infos']
                print(len(pic_infos))
                for ii in pic_infos.values():
                    print(ii['largest'])
                    pic_url=ii['largest']['url']
                    rename=f"{created_at}_{pic_url.split('/')[-1][14:24]}"
                    page.download.add(pic_url,goal_path=f'{users}\pics',rename=rename)
                    if 'video' in ii:
                        print(ii['video'])
                        gif_url=ii['video']
                        rename=f"{created_at}_{gif_url.split('/')[-1][65:85]}"
                        res = requests.get(gif_url)
                        print(res)
                        with open(rf'{users}\pics\{rename}', "wb") as f:
                            f.write(res.content)
                        # page.download.add(gif_url,goal_path=f'{users}\pics',rename=rename)
                    
                    
            else:
                print("不存在pic_infos")
if __name__ == '__main__':
    uid = input("请输入用户的UID： ")

    headers = {
        "referer": f"https://weibo.com/u/{uid}",
        "x-xsrf-token": "HFVN75npxEc6HCEJfTLJ0CmJ",
        "x-requested-with": "XMLHttpRequest",
        "Accept": "application/json, text/plain, */*",
    }
    with open(f'{users}/last_posttime.txt', 'r') as f:
        lines = f.readlines()
        last_line = lines[-1].split(':')[-1].strip('\n')
    date_obj = datetime.strptime(last_line, '%Y-%m-%d')

    # 将日期减去两天
    new_date_obj = date_obj - timedelta(days=2)
    last_time=new_date_obj.date()
    print(new_date_obj.date())
    start=time.time()
    num=1
    while num!=30:
        #https://weibo.com/u/3845052579
        #https://weibo.com/u/7743317355
        print('循环次数： ',num)
        url = f'https://weibo.com/ajax/statuses/mymblog?uid={uid}&page={num}'
        num+=1
        result=download(url,headers,last_time)
        if result:
            break
    end=time.time()
    print("消耗的时间为 ：",end-start)