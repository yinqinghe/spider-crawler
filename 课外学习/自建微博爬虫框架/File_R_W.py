import xlwt
import xlrd
from xlutils.copy import copy

savepath = 'D:\Pics\Data_22.xls'
tem_ff=open("D:\Pics\Status_record.txt",mode='r',encoding='utf-8')           #状态记录   独立于程序  一个数据记录文件存储
tem=tem_ff.read()
tem_ff.close()
tem_f=open("D:\Pics\Status_record.txt",mode='w+',encoding='utf-8')
tem_f.write(str(int(tem)+1))
tem_f.close()

tem_data = xlrd.open_workbook(savepath, formatting_info=True)         #将之前的文件.xls拷贝到新的文件里
tem_wb = copy(wb=tem_data)
print(tem+"--------------------------")
tem_sheet=tem_wb.add_sheet(tem)                                      #在拷贝之后文件的基础之上添加一个sheet

style = xlwt.XFStyle()                                                # 设置样式
font = xlwt.Font()                                                    # 字体基本设置                               # 字体大小
style.font = font                                                     # 字体样式
tem_sheet.col(0).width = 256*19                                       #修改单元格的宽度
tem_sheet.col(1).width = 256*15
tem_sheet.col(2).width = 256*35
tem_sheet.col(3).width = 256*35
tem_sheet.col(4).width = 256*21
tem_sheet.col(5).width = 256*17
tem_sheet.col(6).width = 256*16