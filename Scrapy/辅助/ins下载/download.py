import os
import re

import requests
import time
import aiohttp
import asyncio
import aiofile

# 使用多线程或多进程，协程减少下载的时间
# log = open('D:\Pics\log.txt', mode="a", encoding='utf-8')
# f1 = open('D:\Pics\sunyunzhu.txt', mode="r", encoding='utf-8')
t1 = time.time()
# contents=f1.readlines()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    # 'referer': 'https://m.weibo.cn',
}

async def request_pics(url,path_file,name):
    proxie = {'http': 'http://127.0.0.1:7890', 'https': 'https://127.0.0.1:7890'}

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url,proxy='http://127.0.0.1:7890', headers=headers,timeout=250) as resp:
                path = path_file+ '/' + name
                async with aiofile.async_open(path, mode='wb', ) as f:
                    await f.write(await resp.content.read())
                    # print('-' * 10)
    except TimeoutError as e:
        print("-----socket timout:",url)
    except RuntimeError:
        print('Event loop is closed')
    except ConnectionResetError as e:
        print("远程主机强迫关闭了一个现有的连接",e)



async def DownLoadPics(contents):
    tasks=[]

    title=contents['shortcode']
    # title = re.sub('[*]', '', title)
    print(title)
    path_file = rf'D:\Pics\taaarannn\{title}'
    if not os.path.exists(path_file):
        os.makedirs(path_file)
        print(path_file)
    for r in range(1,15):
        url = contents[f'link{r}']
        if len(url)==0:
            break
        name=url.split('/')[-1].split('?')[0]
        print(url)
        tasks.append(asyncio.create_task(request_pics(url,path_file,name)))
    await asyncio.wait(tasks)
if __name__ == '__main__':

    # loop=asyncio.get_event_loop()
    # loop.run_until_complete(DownLoadPics())
    # asyncio.run(DownLoadPics(contents=))
    t2 = time.time()
    # log.write(f"本次运行消耗的时间为:{t2 - t1} \n")
    # log.close()
    # f1.close()
    print("程序运行消耗时间为:", t2 - t1)
