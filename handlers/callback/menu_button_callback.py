from aiogram import Bot , Router , F
from aiogram.types import CallbackQuery
from keyboards.servise_button import followers_button , menu_button, delete_button
from aiogram.enums.parse_mode import ParseMode

from api.manage_service import ManageBot

router = Router()

@router.callback_query(F.data == 'get_followers')
async def get_folower(call:CallbackQuery):
    text = (
        '<b>📝 Yangi buyurtma:</b>\n'
        '├<b>Platforma:</b> <code>Instagram</code>\n'
        '└<b>Hizmat:</b> <code>Obunachilar</code>\n\n'
        'Narhlar <b>100 dona</b> uchun\n'
        'Klaviaturadan kerakli bulimni tanlang ⤵'
    )
    message_id = call.message.message_id
    await call.message.bot.edit_message_text(text=text, chat_id=call.message.chat.id , message_id=message_id , reply_markup=followers_button(category='1') , parse_mode=ParseMode.HTML)
    # await call.message.answer(text=text ,reply_markup=followers_button(), parse_mode=ParseMode.HTML)

@router.callback_query(F.data == 'get_likes')
async def get_likesa(call:CallbackQuery):
    text = (
        '<b>📝 Yangi buyurtma:</b>\n'
        '├<b>Platforma:</b> <code>Instagram</code>\n'
        '└<b>Hizmat:</b> <code>Layklar</code>\n\n'
        'Narhlar <b>100 dona</b> uchun\n'
        'Klaviaturadan kerakli bulimni tanlang ⤵'
    )
    message_id = call.message.message_id
    await call.message.bot.edit_message_text(text=text, chat_id=call.message.chat.id , message_id=message_id , reply_markup=followers_button(category='2') , parse_mode=ParseMode.HTML)


@router.callback_query(F.data == 'get_views_video')
async def get_views_videoa(call:CallbackQuery):
    text = (
        '<b>📝 Yangi buyurtma:</b>\n'
        '├<b>Platforma:</b> <code>Instagram</code>\n'
        '└<b>Hizmat:</b> <code>Prasmotr video</code>\n\n'
        'Narhlar <b>100 dona</b> uchun\n'
        '<b>🚨 MINIMUM 100 dona 🚨</b>\n'
        'Klaviaturadan kerakli bulimni tanlang ⤵'
    )
    message_id = call.message.message_id
    await call.message.bot.edit_message_text(text=text, chat_id=call.message.chat.id , message_id=message_id , reply_markup=followers_button(category='3') , parse_mode=ParseMode.HTML)

@router.callback_query(F.data == 'get_saves')
async def get_savesa(call:CallbackQuery):
    text = (
        '<b>📝 Yangi buyurtma:</b>\n'
        '├<b>Platforma:</b> <code>Instagram</code>\n'
        '└<b>Hizmat:</b> <code>Sohraneniya</code>\n\n'
        'Narhlar <b>100 dona</b> uchun\n'
        'Klaviaturadan kerakli bulimni tanlang ⤵'
    )
    message_id = call.message.message_id
    await call.message.bot.edit_message_text(text=text, chat_id=call.message.chat.id , message_id=message_id , reply_markup=followers_button(category='6') , parse_mode=ParseMode.HTML)

@router.callback_query(F.data == 'get_ohvat')
async def get_ohvata(call:CallbackQuery):
    text = (
        '<b>📝 Yangi buyurtma:</b>\n'
        '├<b>Platforma:</b> <code>Instagram</code>\n'
        '└<b>Hizmat:</b> <code>Ohvat + Top </code>\n\n'
        'Narhlar <b>100 dona</b> uchun\n'
        'Klaviaturadan kerakli bulimni tanlang ⤵'
    )
    message_id = call.message.message_id
    await call.message.bot.edit_message_text(text=text, chat_id=call.message.chat.id , message_id=message_id , reply_markup=followers_button(category='12') , parse_mode=ParseMode.HTML)
# @get_likes

@router.callback_query(F.data == 'back_to_menu')
async def back_to_menu(call:CallbackQuery):
    text = (
        '<b>Доступные команды 🧾 :</b>\n'
        '/menu — 🏠 Asosy menyu\n'
        '/invite — 👥 Dustlarni taklif qilish\n'
        '/help   — 👤 Poderjka\n'
        '/terms — 🚨 Foydalanish qoidalari \n \n'
        '<b>Uzingizga kerak bulgan bulimni tanlang ⤵</b>'
    )
    message_id = call.message.message_id
    await call.message.bot.edit_message_text(chat_id=call.message.chat.id, text=text, message_id=message_id,  parse_mode=ParseMode.HTML, reply_markup=menu_button(user_id=call.from_user.id))


@router.callback_query(F.data == 'delete_message')
async def delete_message(call:CallbackQuery):
    await call.message.delete()