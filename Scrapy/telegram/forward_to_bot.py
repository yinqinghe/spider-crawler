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

        # to_chat = -1001583731748   #pics
        # to_chat = -1001676663871

        to_chat=5250727789   #save to Pikpak
        # to_chat=-1001714003588


        # from_chat=-1001381662338    #欧美精选
        # from_chat=-1001295602129    #春潮阁_美臀图鉴
        # from_chat=-1001553566346    #高清AV影院

        # from_chat=-1001186971158     #@gtkankan8
        # from_chat=-1001500466490     #@tglm_oumei
        # from_chat=-1001597729580     #@youzhi3333

        # from_chat=-1001167369239     #@pornoasis
        # from_chat=-1001468739616     #@wuma88
        # from_chat=-1001281624577     #@dubai0166

        from_chat=-1001156730731     #@random_porn


        try:
            ti = 0
            for r in range(29,500):#438
                num=r*20
                list = []
                for l in range(num,num+20):
                    list.append(l)
                pic=await app.forward_messages(to_chat, from_chat,list)
                print(pic)
                for p in pic:
                    print(p['forward_from_message_id'])
                    print(p['media'])

                print("num:", num)

                ti=ti+1
                if ti>10:
                    # await asyncio.sleep(78)
                    print('ti:::::::',ti)
                    ti=0
                if len(pic) != 0:
                    await asyncio.sleep(17)
                else:
                    await asyncio.sleep(8)
                if len(pic)==0 and r>=50:
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

