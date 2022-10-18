import pymysql
#创建连接
conn=pymysql.connect(host='127.0.0.1',port=3306,user='root',password='123456',database='wall_paper',charset='utf8')
#创建游标
cursor=conn.cursor(pymysql.cursors.DictCursor)
# sql_create="create table message(datatime varchar(15)null ,Froms varchar(20)null ,text varchar(50)null ,Pic_link varchar(50)NULL )"
# sql_query="select * from one where "
# sql_add="insert into message(datatime,Froms,text," \
#         "Pic_link1,Pic_link2,Pic_link3,Pic_link4,Pic_link5,Pic_link6,Pic_link7,Pic_link8,Pic_link9," \
#         "Pic_link10,Pic_link11,Pic_link12,Pic_link13,Pic_link14,Pic_link15,Pic_link16,Pic_link17,Pic_link18) values " \
#         "(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
# sql_add1="insert into message(datatime,Froms,text) values  (%s,%s,%s)"
#
#
# for i in range(0,sheet.nrows):
#         content = sheet.row_values(i)
#         cursor.execute(sql_add,content)
sql="alter table totaluniquesubscribers add id int auto_increment primary key "#增加一个自增字段   且这个键必须设为主键
cursor.execute(sql)

#提交  不然无法保存
conn.commit()

#关闭游标
cursor.close()
#关闭连接
conn.close()