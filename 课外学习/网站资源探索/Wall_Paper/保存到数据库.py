import pymysql
sql_add1="insert into message(datatime,Froms,text) values  (%s,%s,%s)"

sql_add="insert into everyone(workshopItemTitle,workshop_author_name,data_publishedfileid,workshop_author_link,workshopItemPreviewImage,fileRating_num)" \
        " values (%s,%s,%s,%s,%s,%s)"

def SQL_opration(arr):
        # 创建连接
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', database='wall_paper',
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