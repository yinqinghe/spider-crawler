import os
import sys
import time
from math import ceil
import requests

"""
    单独获取cos区b站up的相簿
"""
print('请选择输入类型数字')
stat = input('1 名字  2 uid,请选择：')
file_name = 'bili'

# 1. 根据name获取uid
boo = True
if stat == '1':
    uname = input('请输入up全称：')
    while boo:
        search_url = f'https://api.bilibili.com/x/web-interface/search/all/v2?keyword={uname}'
        search_json = requests.get(url=search_url).json()
        search_results = search_json['data']['result']
        for r_num in range(len(search_results)):
            search_result = search_results[r_num]
            if search_result['result_type'] != 'bili_user':
                continue
            if len(search_result['data']) == 0:
                uname = input('用户名错误，请重新输入：')
                break
            r_data = search_result['data']
            for u_num in range(len(r_data)):
                if r_data[u_num]['uname'] == uname:
                    uid = r_data[u_num]['mid']
                    r_num = -1
                    boo = False
                    break
            if r_num == -1:
                break
else:
    uid = input('请输入up的uid：')
    info_url = f'https://api.bilibili.com/x/space/acc/info?mid={uid}'
    info_json = requests.get(url=info_url).json()
    uname = info_json['data']['name']
print(f'================== {uname} ==================')

# 2. 根据uid获取相簿投稿数量
nav_url = f'https://api.bilibili.com/x/space/navnum?mid={uid}'
nav_json = requests.get(nav_url).json()
album_count = nav_json['data']['album']
print(f'获取相簿数量：{album_count}')
if album_count == 0:
    print('该up没有图片，结束运行')
    sys.exit()
# 创建文件夹
if not os.path.exists(f'{file_name}/{uname}'):
    os.makedirs(f'{file_name}/{uname}')
# 3. 获取相簿列表
page_num = 0  # 页码
page_size = 30  # 条数
page_max = ceil(album_count / page_size)
for page_num in range(page_max):
    album_url = f'https://api.bilibili.com/x/dynamic/feed/draw/doc_list?uid={uid}&page_num={page_num}' \
                f'&page_size={page_size}&biz=all&jsonp=jsonp '
    album_json = requests.get(url=album_url).json()
    album_items = album_json['data']['items']
    print(f'第 {page_num + 1} 页')
    for item_num in range(len(album_items)):
        album_item = album_items[item_num]
        dyn_id = album_item['dyn_id']
        print(f'  {page_num + 1}-{item_num + 1}、动态：{dyn_id}')
        # 获取时间
        c_time = album_item['ctime']
        c_time = time.strftime('%Y%m%d%H%M%S', time.localtime(c_time))
        p_num = 1
        # 获取图片路径
        for img_num in range(len(album_item['pictures'])):
            # 4. 下载图片
            img_url = album_item['pictures'][img_num]['img_src']
            pic_data = requests.get(img_url).content
            with open(f'{file_name}/{uname}/{uname}_{c_time}_{p_num}.jpg', mode='wb') as f:
                f.write(pic_data)
                print(f'    正在下载：{img_url}.jpg')
            p_num += 1
        time.sleep(2)