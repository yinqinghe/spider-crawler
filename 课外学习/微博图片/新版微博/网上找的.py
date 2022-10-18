import os
import sys
import time
from urllib.parse import quote

import requests

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
}


def time_to_str(c_at):
    ti = time.strptime(c_at, '%a %b %d %H:%M:%S +0800 %Y')
    time_str = time.strftime('%Y%m%d%H%M%S', ti)
    return time_str


# 1. 搜索用户，获取uid
# 2. 通过uid获取空间动态关键参数
# 3. 获取动态内容
# 4. 提取图片参数
# 5. 下载图片

# 1. 搜索用户，获取uid
# ========= 用户名 =========
# 输入不同的用户名可切换下载的用户图片
# 用户名需要完全匹配
name = '半半子_'
# =========================

con_id = f'100103type=1&q={name}'
# 这个条件需要转码
con_id = quote(con_id, 'utf-8')
user_url = f'https://m.weibo.cn/api/container/getIndex?containerid={con_id}&page_type=searchall'
user_json = requests.get(url=user_url, headers=headers).json()
user_cards = user_json['data']['cards']
for card_num in range(len(user_cards)):
    if 'mblog' in user_cards[card_num]:
        if user_cards[card_num]['mblog']['user']['screen_name'] == name:
            print(f'正在获取{name}的空间')
            # 2. 通过uid获取空间动态关键参数
            user_id = user_cards[card_num]['mblog']['user']['id']
            info_url = f'https://m.weibo.cn/profile/info?uid={user_id}'
            info_json = requests.get(url=info_url, headers=headers).json()
            more_card = info_json['data']['more'].split("/")[-1]
            print(more_card)
            break
# file_name = 'weibo'
# if not os.path.exists(file_name):
#     os.mkdir(file_name)
#
# if len(more_card) == 0:
#     sys.exit()
# page_type = '03'
# page = 0
# while True:
#     # 3. 获取动态内容
#     page += 1
#     url = f'https://m.weibo.cn/api/container/getIndex?containerid={more_card}&page_type={page_type}&page={page}'
#     param = requests.get(url=url, headers=headers).json()
#     cards = param['data']['cards']
#     print(f'第 {page} 页')
#     for i in range(len(cards)):
#         card = cards[i]
#         if card['card_type'] != 9:
#             continue
#         mb_log = card['mblog']
#         # 4. 提取图片参数
#         # 获取本人的图片
#         pic_ids = mb_log['pic_ids']
#         user_name = mb_log['user']['screen_name']
#         created_at = mb_log['created_at']
#         if len(pic_ids) == 0:
#             # 获取转发的图片
#             if 'retweeted_status' not in mb_log:
#                 continue
#             if 'pic_ids' not in mb_log['retweeted_status']:
#                 continue
#             pic_ids = mb_log['retweeted_status']['pic_ids']
#             user_name = mb_log['retweeted_status']['user']['screen_name']
#             created_at = mb_log['retweeted_status']['created_at']
#         time_name = time_to_str(created_at)
#         pic_num = 1
#         print(f'======== {user_name} ========')
#         # 5. 下载图片
#         for pic_id in pic_ids:
#             pic_url = f'https://wx2.sinaimg.cn/large/{pic_id}.jpg'
#             pic_data = requests.get(pic_url, headers)
#             # 文件名 用户名_日期(年月日时分秒)_编号.jpg
#             # 例:半半子__20220212120146_1.jpg
#             with open(f'{file_name}/{user_name}_{time_name}_{pic_num}.jpg', mode='wb') as f:
#                 f.write(pic_data.content)
#                 print(f'    正在下载：{pic_id}.jpg')
#             pic_num += 1
#         time.sleep(2)