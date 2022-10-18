import time
import datetime
from time import mktime,strptime
from datetime import datetime

now=datetime.now()
a = "Sat Mar 28 22:24:24 2109"
c="Sat Feb 05 12:00:07 +0800 2022"
b = mktime(strptime(c, "%a %b %d %H:%M:%S +0800 %Y"))#将该时间格式转换成时间戳
time1=time.localtime(b)#将时间戳转换成一种特定的格式
Format="%a %b %d %H:%M:%S +0800 %Y"

tem_ff=open("D:\Pics\Status_record.txt",mode='r+',encoding='utf-8')
tem=tem_ff.read()
tem_ff.close()
tem_f=open("D:\Pics\Status_record.txt",mode='w+',encoding='utf-8')
# tem_int=int(tem)
# tem_wri=str(int(tem)+1)
# print(str(int(tem)+1))
tem_f.write(str(int(tem)+1))
tem_f.close()

message=["""谁说纹身的女孩就一定是坏女孩呢？ <a data-url="http://t.cn/A6qmwodt" href="http://t.cn/A6qmwodt" data-hide=""><span class='url-icon'><img style='width: 1rem;height: 1rem' src='https://h5.sinaimg.cn/upload/2015/09/25/3/timeline_card_small_web_default.png'></span><span class="surl-text">网页链接</span></a>  """,'666']
res=message[0].split('<a')[0]
print(res)
print(b)
print(now.strftime(('%Y-%m-%d %H:%M:%S')))
print(time1)
print(time.strftime('%Y-%m-%d %H:%M:%S',time1))#再将特定格式的时间转换 成自己想要的格式
print(datetime.strptime(c,Format))