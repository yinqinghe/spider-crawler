import requests
import time
from urllib.parse import urlencode
from multiprocessing import Pool
import json
import os

global i
global j
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
    print(url)
    response=requests.get(url,headers=headers,timeout=10)
    re=response.json()
    print(re)
    try:
        if response.status_code==200:
#              pprint.pprint(re)
             return re
    except requests.ConnectionError as e:
        print("error",e.args)
def Get_imge(re):
    i = 0
    j = 0
    picsurl = []
    items = re.get('data').get('cards')
    for item in items:
        j = j + 1
        try:
            pics = item.get('mblog').get('pics')
            page_info = item.get('mblog').get('page_info')
            ret=item.get('mblog').get('retweeted_status')
            times = item.get('mblog').get('created_at')
            source = item.get('mblog').get('source')
            text = item.get('mblog').get('text')
            message = []
            # message.append(Etime)
            message.append(source)
            message.append(text)
            if pics is not None:
                for p in pics:
                    v = p.get('large').get('url')
                    print(v)
                    i = i + 1
                    message.append(v)
                    picsurl.append(v)
                print(len(message) - 3)
            elif page_info is not None:                                          #视频链接处理
                i = i + 1
                vedio = page_info.get('urls').get('mp4_hd_mp4')
                message.append(vedio)
                picsurl.append(vedio)
                print(message)
            elif ret is not None:
                transmit = ret.get('pics')  # 转发微博处理
                for t in transmit:
                    i = i + 1
                    v0 = t.get('large').get('url')
                    message.append(v0)
                    picsurl.append(v0)
            else:
                continue
            # for jj in range(0, len(message)):  # 写入数组信息
            #     tem_sheet.write(j, jj, message[jj],style)
            # # data.save(savepath)#保存文件
            # tem_wb.save(savepath)
        except:
            continue
    if i!=0:
        print("单页多条微博发布图片的总个数", i)
        print("一页获取的数据项", j)
    return picsurl

if __name__ == '__main__':
#     try:
        uid=['3224882012']#
#         uid = ['1192515960']#李冰冰
        for j in uid:
            a=Get_page(198,j)
            # sin=a.get('data').get('cards')[1].get('mblog').get('user').get('screen_name')
            listUrl=Get_imge(a)
            # for i in range(200,3):
            #     o=Get_page(i,j)
            #     print('该页为：',i)
            #     a=Get_imge(o)
            #     DownLoadPics(a,sin)
#     except:pass


