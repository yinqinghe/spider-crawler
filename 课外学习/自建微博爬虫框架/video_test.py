import requests
import os

def DownLoadPics(picsurl, sin_id):
    headers = {
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
        'referer': 'https://m.weibo.cn',
    }
    wen = "D:/Pics/" + sin_id
    if not os.path.exists(wen):
        os.makedirs(wen)
    for i in picsurl:
        qr = requests.get(i, headers=headers)
        print(qr)
        name = i.split('\n')[0]
        name=name.split('?')[0]
        path = wen + '/' + sin_id + name.split('/')[-1]
        print(path)
        with open(path, 'wb') as f:
            f.write(qr.content)
            print('-' * 10)

url=['https://f.us.sinaimg.cn/000xecRhlx07tUPBK2bu010412000WPv0E010.mp4?label=mp4_hd&template=480x480.28.0&ori=0&ps=1CwnkDw1GXwCQx&Expires=1647855776&ssig=M8OKgSn4T2&KID=unistore,video']
DownLoadPics(url,'001')