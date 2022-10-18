import random

# tem_ff=open("D:\C#\python\爬虫\课外学习\cookie.txt",mode='r',encoding='utf-8')
# print(tem_ff.readlines()[random.randint(0,1)])
# print(random.randint(0,1))
# f1 = open('D:\Pics\links.txt', mode="r", encoding='utf-8')
# contents=f1.readlines()
# print(contents[115])


from xlrd import open_workbook

workbook=open_workbook(r'D:\Pics\Data_22.xls')
sheet_name=workbook.sheet_names()
print(sheet_name)
sheet=workbook.sheet_by_index(4)
# sheet1=workbook.sheet_by_name('265')
print(sheet.name,sheet.nrows,sheet.ncols)
content=sheet.row_values(1)
print(content)