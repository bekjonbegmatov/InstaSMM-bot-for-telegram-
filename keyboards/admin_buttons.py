from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types

from database.data import Chanals

def chanal_delete_inline_button(idt:int):
    builder = InlineKeyboardBuilder()
    builder.button(text='⛔️ Kanalni uchirish ⛔️' , callback_data=f'delete_chanal_{idt}')
    return builder.as_markup()

def active_chanal(idt:int):
    bulder = InlineKeyboardBuilder()
    bulder.button(text='✅ Ishga tushurish ✅' , callback_data=f'activate_chanal_{idt}')
    return bulder.as_markup()

def chanals_list_buton():
    bulder = InlineKeyboardBuilder()
    C = Chanals()
    i = 1
    for chanal in C.get_all_chanals():
        bulder.button(
            text=f'{i}. {chanal[1]}',
            callback_data=f'get_chanal_info_{chanal[0]}'
        )
        i += 1
    bulder.adjust(1)
    return bulder.as_markup()

