from datetime import datetime
import random
import time
item=1639787513
time1 = time.localtime(time.time())
now=datetime.now()
t=time.strftime('%Y-%m-%d %H:%M:%S',time1 )
print(time.time())
print(t)
print(time1)
print(datetime.now())
random.seed(time.time())
# UA=open("D:\C#\python\爬虫\课外学习\Agent.txt",mode='r',encoding='utf-8')
# U_a=UA.readlines()[random.randint(0,9)]
# # print(len(U_a))
# print(U_a)
print(random.randint(0,9))

for i in range(0,9):
    print(i)