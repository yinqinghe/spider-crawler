import json
import requests
from bs4 import BeautifulSoup
import redis
import re

video_url="https://www.bilibili.com/video/av28989880"
cid_regex=re.compile(r'.*?cid(\d*?)\&amp.*',re.S)
def get_cid():
    resp=requests.get(video_url).text
    bs=BeautifulSoup(resp,'lxml')
    # print(bs)
    script=bs.find_all("script")[4]
    # print(script.text)
    # print(type(script))
    script_text=script.text
    script_pro1=script_text.split("__=")[1]
    script_pro2=script_pro1.split(";(function()")[0]
    # print(script_pro2,type(script_pro2))

    dic_dic=json.loads(script_pro2)
    # print(dic_dic,type(dic_dic))

    key=dic_dic['videoData']['cid']
    # for i in key:
    #     value=key[i]
    #     print(i)
    #     print(type(value))
    #     if type(value) == dict:
    #         if len(value) == 0:
    #             print("空字典")
    #         else:
    #             print("字典")
    print(key)
    cid=dic_dic['videoData']['cid']
    print("获取到的cid:",cid)


get_cid()
# url="https://comment.bilibili.com/50280136.xml"
# res=requests.get(url)
# res.encoding='utf-8'
# bs=BeautifulSoup(res.text,'lxml')
# d_s=bs.find_all('d')
# count=1
# # print(res.text)
# pool=redis.ConnectionPool(host='127.0.0.1',port=6379,password='123456',db=0)
# dan_redis=redis.StrictRedis(connection_pool=pool)
# for d in d_s:
#     dan_redis.set(str(count),d.text)
#     count+=1
#     print(d.text)
# result_num=dan_redis.mget(dan_redis.keys())
# print("总共有%d条数据"%len(result_num))
