import time

from Get_pages import Get_page
from Get_images import Get_imge
from datetime import datetime

year = ['2022', '2021']
month = ['12', '11', '10', '09', '08', '07', '06', '05', '04', '03', '02', '01']
uid = ['5901859174']
for y in year:
    for m in month:
        s_date = y + m
        # time.sleep(6)
        for j in uid:
            for p in range(1, 30):
                time.sleep(3)
                Get_page(p, j, y, m, s_date)

# for i in range(0, 7):
#     tem_sheet.write(0, i, col[i])
# a = Get_page(1, uid[0], 2022, '02',202202 )
# lists = a.get('data').get('list')
# if len(lists) == 0:  # 判断该页是否存在
#     print('不存在')
#     # break
# else:
#     print('存在')
# async def All():
#     tasks=[]
#     for y in year:
#         for m in month:
#             s_date = y + m
#             # time.sleep(6)
#             for j in uid:
#                 for p in range(1, 30):
#                     time.sleep(3)
#                     tasks.append(asyncio.create_task(Get_page(p, j, y, m, s_date)))
#                     # a = Get_page(p, j, y, m, s_date)
#     await asyncio.wait(tasks)
#
# if __name__ == '__main__':
#     asyncio.run(All())