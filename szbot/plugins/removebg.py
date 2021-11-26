import io
import os
from datetime import datetime
from szbot import tele as sz 
from telethon import events
import requests
from telethon import types
from telethon.tl import functions
from config import REM_BG_API_KEY
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


TEMP_DOWNLOAD_DIRECTORY = "./"

def ReTrieveFile(input_file_name):
    headers = {
        "X-API-Key": REM_BG_API_KEY,
    }
    files = {
        "image_file": (input_file_name, open(input_file_name, "rb")),
    }
    r = requests.post(
        "https://api.remove.bg/v1.0/removebg",
        headers=headers,
        files=files,
        allow_redirects=True,
        stream=True,
    )
    return r

async def is_app_admin(chat, user):
    if isinstance(chat, (types.InputPeerChannel, types.InputChannel)):
        return isinstance(
            (
                await sz(functions.channels.GetParticipantRequest(chat, user))
            ).participant,
            (types.ChannelParticipantAdmin, types.ChannelParticipantCreator),
        )
    if isinstance(chat, types.InputPeerUser):
        return True

TEXT=f"""🗑️** Background removed Successfully**✅
◇───────────────◇
🔥 **Removed  by** : [ 🎨 Imᥲgᥱ Tooᥣs Bot](https://t.me/szimagebot)
⚡️ **Powered By**  : `【SZ™】`
◇───────────────◇
©2021[【SZ™】 team ](https://t.me/szteambots) **All Right Reserved**⚠️️
"""    
    
    
BUTTONS = InlineKeyboardMarkup(	
      [	
        [	
        InlineKeyboardButton(text="➕ Add me to your group ➕", url=f"http://t.me/szimagebot?startgroup=botstart") 	
        ],	
        [	
         InlineKeyboardButton(text="🗣️Join my updates ", url=f"https://t.me/sszteambots") 	
        ]	
      ]      	
    )    
    

@sz.on(events.NewMessage(pattern='^/rmbg'))
async def _(event):
    HELP_STR = "use `/rmbg` as reply to a media.\nJoin my updates channel @sl_bot_zone "
    if event.fwd_from:
        return
    if event.is_group:
        if await is_app_admin(event.input_chat, event.message.sender_id):
            pass
        else:
            return
    if REM_BG_API_KEY is None:
        await event.reply("You need API token from remove.bg to use this plugin.")
        return False
    start = datetime.now()
    message_id = event.message.id
    if event.reply_to_msg_id:
        message_id = event.reply_to_msg_id
        reply_message = await event.get_reply_message()
        gg = await event.reply("** Please wait Processing Your image ...**")
        try:
            downloaded_file_name = await sz.download_media(
                reply_message, TEMP_DOWNLOAD_DIRECTORY
            )
        except Exception as e:
            await event.reply(str(e))
            return
        else:
            output_file_name = ReTrieveFile(downloaded_file_name)
            os.remove(downloaded_file_name)
    else:
        await event.reply(HELP_STR)
        return
    contentType = output_file_name.headers.get("content-type")
    if "image" in contentType:
        with io.BytesIO(output_file_name.content) as remove_bg_image:
            remove_bg_image.name = "rmbg.png"
            await sz.send_file(
                event.chat_id,
                remove_bg_image,
                force_document=True,
                supports_streaming=False,
                allow_cache=False,
                reply_to=message_id,
                caption=TEXT,
                reply_markup=BUTTONS,
                disable_web_page_preview=True
            )
        end = datetime.now()
        ms = (end - start).seconds
        await gg.edit("**🗑️Background Removed in `{}` seconds **".format(ms))
        await gg.delete()
    else:
        await gg.edit(
            "remove.bg API returned Errors. Please report to @slbotzone\n`{}` ".format(
                output_file_name.content.decode("UTF-8")
            )
        )
        await gg.delete()
