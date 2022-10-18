import requests
import xlwt
from urllib.parse import urlencode
import os
import csv
import datetime,time
from time import mktime,strptime
from datetime import datetime
now=datetime.now()
nowtime=now.strftime('%Y-%m-%d %H:%M:%S')
Nowtime=now.strftime('%Y-%m-%d')
global i
global j
savepath='D:\图片\data.xls'
data=xlwt.Workbook(encoding='utf-8',style_compression=0)
sheet=data.add_sheet(Nowtime,cell_overwrite_ok=True)
col=('发布时间','来自','文案','图片链接')
for i in range(0,4):
    sheet.write(0,i,col[i])
# f = open("data.csv", mode="w", encoding="utf-8", newline='')
# writer = csv.writer(f)
style=xlwt.XFStyle()#设置样式
font=xlwt.Font()#字体基本设置
font.name='new'
font.height=20*10#字体大小
style.font=font#字体样式
sheet.col(2).width=3333
f1=open('D:\图片\log.txt',mode="a",encoding='utf-8')
def Get_page(page,uid):
    headers = {
        'Host': 'm.weibo.cn',
        'Referer': 'https://m.weibo.cn/u/1885611142?uid=1885611142&t=0&luicode=10000011&lfid=100103type%3D1%26q%3D%E5%AD%94%E9%9B%AA%E5%84%BF',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
        # 这个可以从你的浏览器里检查网页里面找 目的是模拟浏览器申请页面
    }
    params = {
        'uid': uid,
        't': 0,
        'luicode': 10000011,
        'lfid': 100103,
        'containerid': '107603' + str(uid),
        'page': page
    }
    url = 'https://m.weibo.cn/api/container/getIndex?' + urlencode(params)
    response = requests.get(url, headers=headers, timeout=10)
    re = response.json()
    # print(re)
    try:
        if response.status_code == 200:
            #              pprint.pprint(re)
            return re
    except requests.ConnectionError as e:
        print("error", e.args)
def Get_imge(re,iii,jjj):
    i = iii
    j = jjj
    picsurl = []
    items = re.get('data').get('cards')
    for item in items:
        j=j+1
        try:
            pics = item.get('mblog').get('pics')
            page_info=item.get('mblog').get('page_info')
            times=item.get('mblog').get('created_at')
            # Format="%a %b %d %H:%M:%S +0800 %Y"
            # Etime=datetime.strptime(times,Format)
            b = mktime(strptime(times, "%a %b %d %H:%M:%S +0800 %Y"))  # 将该时间格式转换成时间戳
            time1 = time.localtime(b)  # 将时间戳转换成一种特定的格式
            Etime=time.strftime('%Y-%m-%d %H:%M:%S', time1)
            print(Etime)
            source=item.get('mblog').get('source')
            text=item.get('mblog').get('text')
            message = []
            message.append(Etime)
            message.append(source)
            message.append(text)
            # writer.writerow(message)
            # print(pics)

            if pics is not None:
                for p in pics:
                    v = p.get('large').get('url')
                    print(v)
                    i=i+1
                    # message = []
                    # message.append(times)
                    # writer.writerow(message)
                    message.append(v)
                    # writer.writerow(message)
                    picsurl.append(v)
                print(len(message)-3)
            elif page_info is not None:
                    vedio = page_info.get('urls').get('mp4_hd_mp4')
                    message.append(vedio)
                    picsurl.append(vedio)
                    print(message)
            else:
                transmit=item.get('mblog').get('retweeted_status').get('pics')#转发微博处理
                for t in transmit:
                    i = i + 1
                    v0=t.get('large').get('url')
                    message.append(v0)
                    picsurl.append(v0)

            for jj in range(0,len(message)):#写入数组信息
                sheet.write(j,jj,message[jj])
            data.save(savepath)#保存文件
        except:
            continue
    print("单页多条微博发布图片的总个数",i)
    print("一页获取的数据项",j)
    f1.write(f"{nowtime}  单页多条微博发布图片的总个数:{i}\n")#记录运行日志
    return picsurl,i,j

def DownLoadPics(picsurl, sin_id):
    headers = {
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
        'referer': 'https://m.weibo.cn',
    }
    wen = "D:/图片/" + sin_id
    if not os.path.exists(wen):
        os.makedirs(wen)
    for i in picsurl:
        qr = requests.get(i, headers=headers)
        print(qr)
        path = wen + '/' + sin_id + i.split('/')[-1]
        print(path)
        with open(path, 'wb') as f:
            f.write(qr.content)
            print('-' * 10)
if __name__ == '__main__':
    #     try:
    sum_i=0
    sum_j=0
    uid = ['3224882012']
    for j in uid:
        a = Get_page(1, j)
        sin = a.get('data').get('cards')[1].get('mblog').get('user').get('screen_name')
        # listUrl,sum_i,sum_j=Get_imge(a,ii,jj)
        # print(listUrl)
        # print(sum_i)
        # for i in range(1, 2):
        #     f1.write(f"{nowtime}    正在加载的页数：{i}\n")
        #     o = Get_page(i, j)
        #     listUrl,tem_i,tem_j= Get_imge(o,sum_i,sum_j)
        #     sum_i=tem_i
        #     sum_j=tem_j
            # DownLoadPics(a, sin)
    print(sum_i)
    print(sum_j)