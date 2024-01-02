from aiogram import Router, F 
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove 
from aiogram.enums.parse_mode import ParseMode

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
        balance='30')
    text = f"""
        Salom! {message.from_user.first_name} 🌟 {info.first_name} ga xush kelibsiz - Instagram SMM-dagi ishonchli yordamchingiz! 🚀

🤖 Biz sizning Instagram tajribangizni noyob qilish uchun shu yerdamiz! Bizning botimiz SMM xizmatlari uchun eng maqbul narxlarni taqdim etadi - faqat bizning foydalanuvchilarimiz uchun. 💰

👉 Nima uchun {info.first_name} Instagram uchun eng yaxshi tanlovdir:

✨ Tejamkorlik: kamroq evaziga ko'proq narsani oling. SMM xizmatlari uchun narxlarimiz beqiyos!

🤝 Ishonch: Hisobingiz xavfsizligiga ishonch hosil qiling. Ishonchingizni qadrlaymiz.

🎯 Maqsadli auditoriya: Maksimal samaradorlik uchun maqsadli auditoriyani o'rnatamiz.

🔒 Maxfiylik: Sizning ma'lumotlaringiz sizning shaxsiy sohangizdir. Biz mutlaq maxfiylikni ta'minlaymiz.

📈 O'sishga ta'sir qiling: bizning yordamimiz bilan onlayn vazningizni oshiring. Yulduzga aylaning!

🚀 Tez boshlash: Bugundan boshlang va ertaga farqni his qiling!

        """
    if us :
        await message.answer_sticker(sticker='CAACAgIAAxkBAAEKPlhk-eL1_yehX1XkfY7ij6piNAqDSwACywEAAhZCawqjQZ8C-a857jAE')
        msg = f'Assalomu alykum {message.from_user.first_name}, men sizni yana kurganimdan hursand man !\nMen {info.first_name}.\nMen sizga Instagramda rivojlanishingizga yordam beraman!'
        await message.answer(text+'\nIlk foydalanuvchilar uchun bonus : 30₽')
        await message.answer('🎁 Bizning bot qanday ishlashini tekshiring, balansingiz 20₽ ga to\'ldirildi.')
    else :
        await message.answer_sticker(sticker='CAACAgIAAxkBAAEKPlZk-eLKS3tUCG_aRGY1wZjJY8tnxAACxgEAAhZCawpKI9T0ydt5RzAE')
        msg = f'Assalomu alykum {message.from_user.first_name}!\nMen {info.first_name}.\nMen sizga Instagramda rivojlanishingizga yordam beraman!'
        await message.answer(text+'\n<b>Ilk foydalanuvchilar uchun bonus : 30₽</b>' , parse_mode=ParseMode.HTML)
        await message.answer('🎁 Bizning bot qanday ishlashini tekshiring, balansingiz 20₽ ga to\'ldirildi.')
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
