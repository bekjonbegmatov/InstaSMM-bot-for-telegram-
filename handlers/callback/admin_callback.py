from aiogram import Bot , F
from aiogram.types import CallbackQuery
from aiogram import Router

from database.data import Chanals
from keyboards.admin_buttons import active_chanal , chanal_delete_inline_button

router = Router()

@router.callback_query(F.data.startswith('delete_chanal_'))
async def deactive_chanal(call:CallbackQuery , bot:Bot):
    idv = call.data.split('_')[2]
    C = Chanals()
    try:
        message = call.message
        C.change_active(is_active=False, idv=int(idv))
        info = C.get_chanal_with_id(idv=int(idv))
        await bot.edit_message_text(
            message_id=message.message_id,
            chat_id=call.message.chat.id,
            text=f"✅ SUCCESS ✅ ACTIVE -> False\n{info}",
            reply_markup=active_chanal(idt=int(idv))
        )
        
    except:
        await bot.send_message(chat_id=call.message.chat.id , text='Karoche qanaqadur hatolik')
    # await bot.send_message(chat_id=call.message.chat.id , text=id)

@router.callback_query(F.data.startswith('activate_chanal_'))
async def activate_chanal(call:CallbackQuery , bot:Bot):
    idv = call.data.split('_')[2]
    C = Chanals()
    try:
        message = call.message
        C.change_active(is_active=True, idv=int(idv))
        info = C.get_chanal_with_id(idv=int(idv))
        await bot.edit_message_text(
            message_id=message.message_id,
            chat_id=call.message.chat.id,
            text=f"✅ SUCCESS ✅ ACTIVE -> True\n{info}",
            reply_markup=chanal_delete_inline_button(idt=int(idv))
        )
        
    except:
        await bot.send_message(chat_id=call.message.chat.id , text='Karoche qanaqadur hatolik')
        
@router.callback_query(F.data.startswith('get_chanal_info_'))
async def get_chanal_info(call:CallbackQuery , bot:Bot):
    idv = call.data.split('_')[3]
    C = Chanals()
    try:
        message = call.message
        info = C.get_chanal_with_id(idv=int(idv))
        if int(info[-1]) == 1 :
            await bot.edit_message_text(
                message_id=message.message_id,
                chat_id=call.message.chat.id,
                text=f"✅ SUCCESS ✅\n{info}",
                reply_markup=chanal_delete_inline_button(idt=int(idv))
            )
        else :
            await bot.edit_message_text(
                message_id=message.message_id,
                chat_id=call.message.chat.id,
                text=f"✅ SUCCESS ✅ ACTIVE -> False\n{info}",
                reply_markup=active_chanal(idt=int(idv))
            )
    except : 
        await bot.send_message(chat_id=call.message.chat.id , text='Karoche qanaqadur hatolik')