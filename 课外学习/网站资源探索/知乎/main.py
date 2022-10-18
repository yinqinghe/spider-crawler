from Ajax_people import request
from 保存到数据库 import SQL_opration
from downloadpage import request_d

# for i in range(0,55):
#     num=0+i*60
#     print(i)
offset=60
limit=20
arry=request(offset,limit)
# print(arry)
# arry=request_d()
SQL_opration(arry)