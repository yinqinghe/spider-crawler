import requests
import xlwt
from urllib.parse import urlencode
import os
import xlrd
from xlutils.copy import copy
import csv
import datetime, time
from time import mktime, strptime
from datetime import datetime
t1 = time.time()
now = datetime.now()
nowtime = now.strftime('%Y-%m-%d %H:%M:%S')
Nowtime = now.strftime('%Y-%m-%d')
global i
global j
savepath = 'D:\Pics\data.xls'
f1 = open('D:\Pics\log.txt', mode="a", encoding='utf-8')                #运行日志记录
# data = xlwt.Workbook(encoding='utf-8', style_compression=0)
# sheet = data.add_sheet('data', cell_overwrite_ok=True)

tem_ff=open("D:\Pics\Status_record.txt",mode='r',encoding='utf-8')     #状态记录   独立于程序  一个数据记录文件存储
tem=tem_ff.read()
tem_ff.close()
tem_f=open("D:\Pics\Status_record.txt",mode='w+',encoding='utf-8')
tem_f.write(str(int(tem)+1))
tem_f.close()

tem_data = xlrd.open_workbook(savepath, formatting_info=True)         #将之前的文件.xls拷贝到新的文件里
tem_wb = copy(wb=tem_data)
print(tem+"--------------------------")
tem_sheet=tem_wb.add_sheet(tem)                                      #在拷贝之后文件的基础之上添加一个sheet

style = xlwt.XFStyle()                                                # 设置样式
font = xlwt.Font()                                                    # 字体基本设置
# font.name = 'new'
# font.height = 20 * 10                                               # 字体大小
style.font = font                                                     # 字体样式
tem_sheet.col(0).width = 256*19                                       #修改单元格的宽度
tem_sheet.col(1).width = 256*15
tem_sheet.col(2).width = 256*35
tem_sheet.col(3).width = 256*35
tem_sheet.col(4).width = 256*21
tem_sheet.col(5).width = 256*17
tem_sheet.col(6).width = 256*16

def Get_page(page, uid):
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
    response = requests.get(url, headers=headers, timeout=(10,250))
    re = response.json()
    # print(re)
    try:
        if response.status_code == 200:
            #              pprint.pprint(re)
            return re
    except requests.ConnectionError as e:
        print("error", e.args)
def Get_imge(re, iii, jjj):
    i = iii
    j = jjj
    picsurl = []
    items = re.get('data').get('cards')
    for item in items:
        j = j + 1
        try:
            pics = item.get('mblog').get('pics')
            page_info = item.get('mblog').get('page_info')
            ret=item.get('mblog').get('retweeted_status')      #转发微博处理
            times = item.get('mblog').get('created_at')
            b = mktime(strptime(times, "%a %b %d %H:%M:%S +0800 %Y"))  # 将该时间格式转换成时间戳
            time1 = time.localtime(b)  # 将时间戳转换成一种特定的格式
            Etime = time.strftime('%Y-%m-%d %H:%M:%S', time1)
            source = item.get('mblog').get('source')
            text = item.get('mblog').get('text')
            message = []
            message.append(Etime)
            message.append(source)
            message.append(text)
            print('前者',message)
            print(type(pics))
            if pics is not None:
                for p in pics:
                    v = p.get('large').get('url')
                    print(v)
                    i = i + 1
                    message.append(v)
                    picsurl.append(v)
            elif page_info is not None:                                          #视频链接处理
                i = i + 1
                vedio = page_info.get('urls').get('mp4_hd_mp4')
                message.append(vedio)
                picsurl.append(vedio)
            elif ret is not None:
                transmit = ret.get('pics')  # 转发微博   图片    处理
                if transmit is not None:
                    for t in transmit:
                        i = i + 1
                        v0 = t.get('large').get('url')
                        message.append(v0)
                        picsurl.append(v0)
                else:
                    i = i + 1
                    ret_page_info=ret.get('page_info').get('urls').get('mp4_720p_mp4')       # 转发微博   视频    处理
                    message.append(ret_page_info)
            else:
                i = i + 1
                message.append('链接消失的一页')
                # ret=message[2].split('<a')[0]                                #解决了只有前面的数据，获取到文案   后面无信息的数据
                # message[2]=ret
            print('后者',message)
            for jj in range(0, len(message)):  # 写入数组信息
                tem_sheet.write(j, jj, message[jj],style)

            tem_wb.save(savepath)
        except:
            continue
    print("单页多条微博发布图片的总个数", i)
    print("一页获取的数据项", j)
    f1.write(f"{nowtime}  单页多条微博发布图片的总个数:{i}\n")  # 记录运行日志
    return picsurl, i, j
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
    sum_i = 0
    sum_j = 0
    uid = ['5901859174']#林妙茜
    # uid = ['1192515960']#李冰冰
    a = Get_page(1, uid[0])
    sin = a.get('data').get('cards')[1].get('mblog').get('user').get('screen_name')
    followers_count = a.get('data').get('cards')[1].get('mblog').get('user').get('followers_count')
    follow_count = a.get('data').get('cards')[1].get('mblog').get('user').get('follow_count')
    col = ('发布时间', '来自', '文案', '图片链接', nowtime, f'用户名：{sin}', f'uid:{uid[0]}', f'该用户关注的账号数：{follow_count}',
           f'该用户的粉丝数：{followers_count}')
    for i in range(0, 9):
        tem_sheet.write(0, i, col[i])
    for j in uid:
        for i in range(1, 150):
            f1.write(f"{nowtime}    正在加载的页数：{i}\n")
            o = Get_page(i, j)
            listUrl, tem_i, tem_j = Get_imge(o, sum_i, sum_j)
            f1.write(f"一页获取的数据项 :{tem_j} \n")
            sum_i = tem_i
            sum_j = tem_j
            # DownLoadPics(a, sin)
    print(sum_i)
    print(sum_j)
    t2 = time.time()
    f1.write(f"本次运行消耗的时间为:{t2-t1} \n")
    f1.close()
    print("程序运行消耗时间为:", t2 - t1)
