#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>╔════════════⦿\n├⋗ Oᴡɴᴇʀ : <a href='tg://user?id={5205293211}'>ησzєℓ ѕιℓνα #𝕲𝖔𝖉𝕺𝖋𝕮𝖗𝖆𝖈𝖐𝖊𝖗𝖘 </a>\n├⋗ ᴄʀᴇᴀᴛᴏʀ : <a href='tg://user?id={5205293211}'>ησzєℓ ѕιℓνα #𝕲𝖔𝖉𝕺𝖋𝕮𝖗𝖆𝖈𝖐𝖊𝖗 </a>\n├⋗ ʟᴀɴɢᴜᴀɢᴇ : <code>Python3</code>\n├⋗ ʟɪʙʀᴀʀʏ : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a>\n├⋗ ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ : <a href=https://t.me/Its_Tartaglia_Childe>File Store Bot</a>\n├⋗ Main Channel : <a href=https://t.me/Anime_X_Hunters>Anime Hunters</a>\n├⋗ Support Group : https://t.me/Hunters_Discussion\n╚═════════════════⦿</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
