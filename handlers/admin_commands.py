from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove , FSInputFile


from database.data import *
import re
router = Router()


@router.message(Command("ahelp"))
async def help_command_for_admin(message: Message):
    text = (
        ">>>>>>>>>🅷🅴🅻🅿<<<<<<<<<\n"
        +'\nUsers and Admins 👥\n\n'
        +'/all_users attribute -t -j -m (-t -> file.txt, -j -> file.json, -m -> in message)\n'
        +'/set_role id_admin role (for changing role, roles => [super_admin, admin, moder])\n'
        +'/remove_admin id_admin (Removes admin)\n'
        +'\nChanals 🎥\n\n'
        +'/chanal_add chanal_name final_trafic\n'
        +'/set_ft int:num id_chanal (num => new number of trafic)\n'
        +'/set_active bool id_chanal (bool => 1 = active, 0 = deactive)\n'
        +'/all_chanals attribute -t -j -m (-t -> file.txt, -j -> file.json, -m -> in message)\n'
        +'\nStatistik 📈\n\n'
        +'/statistics (Returns statistics of this bot)\n'
        +'\nNewsletter 🚀\n\n'
        +'/newsletter message (you can use HTML tags)'
    )
    A = Admin()
    if A.is_admin(user_id=message.from_user.id) == 'user':
        pass
    else :
        await message.answer(text=text)

@router.message(Command('all_users'))
async def all_users_command(message:Message):
    A = Admin()
    if A.is_admin(user_id=message.from_user.id) == 'user':
        pass
    else :
        U = User()
        bot = message.bot
        text = message.text
        if text.count('-t') == 1:
            U.extport_to_txt()
            document = FSInputFile(path="/Users/apple/Documents/python/tg_bot/InstaFollowerBot/users.txt", filename='Users.txt')
            await bot.send_document(message.chat.id, document=document, caption='This is a list of bot users')
        elif text.count('-j') == 1:
            U.export_to_json()
            document = FSInputFile(path='/Users/apple/Documents/python/tg_bot/InstaFollowerBot/users.json', filename='Users.json')
            await bot.send_document(chat_id=message.chat.id, document=document , caption='This is a list of bot users in json file')
        elif text.count('-m') == 1:
            txt = U.export_to_array()
            await bot.send_message(chat_id=message.chat.id, text=txt)
        else : await message.reply(text="Pleace select one option -t -j -m (-t -> file.txt, -j -> file.json, -m -> in message)")


