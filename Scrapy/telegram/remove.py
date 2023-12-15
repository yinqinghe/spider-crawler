import asyncio

from pyrogram import Client
from pyrogram.handlers import MessageHandler
api_id = xxx
api_hash = "xxx"

proxy = {
     "scheme": "http",  # "socks4", "socks5" and "http" are supported
     "hostname": "127.0.0.1",
     "port": 7890,
 }
# async def my_function(client, message):
#     await message.forward("me")

app = Client("+8618536384331", api_id=api_id, api_hash=api_hash,proxy=proxy)
# async def my_function(cilent,message):
#
#     await app.create_channel("Channel Title", "Channel Description")
# await asyncio.sleep(2)
# async def my_function(client,message):
#     chat_id = -1001714003588
#
#     await app.read_chat_history(chat_id)
#     #
#     # await client.forward_messages(
#     #     chat_id=-1001714003588,
#     #     from_chat_id=-1001152046416,
#     #     message_ids=12
#     # )
#     # await message.forward(chat_id)
# my_handler = MessageHandler(my_function)
# app.add_handler(my_handler)
# app.run()
async def main():
    async with app:
        # Send a message, Markdown is enabled by default
        chat_id=-1001714003588
        to_chat = -1001714003588
        from_chat=-1001152046416
        # id=await app.get_chat_history(chat_id)
        # print(id)
        # chat = await app.get_chat("MikeJordan98")
        # print(chat)
        # count = await app.get_dialogs_count()
        # print(count)
        # me = await app.get_me()
        # print(me)
        # pic=await app.forward_messages(to_chat, from_chat, 120)
        # print(pic)
        # get=await app.get_messages(chat_id, 12)
        # print(get)
        list = []
        for l in range(100,200):
            list.append(l)
        dele=await app.delete_messages(chat_id,list)
        print(dele)
        # await app.send_message("me", "Hi there! I'm using **Pyrogram**")


app.run(main())

