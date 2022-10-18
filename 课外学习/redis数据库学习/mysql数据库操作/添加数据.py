import pymysql
import json
import requests
from bs4 import BeautifulSoup
import re

video_url="https://www.bilibili.com/video/av28989880"
cid_regex=re.compile(r'.*?cid(\d*?)\&amp.*',re.S)

resp=requests.get(video_url).text
bs=BeautifulSoup(resp,'lxml')
script=bs.find_all("script")[4]
script_text=script.text
script_pro1=script_text.split("__=")[1]
script_pro2=script_pro1.split(";(function()")[0]
dic_dic=json.loads(script_pro2)
#创建连接
conn=pymysql.connect(host='127.0.0.1',port=3306,user='root',password='123456',database='第二层',charset='utf8')
cursor=conn.cursor(pymysql.cursors.DictCursor)                      #创建游标

key=dic_dic
sql_add_field="insert into 第一层(字段,value) values (%s,%s)"

for i in key:
    value = key[i]
    if type(value)==dict:
        if len(value)==0:
            print("空字典")
        else:
            sql_table = f"create table {i}(字段 varchar(60)null,value varchar(255)null )"
            cursor.execute(sql_table)
            sql_add_field = f"insert into {i}(字段,value) values (%s,%s)"
            for j in value:
                next_value = value[j]
                if type(next_value)==dict:
                    if len(next_value)==0:
                        cursor.execute(sql_add_field, (j, "这是一个空字典"))
                    else:
                        cursor.execute(sql_add_field,(j,"is a dict"))
                elif type(next_value)==list:
                    cursor.execute(sql_add_field, (j,"is a list"))
                elif next_value==None:
                    cursor.execute(sql_add_field, (j,'None'))
                else:
                    cursor.execute(sql_add_field,(j,next_value))


# for i in key:
#         value=key[i]
#         # print(value)
#         try:
#             if type(value)==dict:
#                 if len(value)==0:
#                     cursor.execute(sql_add_field, (i, "这是一个空字典"))
#                 else:
#                     cursor.execute(sql_add_field,(i,"is a dict"))
#             elif type(value)==list:
#                 cursor.execute(sql_add_field, (i,"is a list"))
#             elif value==None:
#                 cursor.execute(sql_add_field, (i,'None'))
#             else:
#                 cursor.execute(sql_add_field,(i,value))
#         except pymysql.err.ProgrammingError:
#             print(value)

#提交  不然无法保存
conn.commit()

#关闭游标
cursor.close()
#关闭连接
conn.close()