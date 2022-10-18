import pymysql
import asyncio
from download import DownLoadPics
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', database='ins',
                       charset='utf8')
# 创建游标
cursor = conn.cursor(pymysql.cursors.DictCursor)
for i in range(10, 11):  # 176    100
    num = i * 10
    ind='link1'
    for i in range(2,31):
        index=f'link{i}'
        ind=('%s,%s'%(ind,index))
        # print(ind)

    print(ind)
    sql_query_id = f"select shortcode,{ind} from taaarannn where id between {1+num} and {10+num}"
    print(sql_query_id)
# sql_query_id = f"select link1 from nanicopics where id between 1+{num} and 10+{num}"
# print(sql_query_id)
    print(f"第{num}页")
    cursor.execute(sql_query_id)
    result = cursor.fetchall()  # 接收查询到的结果
    print(result)
    print(len(result))
    for rr in range(0,len(result)):
        print(result[rr]['shortcode'])
    #     asyncio.run(DownLoadPics(contents=result[rr]))
    #     print('finish')

        # # for r in range(1,61):
        #     link = result[rr][f'link{r}']
        #     print(link)
        #     if link==None:
        #         break

#提交  不然无法保存
conn.commit()

#关闭游标
cursor.close()
#关闭连接
conn.close()