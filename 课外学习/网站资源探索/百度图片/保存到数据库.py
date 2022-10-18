import pymysql

sql_add="insert into sunyunzhu(bdImgnewsDate,fromPageTitleEnc,hoverURL,pageNum,FromURL1,ObjURL1,FromURL2,ObjURL2,FromURL3,ObjURL3)" \
        " values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

def SQL_opration(arr):
        # 创建连接
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', database='baidupics',
                               charset='utf8mb4')
        # 创建游标
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        for i in arr:
                cursor.execute(sql_add,i)

        #提交  不然无法保存
        conn.commit()
        #关闭游标
        cursor.close()
        #关闭连接
        conn.close()