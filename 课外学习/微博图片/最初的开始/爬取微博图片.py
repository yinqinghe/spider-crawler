
import pprint
import requests
import time
from urllib.parse import urlencode
from multiprocessing import Pool
import json

import os
def Get_page(page,uid):
# https://m.weibo.cn/api/container/getIndex?uid=1885611142&t=0
#&luicode=10000011&lfid=100103&type=uid&value=1885611142&containerid=1076031885611142
#这个是我取到的链接 我们可以一个个分析 发现最重要的是 uid containerid 和 page
    headers = {
    'Host':'m.weibo.cn',
    'Referer':'https://m.weibo.cn/u/1885611142?uid=1885611142&t=0&luicode=10000011&lfid=100103type%3D1%26q%3D%E5%AD%94%E9%9B%AA%E5%84%BF',
    'X-Requested-With':'XMLHttpRequest',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
#这个可以从你的浏览器里检查网页里面找 目的是模拟浏览器申请页面
       }
#https://m.weibo.cn/p/second?containerid=1078037030188037_-_photoall&page=1&count=24&title=%E5%9B%BE%E7%89%87%E5%A2%99&luicode=10000011&lfid=1078037030188037
#https://m.weibo.cn/u/7030188037?uid=7030188037&t=0&luicode=10000011&lfid=100103type%3D1%26q%3D%E7%BB%99%E6%88%91%E5%96%9D%E5%8F%A3%E4%BC%8F%E7%89%B9%E5%8A%A0
    params={
        'uid':uid,
        't':0,
        'luicode':10000011,
        'lfid':100103,
        'containerid':'107603'+str(uid),
        'page':page
    }
    url='https://m.weibo.cn/api/container/getIndex?' +urlencode(params)
    response=requests.get(url,headers=headers,timeout=10)
    re=response.json()
    try:
        if response.status_code==200:
#              pprint.pprint(re)
             return re
    except requests.ConnectionError as e:
        print("error",e.args)
def Get_imge(re):
    picsurl = []
    items = re.get('data').get('cards')
    for item in items:#一次请求获取的十条数据信息
        try:
            pics = item.get('mblog').get('pics')#要想分开存储，从这处理
            if pics is not None:
                for p in pics:
                    v = p.get('large').get('url')
                    print(v)
                    picsurl.append(v)
        except:
            continue
    return picsurl
def DownLoadPics(picsurl,sin_id):
        headers = {
                      'X-Requested-With':'XMLHttpRequest',
                      'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
                      'referer': 'https://m.weibo.cn',
         }
        wen="D:/图片/"+sin_id
        if not os.path.exists(wen):#如果不存在该路径，则创建一个
            os.makedirs(wen)
        for i in picsurl:
            qr=requests.get(i,headers=headers)
            print(qr)
            path=wen+'/'+sin_id+i.split('/')[-1]
            print(path)
            with open(path, 'wb')as f:
                f.write(qr.content)
                print('-' * 10)

if __name__ == '__main__':
#     try:
        uid=['3224882012']
        for j in uid:
            a=Get_page(1,j)
            sin=a.get('data').get('cards')[1].get('mblog').get('user').get('screen_name')
            for i in range(1,100):
                o=Get_page(i,j)
                a=Get_imge(o)
                DownLoadPics(a,sin)
#     except:pass


