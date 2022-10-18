import time

from tmt_SDK import tmt_SOK
import pymysql

#创建连接
conn=pymysql.connect(host='127.0.0.1',port=3306,user='root',password='123456',database='sun',charset='utf8')
#创建游标
cursor=conn.cursor(pymysql.cursors.DictCursor)

for i in range(65, 200):  # 176    100
    num = i * 10

    sql_query_id = f"select title from nanico where id between {1+num} and {10+num}"
    cursor.execute(sql_query_id)
    result = cursor.fetchall()  # 接收查询到的结果
    print(result)

    ii=0

    for r in result:
        ii=ii+1
        time.sleep(0.2)
        zh=tmt_SOK(r['title'])
        print(zh)
        j = num + ii
        sql_add = f"update nanico set CN_title='{zh}' where id={j}"

        cursor.execute(sql_add)

    # 提交  不然无法保存
    conn.commit()

#提交  不然无法保存
conn.commit()

#关闭游标
cursor.close()
#关闭连接
conn.close()