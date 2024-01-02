from aiogram import Bot, Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.enums import ParseMode

from keyboards.servise_button import menu_button
from handlers.callback.menu_button_callback import router as call_router
from handlers.callback.pay_command import router as pay_router
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

router.include_routers(
    call_router,
    pay_router,
) #(call_router)