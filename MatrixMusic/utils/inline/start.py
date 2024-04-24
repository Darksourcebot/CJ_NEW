from pyrogram.types import InlineKeyboardButton

import config
from MatrixMusic import app

def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="اضغط لاضافتي لمجموعتك✅", url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text="𝙶𝚁𝙾̀𝚄𝙿", url= "https://t.me/PO_UV"),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="اضغط لاضافتي لمجموعتك✅",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        
        [
            InlineKeyboardButton(text="مطور البوت", user_id=config.OWNER_ID),
            InlineKeyboardButton(text="ᏀᎡΌႮᏢ", url=f"https://t.me/PO_UV"), 
        ],
        [
            
            InlineKeyboardButton(text="𝙎𝙊𝙐𝙍𝘾𝙀 𝗖𝗝", url=f"https://t.me/CG_G11") , 
        ],
    ]
    return buttons
