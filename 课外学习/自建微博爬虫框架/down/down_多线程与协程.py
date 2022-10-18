import os
import requests
import time
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor#线程池，进程池
# 使用多线程或多进程，协程减少下载的时间
log = open('D:\Pics\log1.txt', mode="a", encoding='utf-8')
f1 = open('D:\Pics\links2.txt', mode="r", encoding='utf-8')
t1 = time.time()
headers = {
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    'referer': 'https://m.weibo.cn',
}
sin_id='thread01'
wen = "D:/Pics/" + sin_id
if not os.path.exists(wen):
    os.makedirs(wen)
contents=f1.readlines()

class count(object):
    def __init__(self,func):
        self.func=func
        self.count=0
    def __call__(self, *args, **kwargs):
        self.count+=1
        print(self.count)

def DownLoadPics(i):
    qr = requests.get(i, headers=headers)
    # print(qr)
    name = i.split('\n')[0]
    name=name.split('?')[0]
    path = wen + '/' + sin_id + name.split('/')[-1]
    with open(path, 'wb') as f:
        f.write(qr.content)
        print('-' * 10)
#第一次为5        消耗时间170s
#第二次为20       消耗时间53s    cpu占用50%左右   网络200M左右  任务下载2000项
with ThreadPoolExecutor(20) as t:
    for i in contents:
        t.submit(DownLoadPics,i)

t2 = time.time()
log.write(f"本次运行消耗的时间为:{t2 - t1} \n")
log.close()
f1.close()
print("程序运行消耗时间为:", t2 - t1)
