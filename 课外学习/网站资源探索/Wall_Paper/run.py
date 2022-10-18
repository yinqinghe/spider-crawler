from concurrent.futures import ThreadPoolExecutor
#抓完everyone 的scene     剩下的不想抓了    收手了太难了
from main import main
import time
t1 = time.time()
with ThreadPoolExecutor(8) as t:
    for i in range(1,1670):
        t.submit(main,i)

t2 = time.time()
print("程序运行消耗时间为:", t2 - t1)