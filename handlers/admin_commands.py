from aiogram import Router, F, Bot
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove , FSInputFile


from database.data import *
import re
router = Router()

# Buttons 
from keyboards import admin_buttons
from handlers.callback.admin_callback import router as call_router

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
        floder_path = '/Users/apple/Documents/python/tg_bot/InstaFollowerBot/'
        # Export data to .text file
        if text.count('-t') == 1:
            U.extport_to_txt()
            document = FSInputFile(path=floder_path+'users.txt', filename='Users.txt')
            await bot.send_document(message.chat.id, document=document, caption='This is a list of bot users')

        # Exporting data to .json fele
        elif text.count('-j') == 1:
            U.export_to_json()
            document = FSInputFile(path=floder_path+'users.json', filename='Users.json')
            await bot.send_document(chat_id=message.chat.id, document=document , caption='This is a list of bot users in json file')
        
        # Sending data to the chat
        elif text.count('-m') == 1:
            txt = U.export_to_array()
            await bot.send_message(chat_id=message.chat.id, text=txt)

        elif text.count('-db') == 1:
            document = FSInputFile(path=floder_path+'data.sqlite3' , filename='data.sqlite3')
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

# Function for removing admins
@router.message(Command('remove_admin'))
async def remove_admin_command(message:Message):
    A = Admin()
    bot = message.bot
    proverka = A.is_admin(message.from_user.id)

    # Checking is uadmin Super Admin
    if proverka == 'super_admin':
        text = message.text

        # Trying remove admin
        try:
            admin_id = (text.split())[1]

            # Checking data and removing admin where id = admin_id
            if A.remove_admin(user_id=int(admin_id)): await bot.send_message(chat_id=message.chat.id, text=f"✅ SUCCESS ✅\nAdmin -> User")
            else : await message.reply(text="⛔️ ERROR ⛔️\nPleace write correct data !") # If data error
        
        # If can't remove user
        except: await message.reply(text='/remove_admin id_admin (Removes admin)')
    elif proverka == 'user' : pass
    else : await message.reply(text="You are not Super Admin !!!")

# Function for adding sponseor chanals
@router.message(Command('chanal_add'))
async def chanal_add_command(message : Message):
    A = Admin()

    # Checking is admin
    if A.is_admin(message.from_user.id) != 'user':
        text = message.text
        text = text.split()
        
        # Trying add chalal
        try:
            C = Chanals()
            chanal_name = text[1]
            final_trafic = text[2]

            # Check data and add
            if C.create_chanal(chanal_name=chanal_name,current_trafic=0, final_trafic=int(final_trafic), is_active=True):
                await message.bot.send_message(chat_id=message.chat.id, text=f"✅ SUCCESS ✅\n├Chanal @{chanal_name} added\n├Current trafic : 0\n├Final trafic : {final_trafic}\n└Is Active : True")
        
        # If some thing wrong 
        except : await message.reply(text='/chanal_add chanal_name final_trafic')

@router.message(Command('set_ft'))
async def set_final_trafic_command(message:Message):
    A = Admin()
    if A.is_admin(message.from_user.id) != 'user':
        text = message.text
        text = text.split()
    
        try:
            C = Chanals()
            if C.change_trafic(final_trafic=int(text[1]), idv=int(text[2])):
                chanal_info = C.get_chanal_with_id(idv=int(text[2]))
                await message.bot.send_message(chat_id=message.chat.id , text=f"✅ SUCCESS ✅ -> FTrafic == {text[1]}\n{chanal_info}", reply_markup=admin_buttons.chanal_delete_inline_button(idt=int(text[2])) )
            else : pass
        except: await message.reply(text='/set_ft int:num id_chanal (num => new number of trafic)')

@router.message(Command('all_chanals'))
async def get_all_chanals_command(message:Message, bot:Bot):
    A = Admin()
    if A.is_admin(user_id=message.chat.id ) != 'user':
        text =  message.text
        if text.count('-t') == 1:pass
        elif text.count('-j') == 1:pass
        elif text.count('-m') == 1: pass
        else : 
            await bot.send_message(chat_id=message.chat.id , text='🧾 Chanals List 🧾', reply_markup=admin_buttons.chanals_list_buton())
    else : pass

@router.message(Command('cpay_method'))
async def get_all_pay_methods_create(message:Message):
    A = Admin().is_admin(user_id=message.chat.id)
    if A == 'super_admin':
        mes = message.text
        mes = mes.split()
        # print(mes)
        if Pay().create_pay_method(amount=int(mes[1]) , url=mes[2]): await message.answer(text=f'✅ SUCCESS ✅ \nPay method {mes[1]}\nUrl : {mes[2]} \n Created')

router.include_router(call_router)