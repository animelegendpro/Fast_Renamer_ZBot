class script(object):
    HELP_TXT = """<b>ʜᴇʏ 😎</b> {}
    
<b>ʜᴇʀᴇ ɪs ᴛʜᴇ ʜᴇʟᴘ ғᴏʀ ᴍʏ ᴄᴏᴍᴍᴀɴᴅs.</b>"""

    CAPTION_TXT = """<b>๏ ʜᴏᴡ ᴛᴏ sᴇᴛ ᴄᴀᴘᴛɪᴏɴ ๏</b>

<b>↬ /set_caption - ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ sᴇᴛ ʏᴏᴜʀ ᴄᴀᴘᴛɪᴏɴ</b>
<b>↬ /see_caption - ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ sᴇᴇ ʏᴏᴜʀ ᴄᴀᴘᴛɪᴏɴ</b>
<b>↬ /del_caption - ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴅᴇʟᴇᴛᴇ ʏᴏᴜʀ ᴄᴀᴘᴛɪᴏɴ</b>"""
   
    THUMBNAIL_TXT = """<b>๏ ʜᴏᴡ ᴛᴏ sᴇᴛ ᴛʜᴜᴍʙɴᴀɪʟ ๏</b>

<b>↬ ʏᴏᴜ ᴄᴀɴ ᴀᴅᴅ ᴄᴜsᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ sɪᴍᴘʟʏ ʙʏ sᴇɴᴅɪɴɢ ᴀ ᴘʜᴏᴛᴏ ᴛᴏ ᴍᴇ....</b>

<b>↬ /viewthumb - ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ sᴇᴇ ʏᴏᴜʀ ᴛʜᴜᴍʙɴᴀɪʟ</b>
<b>↬ /delthumb - ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴅᴇʟᴇᴛᴇ ʏᴏᴜʀ ᴛʜᴜᴍʙɴᴀɪʟ</b>"""

    ABOUT_TXT = """<b>๏ ᴍʏ ɴᴀᴍᴇ :</b> <a href='https://t.me/Fast_Renamer_ZBot'><b>Fast Renamer ZBot</b></a>
<b>○ ʟᴀɴɢᴜᴀɢᴇ :</b> <a href='https://python.org'><b>ᴘʏᴛʜᴏɴ 3</b></a>
<b>○ ʟɪʙʀᴀʀʏ :</b> <a href='https://pyrogram.org'><b>ᴘʏʀᴏɢʀᴀᴍ 2.0</b></a>
<b>○ sᴇʀᴠᴇʀ :</b> <a href='https://heroku.com'><b>ʜᴇʀᴏᴋᴜ</b></a>
<b>○ ᴄʜᴀɴɴᴇʟ :</b> <a href='https://t.me/ZPro_Bots'><b>Zᴘʀᴏ ʙᴏᴛs</b></a>
<b>○ ᴅᴇᴠᴇʟᴏᴘᴇʀ :</b> <a href='https://t.me/Devil_Eyes_ZX'><b>Ɗᴇᴠɪʟ ᴇʏᴇs</b></a>

<b>♻ ʙᴏᴛ ᴍᴀᴅᴇ ʙʏ :</b> @ZPro_Bots"""

    DONATE_TXT = """
<b>🥲 ᴛʜᴀɴᴋs ғᴏʀ sʜᴏᴡɪɴɢ ɪɴᴛᴇʀᴇsᴛ ɪɴ ᴅᴏɴᴀᴛɪᴏɴ! ❤️</b>

<b>↬ ɪғ ʏᴏᴜ ʟɪᴋᴇ ᴍʏ ʙᴏᴛs & ᴘʀᴏᴊᴇᴄᴛs, ʏᴏᴜ ᴄᴀɴ ᴅᴏɴᴀᴛᴇ ᴍᴇ ᴀɴʏ ᴀᴍᴏᴜɴᴛ ғʀᴏᴍ 𝟸𝟶 ʀs ᴜᴘᴛᴏ ʏᴏᴜʀ ᴄʜᴏɪᴄᴇ.</b>

<b>🛍 ᴜᴘɪ ɪᴅ:</b> <code>anime-legend@axl</code> 


    ADMIN_TXT = """<b><u>🦋 ADMIN ALL COMMANDS HERE</u></b>

<b>⦿ /users - Use This Command To See Total Users</b>
<b>⦿ /allids - Use This Command To See All Users IDs</b>
<b>⦿ /broadcast - Use This Command To Send A Message To Users</b>
<b>⦿ /warn - Use This Command To Send A Message To A User</b>
<b>⦿ /resetpower - Use This Command To Reset User Power</b>
<b>⦿ /ceasepower - Use This Command To Cease User Power</b>
<b>⦿ /addpremium - Use This Command To Add Premium To Users</b>
<b>⦿ /restart - Use This Command To Cancel All Process And Restart The Bot</b>"""






# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Developer @JishuDeveloper
