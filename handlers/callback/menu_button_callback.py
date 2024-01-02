from aiogram import Bot , Router , F
from aiogram.types import CallbackQuery
from keyboards.servise_button import followers_button , menu_button
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
    await call.message.bot.edit_message_text(text=text, chat_id=call.message.chat.id , message_id=message_id , reply_markup=followers_button() , parse_mode=ParseMode.HTML)
    # await call.message.answer(text=text ,reply_markup=followers_button(), parse_mode=ParseMode.HTML)

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

@router.callback_query(F.data.startswith('get_fol_'))
async def get_more_info_about_folow_item(call:CallbackQuery):
    idv = call.data.split('_')[2]
    info = ManageBot().get_from_id(idv=idv)

    # print(info[0]['name'])
    info = info[0]
    name = info['name']
    price = info['cost']
    tmin = info['min']
    tmax = info['max']
    des = info['description']
    # text = f'<b>{name}</b>\n├<b>Narhi :</b> <code>{price}</code>\n├<b>Minimum :</b> <code>{tmin}</code>\n└<b>Maximum :</b> <code>{tmax}</code>\n\n🛡Kafolat ⭐️ Yuqori sifat ⚡️ Tez boshlash\n\n<b>Tezlik :</b> soatiga 2000\n<b>Boshlanish vaqti:</b> 15 min.\n{des}\n🛡Ushbu xizmat 30 kunlik kafolat bilan taqdim etiladi. kamayish holatlarida qayta tiklash (qo\'llab-quvvatlash xizmatiga yozing)'
    text = (
        f'<b>{name}</b>\n'
        f'├<b>Narhi :</b> <code>{price}</code>\n'
        f'├<b>Minimum :</b> <code>{tmin}</code>\n'
        f'└<b>Maximum :</b> <code>{tmax}</code>\n\n'
        f'🛡Kafolat ⭐️ Yuqori sifat ⚡️ Tez boshlash\n\n'
        f'<b>Tezlik :</b> soatiga 2000\n'
        f'<b>Boshlanish vaqti:</b> 15 min.\n{des}\n\n'
        f'🛡Ushbu xizmat 30 kunlik kafolat bilan taqdim etiladi.'
        f'Kamayish holatlarida qayta tiklash <b>(qo\'llab-quvvatlash xizmatiga yozing)</b>'
    )
    await call.message.bot.edit_message_text(text=text , chat_id=call.message.chat.id, message_id=call.message.message_id , parse_mode=ParseMode.HTML , reply_markup=None)