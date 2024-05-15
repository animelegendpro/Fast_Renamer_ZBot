"""JishuDeveloper"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup)
from pyrogram import Client , filters
from script import *
from config import *



@Client.on_callback_query(filters.regex('about'))
async def about(bot,update):
    text = script.ABOUT_TXT
    keybord = InlineKeyboardMarkup([  
                    [InlineKeyboardButton("《 Back",callback_data = "home")]
                  ])
    await update.message.edit(text = text,reply_markup = keybord)


@Client.on_message(filters.private & filters.command(["donate"]))
async def donatecm(bot,message):
	text = script.DONATE_TXT
	keybord = InlineKeyboardMarkup([
        			[InlineKeyboardButton("🍁 Aᴅᴍɪɴ",url = "https://t.me/Devil_Eyes_ZX"), 
        			InlineKeyboardButton("✘ Cʟᴏsᴇ",callback_data = "cancel") ]])
	await message.reply_text(text = text,reply_markup = keybord)

@Client.on_message(filters.private & filters.user(OWNER) & filters.command(["admin"]))
async def admincm(bot,message):
	text = script.ADMIN_TXT
	keybord = InlineKeyboardMarkup([
        			[InlineKeyboardButton("✘ Cʟᴏsᴇ ✘",callback_data = "cancel") ]])
	await message.reply_text(text = text,reply_markup = keybord)

@Client.on_callback_query(filters.regex('help'))
async def help(bot,update):
    text = script.HELP_TXT.format(update.from_user.mention)
    keybord = InlineKeyboardMarkup([ 
                    [InlineKeyboardButton('Tʜᴜᴍʙɴᴀɪʟ', callback_data='thumbnail'),
                    InlineKeyboardButton('Cᴀᴘᴛɪᴏɴ', callback_data='caption')],
                    [InlineKeyboardButton('《 Hᴏᴍᴇ', callback_data='home'),
                    InlineKeyboardButton('Dᴏɴᴀᴛᴇ', callback_data='donate')]
                   ])
    await update.message.edit(text = text,reply_markup = keybord)

@Client.on_callback_query(filters.regex('thumbnail'))
async def thumbnail(bot,update):
    text = script.THUMBNAIL_TXT
    keybord = InlineKeyboardMarkup([  
                    [InlineKeyboardButton("《 Bᴀᴄᴋ",callback_data = "help")]
		  ])
    await update.message.edit(text = text,reply_markup = keybord)

@Client.on_callback_query(filters.regex('caption'))
async def caption(bot,update):
    text = script.CAPTION_TXT
    keybord = InlineKeyboardMarkup([  
                    [InlineKeyboardButton("《 Bᴀᴄᴋ",callback_data = "help")]
		  ])
    await update.message.edit(text = text,reply_markup = keybord)

@Client.on_callback_query(filters.regex('donate'))
async def donate(bot,update):
    text = script.DONATE_TXT
    keybord = InlineKeyboardMarkup([  
                    [InlineKeyboardButton("《 Bᴀᴄᴋ",callback_data = "help")]
		  ])
    await update.message.edit(text = text,reply_markup = keybord)


@Client.on_callback_query(filters.regex('home'))
async def home_callback_handler(bot, query):
    text = f"""Hello {query.from_user.mention} \n\n➻ This Is An Advanced And Yet Powerful Rename Bot.\n\n➻ Using This Bot You Can Rename And Change Thumbnail Of Your Files.\n\n➻ You Can Also Convert Video To File Aɴᴅ File To Video.\n\n➻ This Bot Also Supports Custom Thumbnail And Custom Caption.\n\n<b>Bot Is Made By @Madflix_Bots</b>"""
    keybord = InlineKeyboardMarkup([  
                    [InlineKeyboardButton("Uᴘᴅᴀᴛᴇs", url="https://t.me/ZPro_Bots"),
                    InlineKeyboardButton("Sᴜᴘᴘᴏʀᴛ", url="https://t.me/+FGM0HOnjDC45ZDk1")],
                    [InlineKeyboardButton("Hᴇʟᴘ", callback_data='help'),
		            InlineKeyboardButton("Aʙᴏᴜᴛ", callback_data='about')],
                    [InlineKeyboardButton("🍁 ᴘʀᴇᴍɪᴜᴍ 🍁", url="https://t.me/(upgrade)")]
		  ])
    await query.message.edit_text(text=text, reply_markup=keybord)






# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Developer @JishuDeveloper
