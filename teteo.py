from pyrogram import Client, filters
from pyrogram.types import Message
import psutil

bot = Client("A", 9151592, "555f3cd13bbeee85b76fd83f713026a9", bot_token="5532363438:AAGnhI2vD_rm9l_o_uBPW8YOGIAgUAobWEU", )

@bot.on_message(filters.command("/ssd"))
async def Hello(client, message: Message):
    disk = psutil.disk_usage(".").total
    await message.reply(disk/ 1000 /1000 / 1000)

bot.run()