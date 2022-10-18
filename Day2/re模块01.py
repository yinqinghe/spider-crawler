import re

# re.findall()
# it=re.finditer()
# for i in it:
#     print(i.group())

obj1=re.compile(r'<a href="(?P<href>.*?)">下一页</a>',re.S)
obj2=re.compile(r'(?<=<a href=")(?![\w\W]*?<a href=")[\w\W]*',re.S)
#;<a href="/meinvtupian/xingganmeinv/241592_2.htm">下一页</a>
s='[<a href="/meinvtupian/xingganmeinv/243196_2.htm">2</a>, <a href="/meinvtupian/xingganmeinv/243196_3.htm">3</a>, <a href="/meinvtupian/xingganmeinv/243196_4.htm">4</a>, <a href="/meinvtupian/xingganmeinv/243196_5.htm">5</a>, <a href="/meinvtupian/xingganmeinv/243196_6.htm">6</a>, <a href="/meinvtupian/xingganmeinv/243196_2.htm">下一页</a>, <a href="/meinvtupian/xingganmeinv/243196_11.htm">尾页</a>]'
ss='<a href="/meinvtupian/xingganmeinv/241592.htm">首页</a>&nbsp;<a href="/meinvtupian/xingganmeinv/241592_7.htm">上一页</a>&nbsp;<a href="/meinvtupian/xingganmeinv/241592_6.htm">6</a>&nbsp;<a href="/meinvtupian/xingganmeinv/241592_7.htm">7</a>&nbsp;<b>8</b>&nbsp;<a href="/meinvtupian/xingganmeinv/241592_9.htm">9</a>&nbsp;<a href="/meinvtupian/xingganmeinv/241592_9.htm">尾页</a>'
sss='<a href="/meinvtupian/xingganmeinv/241591_2.htm">2</a>&nbsp;<a href="/meinvtupian/xingganmeinv/241591_3.htm">3</a>&nbsp;<a href="/meinvtupian/xingganmeinv/241591_4.htm">4</a>&nbsp;<a href="/meinvtupian/xingganmeinv/241591_5.htm">5</a>&nbsp;<a href="/meinvtupian/xingganmeinv/241591_6.htm">6</a>&nbsp;<a href="/meinvtupian/xingganmeinv/241591_2.htm">下一页</a>&nbsp;<a href="/meinvtupian/xingganmeinv/241591_11.htm">尾页</a>'
ssss=' <a href="/meinvtupian/xingganmeinv/241591.htm">首页</a>&nbsp;<a href="/meinvtupian/xingganmeinv/241591_2.htm">上一页</a>&nbsp;<a href="/meinvtupian/xingganmeinv/241591.htm">1</a>&nbsp;<a href="/meinvtupian/xingganmeinv/241591_2.htm">2</a>&nbsp;<b>3</b>&nbsp;<a href="/meinvtupian/xingganmeinv/241591_4.htm">4</a>&nbsp;<a href="/meinvtupian/xingganmeinv/241591_5.htm">5</a>&nbsp;<a href="/meinvtupian/xingganmeinv/241591_6.htm">6</a>&nbsp;<a href="/meinvtupian/xingganmeinv/241591_4.htm">下一页</a>&nbsp;<a href="/meinvtupian/xingganmeinv/241591_11.htm">尾页</a>'
web = obj1.search(ssss)
web1=obj2.search(web.group('href'))
# for i in web:
print(web.group())
print(web1.group())
# print(web1)