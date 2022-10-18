import pymysql
from xlrd import open_workbook

workbook=open_workbook(r'D:\QQ\QQ下载文件\2021-2022-1\19级\专业\四专业.xls')
sheet_name=workbook.sheet_names()
# print(sheet_name)
sheet=workbook.sheet_by_index(0)
#创建连接
conn=pymysql.connect(host='127.0.0.1',port=3306,user='root',password='123456',database='data',charset='utf8')
#创建游标
cursor=conn.cursor(pymysql.cursors.DictCursor)
sql_add_Data_22="insert into message(datatime,Froms,text," \
        "Pic_link1,Pic_link2,Pic_link3,Pic_link4,Pic_link5,Pic_link6,Pic_link7,Pic_link8,Pic_link9," \
        "Pic_link10,Pic_link11,Pic_link12,Pic_link13,Pic_link14,Pic_link15,Pic_link16,Pic_link17,Pic_link18) values " \
        "(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
sql_add1="insert into message(datatime,Froms,text) values  (%s,%s,%s)"

sql_add_score="insert into score(排名 ,学号,姓名 ,数字图像处理,计算机科学工程认知实习2,HTML5开发技术实践," \
                 "WEB前端技术基础,现代软件工程及统一建模语言学分_4,小型MIS应用系统设计学分_1,计算机图形学,数据库原理及应用," \
                 "操作系统,总学分,总成绩,平均成绩,总学分绩点,平均学分绩点) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"


for i in range(9,sheet.nrows):
        content = sheet.row_values(i)
        cursor.execute(sql_add_score,content)

#提交  不然无法保存
conn.commit()

#关闭游标
cursor.close()
#关闭连接
conn.close()