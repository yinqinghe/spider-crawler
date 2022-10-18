from 下载数据 import downloadPage
from 保存到数据库 import SQL_opration
import random
import time
random.seed(time.time())
for i in range(0,20):  #
    num=i*5
    # time.sleep(random.randint(3,10))     #
    print(f"第{num}项")
    arry =downloadPage(num)
    print(len(arry))
    if len(arry)==0:
        break
    S=SQL_opration(arry)
    if S==10:
        break