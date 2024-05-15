import time
from pyrogram import Client, filters
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup)
from helper.database import find_one, used_limit
from helper.database import daily as daily_
import datetime
from datetime import datetime
from datetime import date as date_
from helper.progress import humanbytes
from helper.database import daily as daily_
from helper.date import check_expi
from helper.database import uploadlimit, usertype


@Client.on_message(filters.private & filters.command(["myplan"]))
async def start(client, message):
    used_ = find_one(message.from_user.id)
    daily = used_["daily"]
    expi = daily - \
        int(time.mktime(time.strptime(str(date_.today()), '%Y-%m-%d')))
    if expi != 0:
        today = date_.today()
        pattern = '%Y-%m-%d'
        epcho = int(time.mktime(time.strptime(str(today), pattern)))
        daily_(message.from_user.id, epcho)
        used_limit(message.from_user.id, 0)
    _newus = find_one(message.from_user.id)
    used = _newus["used_limit"]
    limit = _newus["uploadlimit"]
    remain = int(limit) - int(used)
    user = _newus["usertype"]
    ends = _newus["prexdate"]
    if ends:
        pre_check = check_expi(ends)
        if pre_check == False:
            uploadlimit(message.from_user.id, 2147483652)
            usertype(message.from_user.id, "Free")
    if ends == None:
        text = f"**User ID :** `{message.from_user.id}` \n**Name :** {message.from_user.mention} \n\n**<b>🏷 ᴘʟᴀɴ :</b>** {user} \n\n<b>✓ ᴜᴘʟᴏᴀᴅ 2GB ғɪʟᴇs \n<b>✓ ᴅᴀɪʟʏ ᴜᴘʟᴏᴀᴅ <b>: {humanbytes(limit)} \n<b>✓ ᴛᴏᴅᴀʏ ᴜsᴇᴅ </b>: {humanbytes(used)} \n</b>✓ ʀᴇᴍᴀɪɴ :</b> {humanbytes(remain)} \n</b>✓ ᴛɪᴍᴇᴏᴜᴛ :</b> 2 ᴍɪɴᴜᴛᴇs \n<b>✓ ᴘᴀʀᴀʟʟᴇʟ ᴘʀᴏᴄᴇss :</b> ᴜɴʟɪᴍɪᴛᴇᴅ \n<b>✓ ᴛɪᴍᴇ ɢᴀᴘ :</b> ʏᴇs \n\n**<b>ᴠᴀʟɪᴅɪᴛʏ :</b>** ʟɪғᴇᴛɪᴍᴇ"
    else:
        normal_date = datetime.fromtimestamp(ends).strftime('%Y-%m-%d')
        text = f"**User ID :** `{message.from_user.id}` \n**Name :** {message.from_user.mention} \n\n**<b>🏷 ᴘʟᴀɴ :</b>** {user} \n\n<b>✓ ʜɪɢʜ ᴘʀɪᴏʀɪᴛʏ </b>\n<b>✓ ᴜᴘʟᴏᴀᴅ 4GB ғɪʟᴇs </b>\n<b>✓ ᴅᴀɪʟʏ ᴜᴘʟᴏᴀᴅ </b>: {humanbytes(limit)} \n<b>✓ ᴛᴏᴅᴀʏ ᴜsᴇᴅ </b>: {humanbytes(used)} \n<b>✓ ʀᴇᴍᴀɪɴ :</b> {humanbytes(remain)} \n<b>✓ ᴛɪᴍᴇᴏᴜᴛ :</b> 0 sᴇᴄᴏɴᴅ \n</b>✓ ᴘᴀʀᴀʟʟᴇʟ ᴘʀᴏᴄᴇss :</b> ᴜɴʟɪᴍɪᴛᴇᴅ \n<b>✓ ᴛɪᴍᴇ ɢᴀᴘ :</b> Yes \n\n**<b>ʏᴏᴜʀ ᴘʟᴀɴ ᴇɴᴅs ᴏɴ </b>:** {normal_date}"

    if user == "Free":
        await message.reply(text, quote=True, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("<b>💳 ᴜᴘɢʀᴀᴅᴇ</b>", callback_data="upgrade"), InlineKeyboardButton("✘ ᴄᴀɴᴄᴇʟ", callback_data="cancel")]]))
    else:
        await message.reply(text, quote=True, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("<b>✘ ᴄᴀɴᴄᴇʟ ✘</b>", callback_data="cancel")]]))





# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Developer @JishuDeveloper
