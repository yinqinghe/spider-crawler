import time
from File_R_W import tem_sheet
from Get_pages import Get_page
from Get_images import Get_imge
from datetime import datetime
url = open("D:\Pics\家居美图.txt", mode='w', encoding='utf-8')
now = datetime.now()
nowtime = now.strftime('%Y-%m-%d %H:%M:%S')
Nowtime = now.strftime('%Y-%m-%d')

sum_i = 0
sum_j = 0
year = ['2022', '2021']
month = ['12', '11', '10', '09', '08', '07', '06', '05', '04', '03', '02', '01']
uid = ['2998156335']

a = Get_page(1, uid[0], 2022, 1, 202201)
lists = a.get('data').get('list')
sin = a.get('data').get('list')[0].get('user').get('screen_name')
print(sin)
col = ('发布时间', '来自', '文案', '图片链接', nowtime, f'用户名：{sin}', f'uid:{uid[0]}')
for i in range(0, 7):
    tem_sheet.write(0, i, col[i])

for y in year:
    for m in month:
        s_date = y + m
        for j in uid:
            for p in range(1, 30):
                a = Get_page(p, j, y, m, s_date)
                statue=a.get('ok')
                while(statue==-100):
                    a= Get_page(p, j, y, m, s_date)
                    statue = a.get('ok')
                else:
                    lists = a.get('data').get('list')
                    if len(lists) == 0:  # 判断该页是否存在
                        print('不存在')
                        break
                    else:
                        print('存在')
                        listUrl, tem_i, tem_j = Get_imge(a, sum_i, sum_j)
                    #     # f1.write(f"一页获取的数据项 :{tem_j} \n")
                        sum_i = tem_i
                        sum_j = tem_j
                        for i in listUrl:#把文件链接保存到txt
                            url.write(i)
                            url.write('\n')
                    #     # f1.write(f"{nowtime}    正在加载的页数：{i}\n")
url.close()