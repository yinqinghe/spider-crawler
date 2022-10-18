import asyncio

from pyrogram import Client
from pyrogram.handlers import MessageHandler
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
# async def my_function(cilent,message):
#
#     await app.create_channel("Channel Title", "Channel Description")
# await asyncio.sleep(2)

#
async def my_function(client,message):
    chat_id = -1001714003588

    await client.forward_messages(
        chat_id=-1001714003588,
        from_chat_id=-1001152046416,
        message_ids=12
    )
    await message.forward(chat_id)
my_handler = MessageHandler(my_function)
app.add_handler(my_handler)
app.run()


# async def main():
#     async with app:
#         # Send a message, Markdown is enabled by default
#         await app.send_message("me", "Hi there! I'm using **Pyrogram**")
#
#
# app.run(main())