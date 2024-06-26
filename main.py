import asyncio
import os
import logging
from os import getenv
from pyrogram import Client, filters, idle
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import ChatAdminRequired, FloodWait

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

# config vars
API_ID = int(os.getenv("API_ID", 21793162))
API_HASH = os.getenv("API_HASH", "9cc4a581ea7b9201db27b3e2dc8124a0")
BOT_TOKEN = os.getenv("BOT_TOKEN", "7159078541:AAFopNI3pA7RAWHukR0UesFhChhaNs6hXGw")


# pyrogram client
app = Client(
            "banall",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
)



@app.on_message(
filters.command("ben") 
& filters.private
)
async def banall_command(client, message: Message):
    if len(message.command) < 2:
        return await message.reply("/ben chat_id")
    grup_id = int(message.text.split()[1])
    await message.reply("ban started")
    print("getting memebers from {}".format(message.chat.id))
    async for i in app.get_chat_members(grup_id):
        try:
            await app.ban_chat_member(chat_id = grup_id, user_id = i.user.id)
            print("kicked {} from {}".format(i.user.id, message.chat.id))
            await asyncio.sleep(0.5)
        except FloodWait as e:
            flood_time = int(e.x)
            if flood_time > 200:
                continue
            await asyncio.sleep(flood_time) 
        except Exception:
            continue           
    print("process completed")
    

# start bot client
app.start()
print("started")
idle()
