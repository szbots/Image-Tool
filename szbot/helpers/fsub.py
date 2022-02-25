from functools import wraps
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant


CAPTION_BTN = InlineKeyboardMarkup(
            [[InlineKeyboardButton("News  Channel", url="https://t.me/szteambots")]])

def ForceSub(func):
    @wraps(func)
    async def sz_message(_, message):
        try:
            await message._client.get_chat_member(-1001325914694, message.from_user.id)
        except UserNotParticipant:
            return await message.reply_text(
            text="""
**🚫 Access Denied**
 You Must Join [My News Channel](https://t.me/szteambots)To Use Me. So, Please Join it & Try Again.
            """,
            reply_markup=CAPTION_BTN,
            disable_web_page_preview=True) 
        return await func(_, message)    
    return sz_message
