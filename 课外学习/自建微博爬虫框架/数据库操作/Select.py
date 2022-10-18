import pymysql
#创建连接
conn=pymysql.connect(host='127.0.0.1',port=3306,user='root',password='123456',database='data',charset='utf8')
#创建游标
cursor=conn.cursor(pymysql.cursors.DictCursor)
# sql_create="create table message(datatime varchar(15)null ,Froms varchar(20)null ,text varchar(50)null ,Pic_link varchar(50)NULL )"
sql_query="select * from message where datatime='2021-10-08 08:40:57'"
sql_query_id="select * from message where id=8"


cursor.execute(sql_query_id)
result=cursor.fetchall()                 #接收查询到的结果

dict_s=result[0]
message=[]
for i in dict_s.values():       #字典转换成列表
    message.append(i)
for m in range(3,len(message)):
    if len(message[m])==0:
        break
    print(message[m])


#提交  不然无法保存
conn.commit()

#关闭游标
cursor.close()
#关闭连接
conn.close()