from 下载数据 import downloadPage
from 保存到数据库 import SQL_opration
import random
import time
random.seed(time.time())
for i in range(70,80):  #496   105
    num=i*5
    # time.sleep(random.randint(3,10))     #第45项   第350项
    print(f"第{num}项")
    arry =downloadPage(num)
    SQL_opration(arry)
