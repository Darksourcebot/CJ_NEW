#_____كسمك تحياتي 
#_____@DAD_E3DAM

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
from MatrixMusic import (Apple, Resso, Spotify, Telegram, YouTube, app)
from MatrixMusic import app
from random import  choice, randint

                
@app.on_message(
    command(["سورس","السورس"])
    
)
async def huhh(client: Client, message: Message):
    await message.reply_video(
        video=f"https://t.me/HE_CJB/2",
        caption=f"𝐖𝐞𝐥𝐨𝐦𝐞 𝐓𝐨 𝐒𝐨𝐮𝐫𝐜𝐞 ĆJ 𝐌𝐮𝐬𝐢𝐜",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝐆𝐑𝐎𝐔𝐏", url=f"https://t.me/PO_UV"), 
                 InlineKeyboardButton(
                   " 𝐒𝐎𝐔𝐑𝐂𝐄",       url=f"https://t.me/CG_G11"), 
                 
             ],[ 
            InlineKeyboardButton(
                        "『 َِٓ𝗘َِ𝟯َِٓ𝗗َِٓ𝗔َِٓ𝗠َِٓ ℡ 』 ☬ ➥ مٓمٓــۄل ||", url=f"https://t.me/DAD_E3DAM"), 
                   
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
    await message.reply_photo(photo,       caption=f"معلومات مطور السورس\n\n‍ ¦dev :{name}\n\n ¦user :@{usr.username}\n\n ¦id :`{usr.id}`\n\n ¦bio :{usr.bio}\n\𝐒𝐎𝐔𝐑𝐂𝐄 CJ", 
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
    command(["اعدام" , "إعدام","مطور السورس"])
    
    
)
async def yas(client, message):
    usr = await client.get_chat("DAD_E3DAM")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"مــعلومـات مــطور الـسـورس \n\n dev :{name}\n\n user :@{usr.username}\n\n id :`{usr.id}`\n\n boi :{usr.bio}\n\n 𝐒𝐎𝐔𝐑𝐂𝐄 CJ", 
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
    command(["مبرمج السورس" , "اعدام","محمد"])
    
    
)
async def yas(client, message):
    usr = await client.get_chat("Pep_s_e")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"مــعلـومـات مــبرمـج الـسـورس  \n\n dev :{name}\n\n user :@{usr.username}\n\n id :`{usr.id}`\n\n bio :{usr.bio}\n\n𝐒𝐎𝐔𝐑𝐂𝐄 CJ", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
                  )
