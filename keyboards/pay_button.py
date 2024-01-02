from aiogram.utils.keyboard import InlineKeyboardBuilder
from database.data import Pay


def pay_list_button(user_id:int):
    pay_methods = Pay().get_all_pay_amounts()
    builder = InlineKeyboardBuilder()
    for pay in pay_methods:
        builder.button(text=str(pay[1])+'₽', url=pay[2])
    builder.button(text='💸 Tekshirish 💸', callback_data=f'check_pay_userid_{user_id}' )
    builder.button(text="⬅️ Ortga", callback_data="back_to_menu")
    builder.adjust(3,3,3,1,1)
    return builder.as_markup()

