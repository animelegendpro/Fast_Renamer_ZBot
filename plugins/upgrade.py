from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """**ғʀᴇᴇ ᴘʟᴀɴ ᴜsᴇʀ**
	ᴅᴀɪʟʏ  ᴜᴘʟᴏᴀᴅ ʟɪᴍɪᴛ 𝟸ɢʙ
	ᴘʀɪᴄᴇ 𝟶
	
	**🔥 Bᴀsɪᴄ** 
	ᴅᴀɪʟʏ  ᴜᴘʟᴏᴀᴅ  ʟɪᴍɪᴛ 20GB
	ᴘʀɪᴄᴇ ʀs 49  ɪɴᴅɪᴀ /🌎 0.59$  ᴘᴇʀ ᴍᴏɴᴛʜ
	
	**😎 Sᴛᴀɴᴅᴀʀᴅ**
	ᴅᴀɪʟʏ ᴜᴘʟᴏᴀᴅ ʟɪᴍɪᴛ 50GB
	ᴘʀɪᴄᴇ ʀs 99  ɪɴᴅɪᴀ /🌎 1.19$  ᴘᴇʀ ᴍᴏɴᴛʜ
	
	**👑 Uʟᴛɪᴍᴀᴛᴇ**
	ᴅᴀɪʟʏ ᴜᴘʟᴏᴀᴅ ʟɪᴍɪᴛ 100GB
	ᴘʀɪᴄᴇ ʀs 179  ɪɴᴅɪᴀ /🌎 2.16$  ᴘᴇʀ ᴍᴏɴᴛʜ
	
	
	ᴘᴀʏ ᴜsɪɴɢ ᴜᴘɪ ɪ'ᴅ `anime-legend@axl`
	
	<b>ᴀғᴛᴇʀ ᴘᴀʏᴍᴇɴᴛ sᴇɴᴅ sᴄʀᴇᴇɴsʜᴏᴛs ᴏғ</b> 
        <b>ᴘᴀʏᴍᴇɴᴛ ᴛᴏ ᴀᴅᴍɪɴ @Devil_Eyes_ZX</b>"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("Aᴅᴍɪɴ",url = "https://t.me/Devil_Eyes_ZX")], 
        			[InlineKeyboardButton("Pʜᴏɴᴇ ᴘᴀʏ",url = "https://telegra.ph/file/7875724e5ead1d6ded2b4.jpg"),
        			InlineKeyboardButton("Gᴏᴏɢʟᴇ ᴘᴀʏ",url = "https://telegra.ph/file/e08ee420fd2c1c27586cb.jpg")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """**ғʀᴇᴇ ᴘʟᴀɴ ᴜsᴇʀ**
	ᴅᴀɪʟʏ  ᴜᴘʟᴏᴀᴅ ʟɪᴍɪᴛ 2GB
	ᴘʀɪᴄᴇ 0
	
	**🔥 Bᴀsɪᴄ** 
	ᴅᴀɪʟʏ  ᴜᴘʟᴏᴀᴅ  ʟɪᴍɪᴛ 20GB
	ᴘʀɪᴄᴇ ʀs 49  ɪɴᴅɪᴀ /🌎 0.59$  ᴘᴇʀ ᴍᴏɴᴛʜ
	
	**😎 Sᴛᴀɴᴅᴀʀᴅ**
	ᴅᴀɪʟʏ ᴜᴘʟᴏᴀᴅ ʟɪᴍɪᴛ 50GB
	ᴘʀɪᴄᴇ ʀs 99  ɪɴᴅɪᴀ /🌎 1.19$  ᴘᴇʀ ᴍᴏɴᴛʜ
	
	**👑 Uʟᴛɪᴍᴀᴛᴇ**
	ᴅᴀɪʟʏ ᴜᴘʟᴏᴀᴅ ʟɪᴍɪᴛ 100GB
	ᴘʀɪᴄᴇ ʀs 179  ɪɴᴅɪᴀ /🌎 2.16$  ᴘᴇʀ ᴍᴏɴᴛʜ
	
	
	ᴘᴀʏ ᴜsɪɴɢ ᴜᴘɪ ɪ'ᴅ `anime-legend@axl`
	
	<b>ᴀғᴛᴇʀ ᴘᴀʏᴍᴇɴᴛ sᴇɴᴅ sᴄʀᴇᴇɴsʜᴏᴛs ᴏғ</b> 
        <b>ᴘᴀʏᴍᴇɴᴛ ᴛᴏ ᴀᴅᴍɪɴ @Devil_Eyes_ZX</b>"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("Admin",url = "https://t.me/Devil_Eyes_ZX")], 
        			[InlineKeyboardButton("Phone Pay",url = "https://telegra.ph/file/7875724e5ead1d6ded2b4.jpg"),
        			InlineKeyboardButton("Google Pay",url = "https://telegra.ph/file/e08ee420fd2c1c27586cb.jpg")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await message.reply_text(text = text,reply_markup = keybord)








# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Developer @JishuDeveloper
