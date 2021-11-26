import re
from szbot import sz
from io import BytesIO
from requests import get
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import os 
from PIL import Image, ImageDraw, ImageFont
import random
from szbot.helpers.fsub import ForceSub
from szbot.helpers.database.add_user import AddUserToDatabase
import requests
import shutil


repmark = InlineKeyboardMarkup(
      [
        [
        InlineKeyboardButton(text="➕ Add me to your group ➕", url=f"http://t.me/szimagebot?startgroup=botstart") 
        ],
        [
         InlineKeyboardButton(text="🗣️Join my updates ", url=f"https://t.me/szteambots") 
        ]
      ]      
    )

def nospace(s):

    s = re.sub(r"\s+", '%20', s)

    return s
@sz.on_message(filters.command(["logo", f"logo@szimagebot"]))
async def make_logo(_, message):
    await AddUserToDatabase(_, message)
    FSub = await ForceSub(_, message)
    if FSub == 400:
        return
    imgcaption = f"""
☘️** Logo Created Successfully**✅
◇───────────────◇
🔥 **Created by** : @szimagebot
🌷 **Requestor** : {message.from_user.mention}
⚡️ **Powered By **  : `【SZ™】`
◇───────────────◇
©2021[【SZ™】 team ](https://t.me/szteambots) **All Right Reserved**⚠️️
"""
    if len(message.command) < 2:
            return await message.reply_text("Please give a text to make logo")
    m = await message.reply_text("📸 Creating..")
    name = message.text.split(None, 1)[1] if len(message.command) < 3 else message.text.split(None, 1)[1].replace(" ", "%20")
    api = get(f"https://api.singledevelopers.net/logo?name={name}")
    await m.edit("📤 Uploading ...")
    await sz.send_chat_action(message.chat.id, "upload_photo")
    img = Image.open(BytesIO(api.content))
    logoname = "szlogo.png"
    img.save(logoname, "png")
    await message.reply_photo(photo = logoname,
                              caption=imgcaption,
                              reply_markup = repmark)
    await m.delete()
    if os.path.exists(logoname):
            os.remove(logoname)
                       
fonts = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
# Colour Selection
colour = ["yellow",
          "red",
          "blue"]

logomake = ["https://telegra.ph/file/7cd465d6609ea17141747.jpg", 
            "https://telegra.ph/file/9cafdfbcdc5212b3138a9.jpg", 
            "https://telegra.ph/file/4e56b39faa4c03ca4079c.jpg",]

@sz.on_message(filters.command(["blogo", f"blogo@szimagebot"]))
async def logomake(_, message: Message):
    await AddUserToDatabase(_, message)
    FSub = await ForceSub(_, message)
    if FSub == 400:
        return
    if len(message.command) != 2:
            return await message.reply_text("Please give a text")
    text = message.text.split(None, 1)[1]
    img = Image.open(random.choice(logomake))
    draw = ImageDraw.Draw(img)
    image_widthz, image_heightz = img.size
    font = ImageFont.truetype(fonts,100)
    w, h = draw.textsize(text, font=font)
    h += int(h*0.21)
    draw.text(((image_widthz-w)/2, (image_heightz-h)/2), text, font=font, fill=(255, 255, 255))
    x = (image_widthz-w)/2
    y= ((image_heightz-h)/2+6)
    draw.text((x, y), text, font=font, fill="black", stroke_width=2, stroke_fill=(random.choice(colour)))
    szlogo = "szimg.png"
    imgcaption = f"""
☘️** Logo Created Successfully**✅
◇───────────────◇
🔥 **Created by** : @szimagebot
🌷 **Requestor** : {message.from_user.mention}
⚡️ **Powered By **  : `【SZ™】`
◇───────────────◇
©2021[【SZ™】 team ](https://t.me/szteambots) **All Right Reserved**⚠️️
"""
    img.save(szlogo, "png")
    await message.reply_photo(
                photo=f"szimg.png",
                caption= imgcaption,
            )
    if os.path.exists(szlogo):
            os.remove(szlogo)

alogomake = ["https://telegra.ph/file/7cd465d6609ea17141747.jpg", 
            "https://telegra.ph/file/9cafdfbcdc5212b3138a9.jpg", 
            "https://telegra.ph/file/4e56b39faa4c03ca4079c.jpg",]

@sz.on_message(filters.command(["glogo", f"glogo@szimagebot"]))
async def logomake(_, message: Message):      
    await AddUserToDatabase(_, message)
    FSub = await ForceSub(_, message)
    if FSub == 400:
        return
    if len(message.command) != 2:
            return await message.reply_text("Please give a text")
    else:
       pass
    await message.reply('Creating your logo...wait!')
    text = message.text.split(None, 1)[1]
    img = Image.open(random.choice(alogomake))
    draw = ImageDraw.Draw(img)
    image_widthz, image_heightz = img.size
    font = ImageFont.truetype(fonts,40)
    w, h = draw.textsize(text, font=font)
    h += int(h*0.21)
    draw.text(((image_widthz-w)/2, (image_heightz-h)/2), text, font=font, fill=(255, 255, 255))
    x = (image_widthz-w)/2
    y= ((image_heightz-h)/2+6)
    draw.text((x, y), text, font=font, fill="black", stroke_width=2, stroke_fill="yellow")
    szlogo = "szimg.png"
    imgcaption=f"""
☘️** Logo Created Successfully**✅
◇───────────────◇
🔥 **Created by** : @szimagebot
🌷 **Requestor** : {message.from_user.mention}
⚡️ **Powered By **  : `【SZ™】`
◇───────────────◇
©2021[【SZ™】 team ](https://t.me/szteambots) **All Right Reserved**⚠️️
"""
    img.save(szlogo, "png")
    await message.reply_photo(
                photo=f"szimg.png",
                caption= imgcaption,
            )
    if os.path.exists(szlogo):
            os.remove(szlogo)

glogomake = ["https://telegra.ph/file/7cd465d6609ea17141747.jpg", 
            "https://telegra.ph/file/9cafdfbcdc5212b3138a9.jpg", 
            "https://telegra.ph/file/4e56b39faa4c03ca4079c.jpg",]

@sz.on_message(filters.command(["alogo", f"alogo@szimagebot"]))
async def logomake(_, message: Message):
    await AddUserToDatabase(_, message)
    FSub = await ForceSub(_, message)
    if FSub == 400:
        return
    if len(message.command) != 2:
            return await message.reply_text("Please give a text")
    text = message.text.split(None, 1)[1]
    img = Image.open(random.choice(glogomake))
    draw = ImageDraw.Draw(img)
    image_widthz, image_heightz = img.size
    font = ImageFont.truetype(fonts,100)
    w, h = draw.textsize(text, font=font)
    h += int(h*0.21)
    draw.text(((image_widthz-w)/2, (image_heightz-h)/2), text, font=font, fill=(255, 255, 255))
    x = (image_widthz-w)/2
    y= ((image_heightz-h)/2+6)
    draw.text((x, y), text, font=font, fill="black", stroke_width=2, stroke_fill="green")
    szlogo = "szimg.png"
    imgcaption=f"""
☘️** Logo Created Successfully**✅
◇───────────────◇
🔥 **Created by** : @szimagebot
🌷 **Requestor** : {message.from_user.mention}
⚡️ **Powered By **  : `【SZ™】`
◇───────────────◇
©2021[【SZ™】 team ](https://t.me/szteambots) **All Right Reserved**⚠️️
"""
    img.save(szlogo, "png")
    await message.reply_photo(
                photo=f"szimg.png",
                caption=imgcaption,
            )
    if os.path.exists(szlogo):
            os.remove(szlogo)
