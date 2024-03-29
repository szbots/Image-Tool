import os
import io
import requests
from requests import get
from pyrogram.types import Message
from szbot import sz as pbot
from bs4 import *
from pyrogram import filters	
from PIL import Image
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from szbot.helpers.fsub import ForceSub

def get_text(message: Message) -> [None, str]:
    text_to_return = message.text
    if message.text is None:
        return None
    if " " in text_to_return:
        try:
            return message.text.split(None, 1)[1]
        except IndexError:
            return None
    else:
        return None
      


@pbot.on_message(filters.command(["wall","wallpaper"]))
@ForceSub
async def logo(client, message):      
 quew = get_text(message)
 if not quew:
     await client.send_message(message.chat.id, "😶 **Please Give me A Text For a query!**")
     return
 m = await client.send_message(message.chat.id, "`⚙️ Searching Your wallpapers..`")
 try:
    text = get_text(message)
    LOGO_API = f"https://single-developers.up.railway.app/wallpaper?search={text}"
    randc = (LOGO_API)
    murl = requests.get(f"https://single-developers.up.railway.app/wallpaper?search={text}").history[1].url
    img = Image.open(io.BytesIO(requests.get(randc).content))
    fname = "szrosebot.png"
    img.save(fname, "png")
    caption = f"""
Wallpaper Genarated Successfully✅

࿂ **Generated By** : [szrosebot](https://t.me/szrosebot)
࿂ **Requestor** :. {message.from_user.mention}
࿂ **Powered By **  : [szteambots](https://t.me/szteambots)
࿂ **Download link** : `{murl}`
"""
    await m.delete()
    await client.send_photo(message.chat.id, photo=murl, caption =caption,
                 reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "••Download Link••", url=f"{murl}"
                    )
                ],
            ]
          ),
    )
    if os.path.exists(fname):
            os.remove(fname)
 except Exception as e:
    await client.send_message(message.chat.id, f'An error occurred! Report this @slbotzone, {e}')
