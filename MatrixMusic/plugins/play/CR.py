import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from MatrixMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from MatrixMusic import app
from random import  choice, randint

                
@app.on_message(
    command(["سورس","السورس"])
    
)
async def huhh(client: Client, message: Message):
    await message.reply_video(
        video=f"https://telegra.ph/file/f1b3a574b536cdaf4c49e.mp4",
        caption=f"""𝐖𝐞𝐥𝐨𝐦𝐞 𝐓𝐨 𝐒𝐨𝐮𝐫𝐜𝐞 𝗖𝗝 𝐌𝐮𝐬𝐢𝐜""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ᏀᎡΌႮᏢ", url=f"https://t.me/PO_UV"), 
                 InlineKeyboardButton(
                   "𝐂𝐇𝐀𝐍𝐍𝐄𝐋",       url=f"https://t.me/CG_G11"), 
                 
             ],[ 
            InlineKeyboardButton(
                        "『𝐄𝟑𝐃𝐀𝐌 ℡ 』 ☬ ➥ مٓمٓــۄل || -", url=f"https://t.me/DAD_E3DAM"), 
                   InlineKeyboardButton(
                        "𝅄 𓏺 𝑚𝑎ℎ𝑚𝑜𝑢𝑑 .", url=f"https://t.me/E_D_O_D"), 
             ],[ 
                  InlineKeyboardButton(
                text="اضغط لاضافتي لمجموعتك⚡",
                url=f"https://t.me/{app.username}?startgroup=true"),
                ],

            ]

        ),

    )








@app.on_message(
    command(["مطور السورس"])
    
    
)
async def yas(client, message):
    usr = await client.get_chat("DAD_E3DAM")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"معلومات مطور السورس\n\n‍ ¦dev :{name}\n\n ¦user :@{usr.username}\n\n ¦id :`{usr.id}`\n\n ¦bio :{usr.bio}\n\n𝙎𝙊𝙐𝙍𝘾𝙀 𝗖𝗝", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )


@app.on_message(
    command(["محمد" , "اعدام","مطور السورس"])
    
    
)
async def yas(client, message):
    usr = await client.get_chat("DAD_E3DAM")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"معلومات مطور السورس.\n\n¦dev :{name}\n\n ¦user :@{usr.username}\n\n ¦id :`{usr.id}`\n\n ¦boi :{usr.bio}\n\n𝙎𝙊𝙐𝙍𝘾𝙀 𝗖𝗝", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )



@app.on_message(
    command(["مبرمج السورس" , "محمود","الدود"])
    
    
)
async def yas(client, message):
    usr = await client.get_chat("E_D_O_D")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"معلومات مبرمج السورس.\n\n¦dev :{name}\n\n ¦user :@{usr.username}\n\n ¦id :`{usr.id}`\n\n ¦bio :{usr.bio}\n\n𝙎𝙊𝙐𝙍𝘾𝙀 𝗖𝗝", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )



