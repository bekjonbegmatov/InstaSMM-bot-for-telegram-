from aiogram import Bot, F, Router
from aiogram.types import CallbackQuery
from aiogram.enums.parse_mode import ParseMode

from keyboards.pay_button import pay_list_button

router = Router()

@router.callback_query(F.data == 'top_up_balance')
async def top_up_methods(call:CallbackQuery):
    text = '<b>💳 Hisobni toldirish</b>\n\n<code>❗️ Hisobingizni boshqa summaga to\'ldirmoqchi bulsangiz yoki hatolik toptingiz mi</code> @smm_bot_menejer <code>ga murojat qiling</code>\nKerakli summani tanlang ⤵'
    await call.message.bot.edit_message_text(
        text=text, 
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        reply_markup=pay_list_button(user_id=int(call.from_user.id)),
        parse_mode=ParseMode.HTML
        )
    

