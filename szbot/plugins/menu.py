from szbot import sz
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery







START_BTN = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("About", callback_data="aboutmenu"),
                    InlineKeyboardButton("Help", callback_data="helpmenu")
                ],
                [
                    InlineKeyboardButton("Updates", url="https://t.me/szteambots"),
                    InlineKeyboardButton("Support", url="https://t.me/slbotzone")
                ],
                [
                    InlineKeyboardButton("➕Add me to your group ➕", url="http://t.me/szimagebot?startgroup=botstart") 
                ]
            ]
        )

GROUP_BTN = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("help", callback_data="helpmenu")
                ]
            ]
        )

HELP_TEXT = f"""

**Help Menu** : 
- /logo [logo name ]
- /logohq [logo name ]
- /rmbg [reply to photo ]
- /edit [reply to photo ] 
- /carbon [reply to text]
- /rlogo [logo name]
- /wall or wallpaper [name]

**Powered By** ~ @szteambots
"""

BACKTOHOME = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🔙Back", callback_data="startmenu")
                ]
            ]
        )

ABOUT_TEXT = """
**Logo Design Platform in Telegram , 
World First Time With Image Editor tools**

🔥You Can Create Many Type Of **Logo Design**
For your Dp & More Usage , Remove Background  
With full **Advance image Editor Features** Included 
This Bot Based on @MalithRukshan **Logo API**
& **TroJanzHex Image editor** 

ᗚ **Features** : 

[+] Api Based logo Creator.
[+] Rando logo Creator .
[+] Carbon maker.
[+] Background Remover.
[+] Text art Genarator 80+ styles.
[+] Image editor.
`(Bright | Mixed | Black & White | Cartoon 
Circle | Blur | Border | Sticker |
Rotate | Contrast | Sepia | Pencil 
| Invert | Glitch | Remove Background)`
"""

CLOSE_BTN =  InlineKeyboardMarkup(
            [[InlineKeyboardButton("News  Channel", url="https://t.me/szteambots")]])


FSUB_TEXT = """
**🚫 Access Denied**
You Must Join [My News Channel](https://t.me/szteambots)To Use Me. So, Please Join it & Try Again.
            """

FSUB_BTN = InlineKeyboardMarkup(
            [[InlineKeyboardButton("News  Channel", url="https://t.me/szteambots")]])

@sz.on_callback_query(filters.regex("startmenu"))
async def startmenu(_, query: CallbackQuery):
    await query.edit_message_text(START_TEXT,
        reply_markup=START_BTN,
     disable_web_page_preview=True
    )

@sz.on_callback_query(filters.regex("helpmenu"))
async def helpmenu(_, query: CallbackQuery):
    await query.edit_message_text(HELP_TEXT,
        reply_markup=BACKTOHOME,
     disable_web_page_preview=True
    )

@sz.on_callback_query(filters.regex("aboutmenu"))
async def aboutenu(_, query: CallbackQuery):
    await query.edit_message_text(ABOUT_TEXT,
        reply_markup=BACKTOHOME,
     disable_web_page_preview=True
    )

@sz.on_callback_query(filters.regex("closeit"))
async def close(_, query: CallbackQuery):
    await query.message.delete()        

