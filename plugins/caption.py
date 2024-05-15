from pyrogram import Client, filters 
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from helper.database import *

@Client.on_message(filters.private & filters.command('set_caption'))
async def add_caption(client, message):
    if len(message.command) == 1:
       return await message.reply_text("**ɢɪᴠᴇ ᴍᴇ ᴀ ᴄᴀᴘᴛɪᴏɴ ᴛᴏ sᴇᴛ.\n\nExᴀᴍᴘʟᴇ:- `/set_caption 📕 Nᴀᴍᴇ ➠ : {filename} \n\n🔗 Size ➠ : {filesize} \n\n⏰ Dᴜʀᴀᴛɪᴏɴ ➠ : {duration}`**")
    caption = message.text.split(" ", 1)[1]
    addcaption(int(message.chat.id), caption)
    await message.reply_text("**ʏᴏᴜʀ ᴄᴀᴘᴛɪᴏɴ sᴜᴄᴄᴇssғᴜʟʟʏ ᴀᴅᴅᴇᴅ ✓**")

@Client.on_message(filters.private & filters.command('del_caption'))
async def delete_caption(client, message): 
    caption = find(int(message.chat.id))[1]
    if not caption:
        await message.reply_text("**ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴀɴʏ ᴄᴜsᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ ✘**")
        return
    delcaption(int(message.chat.id))
    await message.reply_text("**ʏᴏᴜʀ ᴄᴀᴘᴛɪᴏɴ sᴜᴄᴄᴇssғᴜʟʟʏ ᴅᴇʟᴇᴛᴇᴅ 🗑️**")
                                       
@Client.on_message(filters.private & filters.command('see_caption'))
async def see_caption(client, message): 
    caption = find(int(message.chat.id))[1]
    if caption:
       await message.reply_text(f"<b><u>ʏᴏᴜʀ ᴄᴀᴘᴛɪᴏɴ:</b></u>\n\n`{caption}`")
    else:
       await message.reply_text("**ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴀɴʏ ᴄᴜsᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ ✘**")
          




# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Developer @JishuDeveloper
