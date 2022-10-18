import pymysql
#创建连接
conn=pymysql.connect(host='127.0.0.1',port=3306,user='root',password='123456',database='data',charset='utf8')
#创建游标
cursor=conn.cursor(pymysql.cursors.DictCursor)
# sql_create_table="create table message(datatime varchar(15)null ,Froms varchar(20)null ,text varchar(50)null ,Pic_link varchar(50)NULL )"
def create_database():
    #创建数据库
    db_name=input("请输入要创建的数据库库名：")
    sql_create_database=f"create database {db_name}"
    cursor.execute(sql_create_database)

def create_table():
    #创建一个新表
    table_name=input("请输入要创建的表名：")
    field=input("所创建表里字段：")
    sql_create_table=f"create table {table_name}({field})"
    cursor.execute(sql_create_table)

sql_create_table="create table score(排名 varchar(5)null,学号 varchar(10)null ,姓名 varchar(6)null ,数字图像处理 tinyint null,计算机科学工程认知实习2 tinyint null,HTML5开发技术实践 tinyint null," \
                 "WEB前端技术基础 tinyint null,现代软件工程及统一建模语言学分_4 tinyint null,小型MIS应用系统设计学分_1 tinyint null,计算机图形学 tinyint null,数据库原理及应用 tinyint null," \
                 "操作系统 tinyint null,总学分 tinyint null,总成绩 tinyint null,平均成绩 float(3,3) null,总学分绩点 float(3,3) null,平均学分绩点 float(3,3) null)"
cursor.execute(sql_create_table)

#提交  不然无法保存
conn.commit()

#关闭游标
cursor.close()
#关闭连接
conn.close()