import os
import requests
import time
import aiohttp
import asyncio
import aiofile

# 使用多线程或多进程，协程减少下载的时间
log = open('D:\Pics\log.txt', mode="a", encoding='utf-8')
f1 = open('D:\Pics\sunyunzhu.txt', mode="r", encoding='utf-8')
t1 = time.time()
contents=f1.readlines()
headers = {
    # 'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    # 'referer': 'https://m.weibo.cn',
}
sin_id='孙允珠01'
wen = "D:/Pics/" + sin_id
if not os.path.exists(wen):
    os.makedirs(wen)
async def request(i):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(i, headers=headers,timeout=250) as resp:
                name = i.split('\n')[0]
                name = name.split('?')[0]
                path = wen + '/' + sin_id + name.split('/')[-1]
                async with aiofile.async_open(path, mode='wb', ) as f:
                    await f.write(await resp.content.read())
                    print('-' * 10)
    except TimeoutError as e:
        print("-----socket timout:",i)
    except RuntimeError:
        print('Event loop is closed')
    except ConnectionResetError as e:
        print("远程主机强迫关闭了一个现有的连接",e)


async def DownLoadPics():
    tasks=[]
    for i in contents:
        tasks.append(asyncio.create_task(request(i)))
    await asyncio.wait(tasks)
if __name__ == '__main__':

    # loop=asyncio.get_event_loop()
    # loop.run_until_complete(DownLoadPics())
    asyncio.run(DownLoadPics())
    t2 = time.time()
    log.write(f"本次运行消耗的时间为:{t2 - t1} \n")
    log.close()
    f1.close()
    print("程序运行消耗时间为:", t2 - t1)
