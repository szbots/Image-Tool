
from pyrogram import filters
from bot.modules.funcs import sz_checks
from bot import sz
import os
import json
import requests
from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineQueryResultArticle, InlineQueryResultPhoto,
                            InputTextMessageContent)
from pykeyboard import InlineKeyboard
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import traceback
from pyrogram.errors import UserNotParticipant          
from bot.modules import *


picmebtns = InlineKeyboardMarkup(
            [       
                [
                    InlineKeyboardButton("Pic me", callback_data="picme me"),
                    InlineKeyboardButton("Hq logo", callback_data="picme hql") 
                ],
                [
                    InlineKeyboardButton("Logo", callback_data="picme new"),
                    InlineKeyboardButton("Wallpaper", callback_data="picme wall")           
                ],   
            ]
        )

async def inline_help_func():
    answerss = [
        InlineQueryResultArticle(
            title="Button Menu",
            description="Now you can create your own logo create tool useing this bot",
            input_message_content=InputTextMessageContent(
                """
**Now You can Create your Image Useing Me!**

✪ Pic me : Capture Your Profile Picture.
✪ Hq logo : Create your own hq logo.
✪ Logo : create your own logo.
✪ Wallpaper : Get some new wallpapers.

Send To Inbox Automatically You must start
[This Bot](https://t.me/szimagebot)               
                """
            ),
            thumb_url="https://telegra.ph/file/77e05e0b5bd6a60eb5ca9.jpg",
            reply_markup=picmebtns,
        ),
    ]
    return answerss


@sz.on_inline_query()
async def inline_query_handler(client, query):
    try:
        text = query.query.strip().lower()
        answers = []
        if text.strip() == "":
            answerss = await inline_help_func()
            await client.answer_inline_query(
                query.id, results=answerss, cache_time=10
            )
        elif text.split()[0] == "Logo":
            if len(text.split()) < 3:
                return await client.answer_inline_query(
                    query.id,
                    results=answers,
                    switch_pm_text="Logo",
                )   
        elif text.split()[0] == "hqlogo":
            if len(text.split()) < 3:
                return await client.answer_inline_query(
                    query.id,
                    results=answers,
                    switch_pm_text="Hqlogo",
                )    
        elif text.split()[0] == "wall":
            if len(text.split()) < 3:
                return await client.answer_inline_query(
                    query.id,
                    results=answers,
                    switch_pm_text="wall",
                )
    except Exception as e:
        e = traceback.format_exc()
        return answers
