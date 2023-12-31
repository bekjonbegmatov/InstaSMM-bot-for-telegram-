from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types
from handlers.admin_commands import off_chanal_command

def chanal_delete_inline_button(idt:int):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text='⛔️ Kanalni uchirish ⛔️',
        callback_data=off_chanal_command(
            action = 'chanal_off',
            value = idt
        )
    ))