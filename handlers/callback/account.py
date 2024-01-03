from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.enums.parse_mode import ParseMode
from database.data import User
from keyboards.account_button import account_button
from handlers.callback.create_order import router as order_router

router = Router()


@router.callback_query(F.data == "get_my_account")
async def get_user_account(call: CallbackQuery):
    user_id = call.from_user.id
    info = User().get_user_with_user_id(user_id=int(user_id))
    account = f"""<b>💼 Akkaunt</b>
├<b>ID :</b> <code>{user_id}</code>
├<b>Nik :</b> <code>{info['username']}</code>
└<b>Hisob (Balans) :</b> <code>{info['balance']}₽</code>

Kerakli bulimni tanlsng ⤵:
    """
    await call.message.bot.edit_message_text(
        text=account,
        chat_id=call.message.chat.id,
        message_id=call.message.message_id,
        reply_markup=account_button(user_id=call.from_user.id),
        parse_mode=ParseMode.HTML,
    )

@router.callback_query(F.data.startswith('referal_userid_'))
async def get_referal_link(call:CallbackQuery):
    user_id = call.data.split('_')[2]
    bot = await call.message.bot.get_me()
    link = f"""Bu ssilkani do\'stingizga yuboring 👥 :

📎 https://t.me/{bot.username}?start={user_id}

Qachonki do\'stingiz botga kirib akaunt ochsa sizning hisobingizga 10₽ qushiladi ❤️

🚨Ushbu ssilka uzingizga va bot foydalanuvchilarida ishlamaydi🚨
Faqatgina yangi foydalanuvchilar uchun ⚡️
"""
    await call.message.answer(text=link)

@router.callback_query(F.data.startswith('history_pay_userid_'))
async def history_of_orders(call:CallbackQuery):
    user_id = int(call.data.split('_')[3])
    history = User().get_history(user_id=user_id)
    await call.message.answer(text=history)

# user_pay_history_txport_to_array
@router.callback_query(F.data.startswith('history_topup_userid_'))
async def hiytory_of_pay(call:CallbackQuery):
    # print(te)
    user_id = int(call.data.split('_')[3])
    history = User().user_pay_history_txport_to_array(user_id=user_id)
    if len(history) == 0 :
        await call.message.answer(text='Siz hali balans to\'dirmagan siz !')
    else:
        await call.message.answer(text=f'💳 Balans tarihi\n{history}') 

router.include_router(order_router)