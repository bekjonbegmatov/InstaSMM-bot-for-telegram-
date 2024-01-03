from aiogram.utils.keyboard import InlineKeyboardBuilder

def account_button(user_id:int):
    builder = InlineKeyboardBuilder()
    builder.button(text='📎 Referal ssilka' , callback_data=f'referal_userid_{user_id}')
    builder.button(text='🧾 Buyurtmalar tarihi', callback_data=f'history_pay_userid_{user_id}')
    builder.button(text='💳 Balans tarihi', callback_data=f'history_topup_userid_{user_id}')
    builder.button(text='⬅️ Ortga' , callback_data='back_to_menu')
    builder.adjust(1)
    return builder.as_markup()


