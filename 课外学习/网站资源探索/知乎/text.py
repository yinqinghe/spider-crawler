f1 = open('D:\Pics\sunyunzhu.txt', mode="r", encoding='utf-8')
import re
contents=f1.readlines()
print(len(contents))
t='히나 레이스 원피스 *초커세트*'
title = re.sub('[*]','',t)
print(title)