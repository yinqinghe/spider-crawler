import json
import requests
from bs4 import BeautifulSoup
import re

video_url="https://www.bilibili.com/video/av28989880"
cid_regex=re.compile(r'.*?cid(\d*?)\&amp.*',re.S)
def get_cid():
    resp=requests.get(video_url).text
    bs=BeautifulSoup(resp,'lxml')
    # print(bs)
    script=bs.find_all("script")[4]
    script_text=script.text
    script_pro1=script_text.split("__=")[1]
    script_pro2=script_pro1.split(";(function()")[0]

    dic_dic=json.loads(script_pro2)
    # print(dic_dic,type(dic_dic))
    key=dic_dic
    print(key)
    cid=dic_dic['videoData']['cid']
    print("获取到的cid:",cid)


get_cid()