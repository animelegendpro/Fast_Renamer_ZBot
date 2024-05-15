from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup)
from config import *
from pyrogram import Client, filters
from helper.date import add_date
from helper.database import uploadlimit, usertype, addpre


@Client.on_message(filters.private & filters.user(OWNER) & filters.command(["warn"]))
async def warn(c, m):
        if len(m.command) >= 3:
            try:
                user_id = m.text.split(' ', 2)[1]
                reason = m.text.split(' ', 2)[2]
                await m.reply_text("User Notfied Sucessfully 😁")
                await c.send_message(chat_id=int(user_id), text=reason)
            except:
                 await m.reply_text("User Not Notfied Sucessfully 😔")


@Client.on_message(filters.private & filters.user(OWNER) & filters.command(["addpremium"]))
async def buypremium(bot, message):
	await message.reply_text("<b>๏ sᴇʟᴇᴄᴛ ᴘʟᴀɴ ᴛᴏ ᴜᴘɢʀᴀᴅᴇ...</b>", quote=True, reply_markup=InlineKeyboardMarkup([
		           [InlineKeyboardButton("🪙 ʙᴀsɪᴄ", callback_data="vip1")],
				   [InlineKeyboardButton("⚡ sᴛᴀɴᴅᴀʀᴅ", callback_data="vip2")],
				   [InlineKeyboardButton("👑 ᴘʀᴏ", callback_data="vip3")],
				   [InlineKeyboardButton("✘ ᴄᴀɴᴄᴇʟ ✘",callback_data = "cancel")]
				   
				   ]))


@Client.on_message((filters.channel | filters.private) & filters.user(OWNER) & filters.command(["ceasepower"]))
async def ceasepremium(bot, message):
	await message.reply_text("<b>๏ ᴘᴏᴡᴇʀ ᴄᴇᴀsᴇ ᴍᴏᴅᴇ...</b>", quote=True, reply_markup=InlineKeyboardMarkup([
		           [InlineKeyboardButton("ʟɪᴍɪᴛ 1GB", callback_data="cp1")],
				   [InlineKeyboardButton("ᴀʟʟ ᴘᴏᴡᴇʀ ᴄᴇᴀsᴇ", callback_data="cp2")],
				   [InlineKeyboardButton("✘ ᴄᴀɴᴄᴇʟ ✘",callback_data = "cancel")]
				   
				   ]))


@Client.on_message((filters.channel | filters.private) & filters.user(OWNER) & filters.command(["resetpower"]))
async def resetpower(bot, message):
	    await message.reply_text(text=f"Do ʏᴏᴜ ʀᴇᴀʟʟʏ ᴡᴀɴᴛ ᴛᴏ ʀᴇsᴇᴛ ᴅᴀɪʟʏ ʟɪᴍɪᴛ ᴛᴏ ᴅᴇғᴀᴜʟᴛ ᴅᴀᴛᴀ ʟɪᴍɪᴛ 2GB ?",quote=True,reply_markup=InlineKeyboardMarkup([
		           [InlineKeyboardButton("• ʏᴇs ! sᴇᴛ ᴀs ᴅᴇғᴀᴜʟᴛ •",callback_data = "dft")],
				   [InlineKeyboardButton("✘ ᴄᴀɴᴄᴇʟ ✘",callback_data = "cancel")]
				   ]))


# PREMIUM POWER MODE @JISHUDEVELOPER

@Client.on_callback_query(filters.regex('vip1'))
async def vip1(bot,update):
	id = update.message.reply_to_message.text.split("/addpremium")
	user_id = id[1].replace(" ", "")
	inlimit  = 21474836500
	uploadlimit(int(user_id),21474836500)
	usertype(int(user_id),"🪙 ʙᴀsɪᴄ")
	addpre(int(user_id))
	await update.message.edit("ᴀᴅᴅᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ ᴛᴏ ᴘʀᴇᴍɪᴜᴍ ᴜᴘʟᴏᴀᴅ ʟɪᴍɪᴛ 20 GB")
	await bot.send_message(user_id,"ʜᴇʏ ʏᴏᴜ ᴀʀᴇ ᴜᴘɢʀᴀᴅᴇᴅ ᴛᴏ ʙᴀsɪᴄ. ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴘʟᴀɴ ʜᴇʀᴇ /myplan")

@Client.on_callback_query(filters.regex('vip2'))
async def vip2(bot,update):
	id = update.message.reply_to_message.text.split("/addpremium")
	user_id = id[1].replace(" ", "")
	inlimit = 53687091200
	uploadlimit(int(user_id), 53687091200)
	usertype(int(user_id),"⚡ sᴛᴀɴᴅᴀʀᴅ")
	addpre(int(user_id))
	await update.message.edit("ᴀᴅᴅᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ ᴛᴏ ᴘʀᴇᴍɪᴜᴍ ᴜᴘʟᴏᴀᴅ ʟɪᴍɪᴛ 50 GB")
	await bot.send_message(user_id,"ʜᴇʏ ʏᴏᴜ ᴀʀᴇ ᴜᴘɢʀᴀᴅᴇᴅ ᴛᴏ sᴛᴀɴᴅᴀʀᴅ. ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴘʟᴀɴ ʜᴇʀᴇ /myplan")

@Client.on_callback_query(filters.regex('vip3'))
async def vip3(bot,update):
	id = update.message.reply_to_message.text.split("/addpremium")
	user_id = id[1].replace(" ", "")
	inlimit = 107374182400
	uploadlimit(int(user_id), 107374182400)
	usertype(int(user_id),"👑 ᴘʀᴏ")
	addpre(int(user_id))
	await update.message.edit("ᴀᴅᴅᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ ᴛᴏ ᴘʀᴇᴍɪᴜᴍ ᴜᴘʟᴏᴀᴅ ʟɪᴍɪᴛ 𝟷𝟶𝟶 ɢʙ")
	await bot.send_message(user_id,"ʜᴇʏ ʏᴏᴜ ᴀʀᴇ ᴜᴘɢʀᴀᴅᴇᴅ ᴛᴏ ᴘʀᴏ. ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴘʟᴀɴ ʜᴇʀᴇ /myplan")


# CEASE POWER MODE @JISHUDEVELOPER

@Client.on_callback_query(filters.regex('cp1'))
async def cp1(bot,update):
	id = update.message.reply_to_message.text.split("/ceasepower")
	user_id = id[1].replace(" ", "")
	inlimit  = 2147483652
	uploadlimit(int(user_id), 2147483652)
	usertype(int(user_id),"⚠️ ᴀᴄᴄᴏᴜɴᴛ ᴅᴏᴡɴɢʀᴀᴅᴇᴅ")
	addpre(int(user_id))
	await update.message.edit("ᴀᴅᴅᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ ᴛᴏ ᴜᴘʟᴏᴀᴅ ʟɪᴍɪᴛ 2GB")
	await bot.send_message(user_id,"ʜᴇʏ ʏᴏᴜ ᴀʀᴇ ᴅᴏᴡɴɢʀᴀᴅᴇᴅ ᴛᴏ ᴄᴇᴀsᴇ ʟɪᴍɪᴛ 2GB. ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴘʟᴀɴ ʜᴇʀᴇ /myplan \n\n**ᴄᴏɴᴛᴀᴄᴛ ᴀᴅᴍɪɴ :** @Devil_Eyes_ZX")


@Client.on_callback_query(filters.regex('cp2'))
async def cp2(bot,update):
	id = update.message.reply_to_message.text.split("/ceasepower")
	user_id = id[1].replace(" ", "")
	inlimit  = 0
	uploadlimit(int(user_id), 0)
	usertype(int(user_id),"⚠️ ᴀᴄᴄᴏᴜɴᴛ ᴅᴏᴡɴɢʀᴀᴅᴇᴅ")
	addpre(int(user_id))
	await update.message.edit("ᴀᴅᴅᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ ᴛᴏ ᴜᴘʟᴏᴀᴅ ʟɪᴍɪᴛ 0GB")
	await bot.send_message(user_id,"ʜᴇʏ ʏᴏᴜ ᴀʀᴇ ᴅᴏᴡɴɢʀᴀᴅᴇᴅ ᴛᴏ ᴄᴇᴀsᴇ ʟɪᴍɪᴛ 0GB. ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴘʟᴀɴ ʜᴇʀᴇ /myplan \n\n**ᴄᴏɴᴛᴀᴄᴛ ᴀᴅᴍɪɴ :** @Devil_Eyes_ZX")



# RESET POWER MODE @JISHUDEVELOPER


@Client.on_callback_query(filters.regex('dft'))
async def dft(bot,update):
	id = update.message.reply_to_message.text.split("/resetpower")
	user_id = id[1].replace(" ", "")
	inlimit = 2147483652
	uploadlimit(int(user_id), 2147483652)
	usertype(int(user_id),"🆓 Fʀᴇᴇ")
	addpre(int(user_id))
	await update.message.edit("**ᴅᴀɪʟʏ ᴅᴀᴛᴀ ʟɪᴍɪᴛ ʜᴀs ʙᴇᴇɴ ʀᴇsᴇᴛ sᴜᴄᴄᴇssғᴜʟʟʏ.**\n\nᴛʜɪs ᴀᴄᴄᴏᴜɴᴛ ʜᴀs ᴅᴇғᴀᴜʟᴛ 2GB ʀᴇᴍᴀɪɴɪɴɢ ᴄᴀᴘᴀᴄɪᴛʏ")
	await bot.send_message(user_id,"**ʏᴏᴜʀ ᴅᴀɪʟʏ ᴅᴀᴛᴀ ʟɪᴍɪᴛ ʜᴀs ʙᴇᴇɴ ʀᴇsᴇᴛ sᴜᴄᴄᴇssғᴜʟʟʏ.**\n\nᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴘʟᴀɴ ʜᴇʀᴇ /myplan\n\n**ᴄᴏɴᴛᴀᴄᴛ ᴀᴅᴍɪɴ :** <a href='https://t.me/Devil_Eyes_ZX'>Devil Eyes</a>")






# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Developer @JishuDeveloper
