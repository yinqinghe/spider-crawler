import pymysql
#创建连接
conn=pymysql.connect(host='127.0.0.1',port=3306,user='root',password='123456',database='data',charset='utf8')
#创建游标
cursor=conn.cursor(pymysql.cursors.DictCursor)

sql_delete=f"delete from message where {}"

cursor.execute(sql_delete)

#提交  不然无法保存
conn.commit()

#关闭游标
cursor.close()
#关闭连接
conn.close()