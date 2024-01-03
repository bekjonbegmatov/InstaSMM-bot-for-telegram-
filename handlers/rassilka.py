from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.context import FSMContext


from database.data import User, Admin
from utils.states import Rassilka

router = Router()

@router.message(Command('newsletter'))
async def newsletter_command(message:Message , state:FSMContext):
    if Admin().is_admin(user_id=message.from_user.id) != 'user':
        await state.set_state(Rassilka.image)
        await message.answer(text='Yahshi menga rasim junating')

@router.message(Rassilka.image, F.photo)
async def get_photo(message:Message , state:FSMContext):
    file_id = message.photo[-1].file_id
    await state.update_data(image=file_id)
    await state.set_state(Rassilka.desctiption)
    await message.answer(text='✅ Qabul qilindi ✅\nIndi matnni yuboring HTML teglaridan foydalanishingiz mumkun')

@router.message(Rassilka.image, ~F.photo)
async def not_photo(message:Message , state:FSMContext):
    await message.answer(text='Avval rasim tashlang')

@router.message(Rassilka.desctiption)
async def get_desctiption(message:Message, state:FSMContext):
    if len(message.text) <= 5 :
        await message.answer(text='Minimum 5 ta harif')
    else:
        data = await state.get_data()
        foto = data['image']
        await state.update_data(desctiption=message.text)
        await message.answer_photo(photo=foto, caption=message.text, parse_mode=ParseMode.HTML)
        await state.set_state(Rassilka.confirm)
        await message.answer(text='Junatishni tastiqlaysiz mi ? ha yoki yoz ')

@router.message(Rassilka.confirm)
async def confirm_or_not(message:Message, state:FSMContext):
    m = message.text
    m = m.lower() 
    if m == 'ha':
        data = await state.get_data()
        image = data['image']
        desctiption = data['desctiption']
        await state.clear()
        all_users = User().get_all_users()
        active_user = 0
        bloken_user = 0
        for user in all_users:
            try:
                await message.bot.send_photo(chat_id=user[2] , photo=image, caption=desctiption, parse_mode=ParseMode.HTML)
                active_user += 1 
            except:
                bloken_user += 1

        await message.reply(text=f'✅ Habar Hammaga Yuborildi ✅\nStatistika :\nActiv foydalanuvchilar : {active_user}\nBlokka tiqqanlar : {bloken_user}\nJami : {active_user+bloken_user}')
    elif m == 'yoq':
        pass
    else:
        await message.answer(text='Tastiqlaysiz mi ? Ha yoki yoq')