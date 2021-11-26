from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

imgcaption = """
☘️ **Random Logo Created Successfully**✅
◇───────────────◇
🔥 **Created by** :  [🎨 Imᥲgᥱ Tooᥣs Bot](https://t.me/szimagebot)
🌷 **Requestor** : {message.from_user.username}
⚡️ **Powered By **: `【SZ™】´
◇───────────────◇
©2021【SZ™】 team  **All Right Reserved**⚠️️
"""
repmark = InlineKeyboardMarkup(
      [
        [
        InlineKeyboardButton(text="➕Add me to your group ➕", url=f"http://t.me/szimagebot?startgroup=botstart") 
        ],
        [
         InlineKeyboardButton(text="🗣️Join my updates", url=f"https://t.me/szteambots") 
        ]
      ]      
    )
