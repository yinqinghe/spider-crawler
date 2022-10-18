import requests
import xlwt
from urllib.parse import urlencode
import os
import xlrd
from xlutils.copy import copy
import json
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
cookie=open("D:\C#\python\爬虫\课外学习\cookie.txt",mode='r',encoding='utf-8')
f1 = open('D:\Pics\log.txt', mode="a", encoding='utf-8')                #运行日志记录

tem_ff=open("D:\Pics\Status_record.txt",mode='r',encoding='utf-8')           #状态记录   独立于程序  一个数据记录文件存储
tem=tem_ff.read()
tem_ff.close()

tem_f=open("D:\Pics\Status_record.txt",mode='w+',encoding='utf-8')
tem_f.write(str(int(tem)+1))
tem_f.close()

# tem_data = xlrd.open_workbook(savepath, formatting_info=True)         #将之前的文件.xls拷贝到新的文件里
# tem_wb = copy(wb=tem_data)
# print(tem+"--------------------------")
# tem_sheet=tem_wb.add_sheet(tem)                                      #在拷贝之后文件的基础之上添加一个sheet
#
# style = xlwt.XFStyle()                                                # 设置样式
# font = xlwt.Font()                                                    # 字体基本设置                                            # 字体大小
# style.font = font                                                     # 字体样式
# tem_sheet.col(0).width = 256*19                                       #修改单元格的宽度
# tem_sheet.col(1).width = 256*15
# tem_sheet.col(2).width = 256*35
# tem_sheet.col(3).width = 256*35
# tem_sheet.col(4).width = 256*21
# tem_sheet.col(5).width = 256*17
# tem_sheet.col(6).width = 256*16

def Get_page(page, uid,displayYear,curMonth,stat_date):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
        # 这个可以从你的浏览器里检查网页里面找 目的是模拟浏览器申请页面
        'accept': 'application/json,text/plain,*/*',
        'accept-encoding': 'gzip,deflate,br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'x-requested-with': 'XMLHttpRequest',
        'x-xsrf-token': 'cvk-RVYhyoTZvJpXapAAgQon',
        'referer': 'https://weibo.com/u/5901859174?lpage=profileRecom',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'cookie':f'{cookie.read()}',
        # 'cookie': 'SINAGLOBAL=35583908945.38466.1632662233304; XSRF-TOKEN=cvk-RVYhyoTZvJpXapAAgQon; SSOLoginState=1642034409; login_sid_t=95f3b9a1768ec4223239e6afdf96ca14; cross_origin_proto=SSL; _s_tentry=login.sina.com.cn; Apache=7587051160949.691.1642166916527; UOR=,,login.sina.com.cn; ULV=1642166916531:2:1:1:7587051160949.691.1642166916527:1632662233311; appkey=; TC-V-WEIBO-G0=b09171a17b2b5a470c42e2f713edace0; wb_view_log=1536*8641.25; SUB=_2A25PI3v2DeRhGeFN41sU9yjKyzuIHXVsWeo-rDV8PUNbmtANLWXakW9NQ6osNSgcGhIYbfxvS9etcnOlnJuC8buI; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFuaaOUryMCMwq33V2cq8pK5JpX5KzhUgL.FoM01h.fS0qcehM2dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMNe0n4SKMcSo5N; ALF=1678262054; WBPSESS=4ARBQ_XtZWWBs3-KYnu7gm4XOt6WLsK6JFPrdZ5S1AWknhzC8DsYuOZm4LaVZJu47zs0LRAq-rZcYE5Fti8Mf0PqcEmeHGRTGwZmXkxBeIafhWkF_rqx8_zTKTtwHkLPAfZ9uq_RpjVXp7x3tMgFqw=='
    }
    params = {
        'uid': uid,
        'page': page,
        'feature':'0',
        'displayYear': displayYear,
        'curMonth': curMonth ,
        'stat_date': stat_date,
    }
    #https://weibo.com/ajax/statuses/mymblog?uid=6448920093&page=1&feature=0
    url = 'https://weibo.com/ajax/statuses/mymblog?' + urlencode(params)
    print(url)
    response = requests.get(url,headers=headers)
    re=response.json()
    print(re)
    # time.sleep(5)
    try:
        if response.status_code == 200:
            return re
    except requests.ConnectionError as e:
        print("error", e.args)
def Get_imge(re, iii, jjj):
    i = iii
    j = jjj
    picsurl = []
    items = re.get('data').get('list')
    for item in items:
        j = j + 1
        try:
            pic_infos = item.get('pic_infos')
            page_info = item.get('page_info')
            ret=item.get('retweeted_status')      #转发微博处理
            times = item.get('created_at')
            b = mktime(strptime(times, "%a %b %d %H:%M:%S +0800 %Y"))  # 将该时间格式转换成时间戳
            time1 = time.localtime(b)  # 将时间戳转换成一种特定的格式
            Etime = time.strftime('%Y-%m-%d %H:%M:%S', time1)
            source = item.get('source')
            text = item.get('text_raw')
            message = []
            message.append(Etime)
            message.append(source)
            message.append(text)
            print('前者',message)

            if pic_infos is not None:
                for p in pic_infos.values():
                    v = p.get('largest').get('url')
                    print(v)
                    i = i + 1
                    message.append(v)
                    picsurl.append(v)
                # print(len(message) - 3)
            elif page_info is not None:                                          #视频链接处理
                i = i + 1
                vedio = page_info.get('media_info').get('mp4_hd_url')
                message.append(vedio)
                picsurl.append(vedio)
            elif ret is not None:
                transmit = ret.get('pic_infos')  # 转发微博   图片    处理
                media_info=ret.get('media_info')
                if transmit is not None:
                    for t in transmit.values():
                        i = i + 1
                        v0 = t.get('largest').get('url')
                        message.append(v0)
                        picsurl.append(v0)
                elif media_info is not None:
                    ret_page_info=media_info.get('mp4_hd_url')     # 转发微博   视频    处理
                    message.append(ret_page_info)
                else:
                    message.append("转发的一个空链接")
            else:
                message.append('链接消失的一页')
                ret=message[2].split('<a')[0]                                #解决了只有前面的数据，获取到文案   后面无信息的数据
                message[2]=ret
            print('后者', message)
            # for jj in range(0, len(message)):  # 写入数组信息
            #     tem_sheet.write(j, jj, message[jj],style)
            # tem_wb.save(savepath)
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
    year=['2022','2021']
    month=['01']
    # month=['12','11','10','09','08','07','06','05','04','03','02','01']
    uid = ['5901859174']
    a = Get_page(1, uid[0], 2022, 2, 202202)
    # lists = a.get('data').get('list')
    sin = a.get('data').get('list')[0].get('user').get('screen_name')
    print(sin)
    col = ('发布时间', '来自', '文案', '图片链接', nowtime, f'用户名：{sin}', f'uid:{uid[0]}')
    # listUrl, tem_i, tem_j = Get_imge(a, sum_i, sum_j)
    # for i in range(0, 7):
    #     tem_sheet.write(0, i, col[i])
    for y in year:
        for m in month:
            s_date=y+m
            for j in uid:
                for p in range(1,30):
                    time.sleep(20)
                    a = Get_page(p, j,y,m,s_date)
                    print(a)
                    lists=a.get('data').get('list')
                    if len(lists)==0:                                  #判断该页是否存在
                        print('不存在')
                        break
                    else:
                        print('存在')
                        listUrl, tem_i, tem_j = Get_imge(a, sum_i, sum_j)
                        f1.write(f"一页获取的数据项 :{tem_j} \n")
                        sum_i = tem_i
                        sum_j = tem_j
                        for i in range(1, 2):
                            f1.write(f"{nowtime}    正在加载的页数：{i}\n")

                            # DownLoadPics(a, sin)
    cookie.close()
    print(sum_i)
    print(sum_j)
    t2 = time.time()
    f1.write(f"本次运行消耗的时间为:{t2-t1} \n")
    f1.close()
    print("程序运行消耗时间为:", t2 - t1)
