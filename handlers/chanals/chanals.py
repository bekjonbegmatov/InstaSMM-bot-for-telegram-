from aiogram import F , Router
from aiogram.types import Message , CallbackQuery
from database.data import Chanals
from aiogram.utils.keyboard import InlineKeyboardBuilder , InlineKeyboardButton
from handlers.servises_command import all_uslugi_command
router = Router()


async def get_not_sub_chanals(user_id , bot):
    not_sub_ch = []
    chanals = Chanals()
    for chanal in chanals.get_all_chanals():
        if chanal[4] == True or chanal[4] == 1:
            status = await bot.get_chat_member(f'@{chanal[1]}' , user_id)
            if status.status == 'left' : 
                not_sub_ch.append(chanal[1])
    return not_sub_ch

async def subscribe_button(user_id,bot):
    builder = InlineKeyboardBuilder()
    chalals = Chanals()
    not_sub = await get_not_sub_chanals(user_id=user_id,bot=bot)
    i = 1
    for ch in not_sub:
        builder.add(InlineKeyboardButton(
        text=f"Kanal {i}",
        url=f'https://t.me/{ch}'))
        i += 1
    builder.add(InlineKeyboardButton(
        text=" ✅ Tastoqlash ✅ ",
        callback_data="check_subscribe_to_chanals")
    )
    builder.adjust(1)
    return builder.as_markup()

async def check_subckribe(user_id , bot):
    chanals = Chanals()
    not_sub_chan = []
    for chanal in chanals.get_all_chanals():
        if chanal[4] == True or chanal[4] == 1:
            status = await bot.get_chat_member(f'@{chanal[1]}' , user_id)
            if status.status == 'left' : not_sub_chan.append(chanal[1])
    if len(not_sub_chan) == 0 : return True
    return False

# @router.callback_query(F.data == 'check_subscribe_to_chanals' )
@router.callback_query(F.data == "check_subscribe_to_chanals")
async def check_podpisku(call: CallbackQuery):
    await call.message.bot.delete_message(chat_id=call.message.chat.id , message_id=call.message.message_id)
    if await check_subckribe(call.from_user.id , call.message.bot) : 
        await call.message.bot.send_message(chat_id=call.from_user.id , text=' ✅ Botdan Foydalanishingiz mumkun ✅ /menu')
    else : await call.message.bot.send_message(chat_id=call.from_user.id , text=' 🆘 HAMMA KANALLARGA OBUNA BULING 🆘 ' , reply_markup=await subscribe_button(user_id=callback.from_user.id))

