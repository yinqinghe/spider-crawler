import matplotlib.pyplot as plt
import pandas as pd
import xlrd

df=pd.read_excel("D:\Pics\抖音采集工具x64\视频列表0301-1734.xlsx")
df.head(10)
# fig=plt.figure()
#
# ax=fig.add_subpolt(1,1,1)

data=xlrd.open_workbook(filename=r"D:\Pics\抖音采集工具x64\视频列表0301-1734.xlsx")
# table=data.sheets()[8]
table=data.sheet_by_name('作者作品')
names=data.sheet_names()
print(names)
print(table)
print("xlsx行数：",table.nrows)
# print(data.sheet_loaded('61'))
# print(table.row_len(2))
# print(table.row(3))
# print(table.row_types(3,start_colx=0,end_colx=None))
# print(table.row_values(3,start_colx=0,end_colx=None))

# print(table.ncols)
# print(table.col(1,start_rowx=0,end_rowx=15))
# print(table.col_values(1,start_rowx=0,end_rowx=15))
# print(table.col_types(1,start_rowx=0,end_rowx=15))

# print(table.cell(1,6))
# print(table.cell_value(1,6))
# print(table.col_types(1,6))
# ax.hist(df['点赞数'],bins=7)
# # labels and Tit
# plt.title('大小比较')
# plt.xlabel('time')
# plt.ylabel('点赞数')
# plt.show()