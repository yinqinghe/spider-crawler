import os
import requests
import time

# 使用多线程或多进程，协程减少下载的时间
log = open('D:\Pics\log.txt', mode="a", encoding='utf-8')
f1 = open('D:\Pics\sunyunzhu.txt', mode="r", encoding='utf-8')
t1 = time.time()
contents=f1.readlines()

def DownLoadPics(picsurl, sin_id):
    headers = {
        # 'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
        # 'referer': 'https://m.weibo.cn',
    }
    wen = "D:/Pics/" + sin_id
    if not os.path.exists(wen):
        os.makedirs(wen)
    ii=0
    for i in picsurl:
        qr = requests.get(i, headers=headers)
        print(qr)
        print(ii)
        ii=ii+1
        name = i.split('\n')[0]
        name=name.split('?')[0]
        # path = wen + '/' + sin_id + name.split('/')[-1]
        path = wen + '/' + sin_id +str(ii)+name.split('_r')[-1]
        print(i)
        with open(path, 'wb') as f:
            f.write(qr.content)
            print('-' * 10)

DownLoadPics(contents,'孙允珠01')
t2 = time.time()
log.write(f"本次运行消耗的时间为:{t2 - t1} \n")
log.close()
f1.close()
print("程序运行消耗时间为:", t2 - t1)
