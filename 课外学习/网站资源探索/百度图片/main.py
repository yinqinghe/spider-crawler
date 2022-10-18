from 百度图片 import request
from 保存到数据库 import SQL_opration
from params import par

for i in range(0,55):
    num=0+i*60
    print(i)
    parm=par(num)
    arry=request(parm)
    # print(arry)
    SQL_opration(arry)