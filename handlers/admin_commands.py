from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove , FSInputFile


from database.data import *
import re
router = Router()

# Help menu for admins
@router.message(Command("ahelp"))
async def help_command_for_admin(message: Message):
    text = (
        ">>>>>>>>>🅷🅴🅻🅿<<<<<<<<<\n"
        +'\nUsers and Admins 👥\n\n'
        +'/all_users attribute -t -j -m (-t -> file.txt, -j -> file.json, -m -> in message)\n'
        +'/set_role id_admin role (for changing role, roles => [super_admin, admin, moder])\n'
        +"/create_admin id_user role (roles => [super_admin, admin, admin])\n"
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

# Function for getting all users of bot
@router.message(Command('all_users'))
async def all_users_command(message:Message):
    A = Admin()

    # Checking is user admin 
    if A.is_admin(user_id=message.from_user.id) != 'user':
        U = User()
        bot = message.bot
        text = message.text

        # Export data to .text file
        if text.count('-t') == 1:
            U.extport_to_txt()
            document = FSInputFile(path="/Users/apple/Documents/python/tg_bot/InstaFollowerBot/users.txt", filename='Users.txt')
            await bot.send_document(message.chat.id, document=document, caption='This is a list of bot users')

        # Exporting data to .json fele
        elif text.count('-j') == 1:
            U.export_to_json()
            document = FSInputFile(path='/Users/apple/Documents/python/tg_bot/InstaFollowerBot/users.json', filename='Users.json')
            await bot.send_document(chat_id=message.chat.id, document=document , caption='This is a list of bot users in json file')
        
        # Sending data to the chat
        elif text.count('-m') == 1:
            txt = U.export_to_array()
            await bot.send_message(chat_id=message.chat.id, text=txt)
        else : await message.reply(text="Pleace select one option -t -j -m (-t -> file.txt, -j -> file.json, -m -> in message)")

# Function for change role of user
@router.message(Command('set_role'))
async def set_role_admin_command(message:Message):
    bot = message.bot
    A = Admin()
    proverka = A.is_admin(message.from_user.id)

    # Checking is admin is a Super Admin
    if proverka == "super_admin" :
        text = message.text
        text = text.split()

        # Trying a set admin role
        try:
            user_id = text[1]
            new_role = text[2]

            # Checking is corect role 
            if new_role == "super_admin" or new_role == 'admin' or new_role == 'moder':

                # Checking is user_id is correct if ok set admin role
                if A.set_role(user_id=int(user_id) , new_role=new_role) :
                    await message.reply(text=f"✅ SUCCESS ✅\nSet -> {new_role}")
                # If error user_id
                else: await message.reply(text="⛔️ ERROR ⛔️\nPleace write correct data !")

            # if Uncorrect admin role
            else : await message.reply(text='Pleace select correct role (roles => [super_admin, admin, moder])')
        
        # if error
        except :
            await message.reply(text='/set_role id_admin role (for changing role, roles => [super_admin, admin, moder])')

    # If user 
    elif proverka == 'user': pass

    # Is isn't Super admin
    else : await bot.send_message(chat_id=message.chat.id , text="You are not Supper Admin !!!")

# Function for creationg admin
@router.message(Command('create_admin'))
async def create_admin_command(message:Message):
    bot = message.bot
    A = Admin()
    proverka = A.is_admin(message.from_user.id)

    # Cecking is admin is a Seuper admin
    if proverka == "super_admin":
        text = message.text
        text = text.split()

        # Trying create an admin
        try:
            new_admin_id = text[1]
            role = text[2]

            # Cheking is corect role
            if role == "super_admin" or role == 'admin' or role == 'moder':

                # Checking is user_id is correct if ok create admin
                if A.create_admin(new_admin_id=int(new_admin_id), role=role) : await message.reply(text=f"✅ SUCCESS ✅\nUser -> {role}")

                # If error user_id
                else: await message.reply(text="⛔️ ERROR ⛔️\nPleace write correct data !")
            else: await message.reply(text='Pleace use coreact \n/create_admin id_user role (roles => [super_admin, admin, admin])')

        # If error
        except :
            await message.reply(text='/set_role id_admin role (for changing role, roles => [super_admin, admin, moder])')
    
    # If user
    elif proverka == 'user': pass

    # # If isn'nt Supper admin
    else : await message.reply(text="You are not Supper Admin !!!")

@router.message(Command('remove_admin'))
async def remove_admin_command(message:Message):
    A = Admin()
    bot = message.bot
    proverka = A.is_admin(message.from_user.id)
    if proverka == 'super_admin':
        text = message.text
        try:
            admin_id = (text.split())[1]
            if A.remove_admin(user_id=int(admin_id)): await bot.send_message(chat_id=message.chat.id, text=f"✅ SUCCESS ✅\nAdmin -> User")
            else : await message.reply(text="⛔️ ERROR ⛔️\nPleace write correct data !")
        except: await message.reply(text='/remove_admin id_admin (Removes admin)')
    elif proverka == 'user' : pass
    else : await message.reply(text="You are not Super Admin !!!")
