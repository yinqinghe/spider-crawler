import pymysql

sql_add="insert into 有你更幸福(link,time,title,aid,update_time,nowtime)" \
        " values (%s,%s,%s,%s,%s,%s)"

def SQL_opration(arr):
        # 创建连接
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', database='wechat',
                               charset='utf8mb4')
        # 创建游标
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        ii=0
        for i in arr:
                # print(i[3])
                # if i[3]=='2247483784_1':
                #         ii=1
                #         break
                cursor.execute(sql_add,i)

        #提交  不然无法保存
        conn.commit()
        #关闭游标
        cursor.close()
        #关闭连接
        conn.close()
        if ii==1:
                return 10