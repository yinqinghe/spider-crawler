import matplotlib.pyplot as plt
import pandas as pd
import xlrd

data=pd.read_excel("D:\Pics\抖音采集工具x64\视频列表0301-1734.xlsx")

# data_column=data["点赞数"]
data_column=data.iloc[:,5:8]
# print(data_column.head(11))
data_column.loc[:,"分享数"]=data_column.loc[:,"评论数"]+data_column.loc[:,"点赞数"]
print(data_column.head(11))
# data_column.shape()
# data_column.describe()
plt.figure(figsize=(6,4))
plt.rcParams['font.sans-serif']=['SimHei']           #plt画图是找不到字体  需要添加两行代码  来解决font.set_text
plt.rcParams['axes.unicode_minus']=False
# plt.xlim(0,)
plt.scatter(data_column["点赞数"],data_column["评论数"],marker='*')
plt.title('简单来一下',fontsize=14)
plt.xlabel("点赞数")
plt.ylabel("评论数")
plt.legend("ID")
plt.show()