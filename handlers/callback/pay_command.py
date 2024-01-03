from aiogram import Bot, F, Router
from aiogram.types import CallbackQuery
from aiogram.enums.parse_mode import ParseMode

from keyboards.pay_button import pay_list_button
from database.data import Admin

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
    
@router.callback_query(F.data.startswith('check_pay_userid_'))
async def check_pay_result(call:CallbackQuery):
    text = '✅ Qabul qilindi ✅\nMenejerga yuborildi (10-15 minut) ichida pul utadi'
    await call.message.answer(text=text)
    us_id = call.data.split('_')[3]
    admin = Admin().get_admin_with_role(role='super_admin')
    for adm in admin:
        await call.message.bot.send_message(chat_id=adm[2] , text=f'Pulni tastiqlang\nuser_id : {us_id}\n\n/add_pay summa user_id\n/error_pay user_id')
    # await call.message.answer(text='Qabul ')
