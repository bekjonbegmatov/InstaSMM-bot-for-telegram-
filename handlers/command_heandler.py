from aiogram import Router, F 
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove

from database.data import *

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    bot = message.bot
    info = await bot.get_me()

    # Checking usern in database and add 
    user = User()
    us = user.check_user_if_not_add(
        username=message.from_user.username, 
        first_name=message.from_user.first_name, 
        second_name=message.from_user.last_name, 
        chat_id=message.chat.id, 
        user_id=message.from_user.id, 
        balance='50')
    if us :
        await message.answer_sticker(sticker='CAACAgIAAxkBAAEKPlhk-eL1_yehX1XkfY7ij6piNAqDSwACywEAAhZCawqjQZ8C-a857jAE')
        msg = f'Assalomu alykum {message.from_user.first_name}, men sizni yana kurganimdan hursand man !\nMen {info.first_name}.\nMen sizga Instagramda rivojlanishingizga yordam beraman!'
        await message.answer(msg)
    else :
        await message.answer_sticker(sticker='CAACAgIAAxkBAAEKPlZk-eLKS3tUCG_aRGY1wZjJY8tnxAACxgEAAhZCawpKI9T0ydt5RzAE')
        msg = f'Assalomu alykum {message.from_user.first_name}!\nMen {info.first_name}.\nMen sizga Instagramda rivojlanishingizga yordam beraman!'
        await message.answer(msg)

        # Send info to admins 
        admin = Admin()
        admins = admin.get_all_admins()
        for ad in admins:
            try:
                await bot.send_message(chat_id=ad[2], text=f"Yangi foydalanuvchi qushildi\nUsername -> @{message.from_user.username}\nFirst name -> {message.from_user.first_name}\nLast name -> {message.from_user.last_name}")
            except:
                pass

@router.message(Command("help"))
async def help_command(message: Message):
    pass
