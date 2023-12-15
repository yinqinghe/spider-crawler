'''
Author: 殷清贺 987746808@qq.com
Date: 2022-05-11 18:28:55
LastEditors: 殷清贺 987746808@qq.com
LastEditTime: 2022-07-26 20:04:39
FilePath: \pythond:\C#\python\爬虫\Scrapy\telegram\try_more.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import asyncio
import time

from pyrogram import Client
from pyrogram.handlers import MessageHandler
from pyrogram.errors import FloodWait
from pyrogram.raw import functions
from pyrogram.raw import functions, types
api_id = xxx
api_hash = "xxx"

proxy = {
    "scheme": "http",  # "socks4", "socks5" and "http" are supported
    "hostname": "127.0.0.1",
    "port": 7890,
}
# async def my_function(client, message):
#     await message.forward("me")

app = Client("+8618536384331", api_id=api_id, api_hash=api_hash, proxy=proxy)


async def main():
    async with app:
        # Send a message, Markdown is enabled by default
        chat_id = -1001714003588
        # to_chat = -1001714003588
        # to_chat = -1001675197421
        to_chat = -1001583731748
        # to_chat = -1001676663871

        from_chat = -1001434857030

        # await app.send_message("me", "Hi there! I'm using **Pyrogram**")
        # # 获取用户信息
        # me=await app.get_users("me")
        # print(me)
        # chat = await app.get_chat("@lanren_666888")
        # chat = await app.get_chat("@PikPak4_Bot")

        # print(chat)
        # update=functions.messages.SendMessage(peer=5250727789,message='hello',random_id='1998')
        # print(update)
        # anw=await app.send_message("5250727789", "Message sent with **Pyrogram**!")
        # print(anw)
        r = await app.invoke(
            functions.channels.GetFullChannel(
                channel=app.resolve_peer("lanren_6688")
            )
        )

        print(r)
app.run(main())
