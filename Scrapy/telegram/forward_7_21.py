import asyncio
import time

from pyrogram import Client
from pyrogram.handlers import MessageHandler
from pyrogram.errors import FloodWait

api_id = 18492620
api_hash = "85e27071262efb643b2e5ccbde965cfb"

proxy = {
     "scheme": "http",  # "socks4", "socks5" and "http" are supported
     "hostname": "127.0.0.1",
     "port": 7890,
 }
# async def my_function(client, message):
#     await message.forward("me")

app = Client("+8618536384331", api_id=api_id, api_hash=api_hash,proxy=proxy)

async def main():
    async with app:
        # Send a message, Markdown is enabled by default
        chat_id=-1001714003588


        to_chat=-1001583731748


        # from_chat=-1001064408816
        from_chat=-1001278914097


        # from_chat=-1001514265967


        # with open('num.txt','r',encoding='utf-8') as f:
        #     last_read=int(f.read())
        # print(last_read)
        try:

            for r in range(90 ,130):
                num = r * 20
                list = []
                for l in range(num, num + 20):
                    list.append(l)
                pic = await app.forward_messages(to_chat, from_chat, list)
                print(pic)
                for p in pic:
                    print(p['forward_from_message_id'])
                    print(p['media'])

                print("num:", num)
                if len(pic) != 0:
                    await asyncio.sleep(15)
                else:
                    await asyncio.sleep(8)
                if len(pic) == 0 and r >= 50:
                    break
        except FloodWait as e:
            print(e)
            time1 = time.localtime(time.time())
            ti = time.strftime('%Y-%m-%d %H:%M:%S', time1)
            print(ti)
            print(r)
            # await asyncio.sleep(e.x)
        # with open('num.txt','w',enco ding='utf-8') as f:
        #     f.write(str(r))
        # get=await app.get_messages(chat_id, 12)
        # print(get)

        # await app.send_message("me", "Hi there! I'm using **Pyrogram**")


app.run(main())

