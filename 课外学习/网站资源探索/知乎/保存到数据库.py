import pymysql

sql_add="insert into 浮力图片one(title,updated,link1,link2,link3,link4,link5,link6,link7,link8,link9,link10,link11,link12,link13,link14,link15,link16,link17,link18,link19,link20,link21,link22,link23,link24,link25,link26,link27,link28,link29,link30)" \
        " values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

def SQL_opration(arr):
        # 创建连接
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', database='zhihu',
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