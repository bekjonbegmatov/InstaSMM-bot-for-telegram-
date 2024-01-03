from aiogram import Bot, Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.enums import ParseMode

from keyboards.servise_button import menu_button
from handlers.callback.menu_button_callback import router as call_router
from handlers.callback.pay_command import router as pay_router
from handlers.callback.account import router as account_router
from database.data import Admin , User
router = Router()

@router.message(Command('service'))
async def all_uslugi_command(message: Message):
    text = (
        '<b>Доступные команды 🧾 :</b>\n'
        '/menu — 🏠 Asosy menyu\n'
        '/invite — 👥 Dustlarni taklif qilish\n'
        '/help   — 👤 Poderjka\n'
        '/terms — 🚨 Foydalanish qoidalari \n \n'
        '<b>Uzingizga kerak bulgan bulimni tanlang ⤵</b>'
    )
    await message.answer(text=text, parse_mode=ParseMode.HTML, reply_markup=menu_button(user_id=message.from_user.id))

@router.message(Command('add_pay'))
async def add_pay_command(message:Message):
    if Admin().is_admin(user_id=message.from_user.id):
        try:  
            U = User()
            text = message.text
            top_up = int(text.split()[1])
            user_id = int(text.split()[2])
            user = U.get_user_with_user_id(user_id=user_id)
            User().create_user_pay_history(user_id=user_id, amount=str(top_up), description='Karta orqali')
            u_balanse = int(user['balance'])
            new_balance = top_up + u_balanse
            if U.update_balance(user_id=user_id, new_balance=str(new_balance)):
                await message.bot.send_message(chat_id=user_id, text=f'✅ Hisobingiz {top_up}₽ ga tuldi ✅')
                await message.answer(text=f'User : {user_id} , hizsobi {top_up} rublga toldi !')
        except:
            await message.reply(text='qanaqadur hatolik')

@router.message(Command('error_pay'))
async def error_py_command(message:Message):
    if Admin().is_admin(user_id=message.from_user.id):
        try:
            text = message.text
            user_id = int(text.split()[1])
            await message.bot.send_message(chat_id=user_id, text=f'⛔️ Menejer hisobni tulganligini tastiqlamadi ⛔️\nAgar hatolik bulsa @smm_bot_menejer ga murojat qiling !')
            await message.answer(text=f'User : {user_id} , movofoqiyatsiz !')
        except:
            await message.reply(text='/error_pay user_id')

router.include_routers(
    call_router,
    pay_router,
    account_router,
)