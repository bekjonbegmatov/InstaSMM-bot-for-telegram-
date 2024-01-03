from aiogram import Router, F 
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove 
from aiogram.enums.parse_mode import ParseMode
from handlers.servises_command import all_uslugi_command
from database.data import *

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message, command:Command):
    bot = message.bot
    info = await bot.get_me()

    # command.args
    # Checking usern in database and add 
    user = User()
    us = user.check_user_if_not_add(
        username=message.from_user.username, 
        first_name=message.from_user.first_name, 
        second_name=message.from_user.last_name, 
        chat_id=message.chat.id, 
        user_id=message.from_user.id, 
        balance='20')
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
        await message.answer(text=msg)
        await all_uslugi_command(message=message)

    else :
        await message.answer_sticker(sticker='CAACAgIAAxkBAAEKPlZk-eLKS3tUCG_aRGY1wZjJY8tnxAACxgEAAhZCawpKI9T0ydt5RzAE')
        if command.args :
            try:
                ref_id = int(command.args)
                usr = User().get_user_with_user_id(user_id=ref_id)
                t_balans = int(usr['balance']) + 10
                User().update_balance(user_id=ref_id,new_balance=t_balans)
                User().create_user_pay_history(user_id=ref_id, amount='10', description='Referal ssilka orqali')
                await bot.send_message(chat_id=ref_id, text='🥳 Sizning do\'stingiz taklifni qabul qildi 🥳\nHisobingizga 10₽ qushildi !')
            except:
                pass
        msg = f'Assalomu alykum {message.from_user.first_name}!\nMen {info.first_name}.\nMen sizga Instagramda rivojlanishingizga yordam beraman!'
        await message.answer(text+'\n<b>Ilk foydalanuvchilar uchun bonus : 20₽</b>' , parse_mode=ParseMode.HTML)
        await message.answer('🎁 Bizning bot qanday ishlashini tekshiring, balansingiz 20₽ ga to\'ldirildi.')
        # Send info to admins 
        await all_uslugi_command(message=message)
        admin = Admin()
        admins = admin.get_all_admins()
        for ad in admins:
            try:
                await bot.send_message(chat_id=ad[2], text=f"Yangi foydalanuvchi qushildi\nUsername -> @{message.from_user.username}\nFirst name -> {message.from_user.first_name}\nLast name -> {message.from_user.last_name}")
            except:
                pass

@router.message(Command("help"))
async def help_command(message: Message):
    await message.answer(text='Meneger @smm_bot_menejer')

# /invite 
@router.message(Command("invite"))
async def intive_command(message: Message):
    bot = await message.bot.get_me()
    link = f"""Bu ssilkani do\'stingizga yuboring 👥 :

📎 https://t.me/{bot.username}?start={message.from_user.id}

Qachonki do\'stingiz botga kirib akaunt ochsa sizning hisobingizga 10₽ qushiladi ❤️

🚨Ushbu ssilka uzingizga va bot foydalanuvchilarida ishlamaydi🚨
Faqatgina yangi foydalanuvchilar uchun ⚡️
"""
    # await call.message.answer(text=link)
    await message.answer(text=link)

@router.message(Command("menu"))
async def help_command(message: Message):
    await all_uslugi_command(message=message)

terms = """Instagram SMM botidan foydalanish shartlari:

1. <b>Litsenziya va huquqlar:</b>
    1.1 Foydalanuvchi ushbu shartnoma shartlariga muvofiq Instagram SMM botidan foydalanish uchun litsenziya oladi.
    1.2 Instagram SMM bot bilan bog'liq barcha intellektual mulk yetkazib beruvchining mulki bo'lib qoladi.

2. <b>Xizmatlardan foydalanish:</b>
    2.1 Foydalanuvchi Instagram SMM botidan faqat qonuniy maqsadlarda foydalanishga va Instagramdan foydalanish bo‘yicha barcha amaldagi qonun va qoidalarga rioya qilishga rozi.
    2.2 Instagram SMM botidan ruxsatsiz kirish, boshqa odamlarning akkauntlariga aralashish va boshqa noqonuniy harakatlar uchun foydalanish taqiqlanadi.

3. <b>Toʻlovlar:</b>
    3.1 Foydalanuvchi Instagram SMM boti xizmatlari uchun belgilangan tariflarga muvofiq va o‘zi tanlagan to‘lov tizimiga muvofiq to‘lash majburiyatini oladi.
    3.2 Yetkazib beruvchi foydalanuvchilarni oldindan xabardor qilgan holda tariflar va to'lov shartlarini o'zgartirish huquqini o'zida saqlab qoladi.

    3.3 To‘lov o‘z vaqtida amalga oshirilmagan taqdirda yetkazib beruvchi Instagram SMM bot xizmatlarini ko‘rsatishni vaqtincha to‘xtatib qo‘yish huquqini o‘zida saqlab qoladi.

4. <b>Ma'suliyat:</b>
    4.1 Provayder foydalanuvchi tomonidan Instagram SMM botidan noto'g'ri yoki noqonuniy foydalanish natijasida yuzaga keladigan har qanday oqibatlar uchun javobgar emas.
    4.2 Foydalanuvchi o'z hisob ma'lumotlarining xavfsizligi uchun javobgardir va uning akkauntiga ruxsatsiz kirishning oldini olish uchun barcha zarur choralarni ko'rish majburiyatini oladi.

    4.3 Provayder Instagram SMM botning uzluksiz ishlashini kafolatlamaydi va texnik nosozliklar yoki uchinchi shaxslarning harakatlari tufayli uning faoliyatidagi vaqtinchalik uzilishlar uchun javobgar emas.

5. <b>Foydalanishni to'xtatish:</b>
    5.1 Agar foydalanuvchi ushbu shartnoma shartlarini buzsa, Provayder Instagram SMM bot xizmatlarini ko'rsatishni to'xtatib turish yoki to'xtatish huquqini o'zida saqlab qoladi.
    5.2 Instagram SMM botdan foydalanish tugatilgan taqdirda foydalanuvchi dasturdan har qanday foydalanishni to‘xtatish va uni qurilmalardan olib tashlash majburiyatini oladi.

Ushbu shartnoma shartlarini qabul qilib, foydalanuvchi yuqoridagi shartlarga roziligini tasdiqlaydi va Instagram SMM botdan foydalanishda ularga rioya qilish majburiyatini oladi."""

@router.message(Command("terms"))
async def help_command(message: Message):

    await message.answer(text=terms, parse_mode=ParseMode.HTML)