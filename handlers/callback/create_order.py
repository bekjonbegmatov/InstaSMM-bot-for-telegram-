from aiogram import F , Router
from aiogram.types import CallbackQuery , Message
from aiogram.fsm.context import FSMContext
from aiogram.enums.parse_mode import ParseMode

from keyboards.servise_button import inst_order_canel_button
from api.manage_service import ManageBot
from keyboards.servise_button import delete_button, check_order_status_button
from keyboards.pay_button import pay_list_button

from utils.states import InstaOrder
from api.create_order import Order

from database.data import User

router = Router()

@router.callback_query(F.data.startswith('get_fol_'))
async def get_more_info_about_folow_item(call:CallbackQuery, state:FSMContext):
    idv = call.data.split('_')[2]
    info = ManageBot().get_from_id(idv=idv)

    # print(info[0]['name'])
    info = info[0]
    name = info['name']
    price = info['cost']
    tmin = info['min']
    tmax = info['max']
    des = info['description']

    # text = f'<b>{name}</b>\n├<b>Narhi :</b> <code>{price}</code>\n├<b>Minimum :</b> <code>{tmin}</code>\n└<b>Maximum :</b> <code>{tmax}</code>\n\n🛡Kafolat ⭐️ Yuqori sifat ⚡️ Tez boshlash\n\n<b>Tezlik :</b> soatiga 2000\n<b>Boshlanish vaqti:</b> 15 min.\n{des}\n🛡Ushbu xizmat 30 kunlik kafolat bilan taqdim etiladi. kamayish holatlarida qayta tiklash (qo\'llab-quvvatlash xizmatiga yozing)'
    text = (
        f'<b>{name}</b>\n'
        f'├<b>Narhi :</b> <code>{price}</code>\n'
        f'├<b>Minimum :</b> <code>{tmin}</code>\n'
        f'└<b>Maximum :</b> <code>{tmax}</code>\n\n'
        f'🛡Kafolat ⭐️ Yuqori sifat ⚡️ Tez boshlash\n\n'
        f'<b>Tezlik :</b> soatiga 2000\n'
        f'<b>Boshlanish vaqti:</b> 15 min.\n{des}\n\n'
        f'🛡Ushbu xizmat 30 kunlik kafolat bilan taqdim etiladi.'
        f'Kamayish holatlarida qayta tiklash <b>(qo\'llab-quvvatlash xizmatiga yozing)</b>'
    )
    await call.message.bot.edit_message_text(text=text , chat_id=call.message.chat.id, message_id=call.message.message_id , parse_mode=ParseMode.HTML , reply_markup=delete_button())

    link = '-'
    miqdori = '-' 
    summa = 0.0
    order_info = f"""📝<b>Buyurtma haqida ma'lumot</b>
├<b>Ijtimoiy tarmoq:</b> <code>Instagram</code>
├<b>Xizmat:</b> <code>{name}</code>
├<b>Havola:</b> <code>{link}</code>
├<b>Miqdori:</b> <code>{miqdori}</code>
└<b>Narxi:</b> <code>{summa}₽</code>
    """
    
    order_message = await call.message.bot.send_message(chat_id=call.message.chat.id , text=order_info , reply_markup=inst_order_canel_button(), parse_mode=ParseMode.HTML)
    await state.update_data(service=name)
    await state.update_data(price_one=float(int(price)/100))
    await state.update_data(idv=idv)
    await state.set_state(InstaOrder.count)
    await call.message.answer(text='Obunachilar miqdorini yozing : ')

@router.callback_query(F.data == 'canael_inst_order')
async def canael_order_inst(call:CallbackQuery, state:FSMContext):
    await state.clear()
    await call.message.delete()
    await call.message.answer(text='✅ Buyurtma bekor qilindi ✅')

@router.message(InstaOrder.count)
async def get_count(message:Message, state:FSMContext):
    try: 
        count = int(message.text)
        if count >= 10 :
            await state.update_data(count=message.text)
            await message.answer(text='Indi profil ssilkasini yuboring ! \n\nMasalan : https://www.instagram.com/behruz.1312/')
            await state.set_state(InstaOrder.url)
        else: await message.answer(text='Minimum 10 dona bulishi kerak !!!')
    except:
        await message.answer(text='Obunachilar miqdorini yozing, shunchaki neshtaligini : ')

@router.message(InstaOrder.url)
async def get_url_profile(message:Message, state:FSMContext):
    url = message.text
    
    text = url.split('/') 
    if text[0] == 'https:' and text[2] == 'www.instagram.com' and len(text[3]) >= 3 :
        await state.update_data(url=url)
        data = await state.get_data()
        # await state.clear()
        idv = data['idv']
        count = data['count']
        url = data['url']
        name = data['service']
        summa = data['price_one']*int(count)

        order_info = f"""📝<b>Buyurtma haqida ma'lumot</b>
├<b>Ijtimoiy tarmoq:</b> <code>Instagram</code>
├<b>Xizmat:</b> <code>{name}</code>
├<b>Havola:</b> {url}
├<b>Miqdori:</b> <code>{count}</code>
└<b>Narxi:</b> <code>{summa}₽</code>

<b>Buyurtmani tastiqlaysiz mi ? ha yoki yoq deb yozing !</b>
    """
        await message.answer(text=order_info , parse_mode=ParseMode.HTML)
        await state.set_state(InstaOrder.confirm)

    else:
        await message.answer(text='Profil ssilkasini yuboring ! \n\nMasalan : https://www.instagram.com/behruz.1312/\n\nDiqqat ssilka tug\'riligiga ahamiyat bering kegin ozgartirib bulmaydi.\nSavollar bulsa @smm_bot_menejer')

@router.message(InstaOrder.confirm)
async def confirm_order(message:Message, state:FSMContext):
    conf = message.text
    conf = conf.lower()

    if conf == 'ha':
        
        data = await state.get_data()
        idv =  data['idv']
        count = data['count']
        url = data['url']
        name = data['service']
        summa = data['price_one']*int(count)
        order_info = f"""📝<b>Buyurtma haqida ma'lumot</b>
├<b>Ijtimoiy tarmoq:</b> <code>Instagram</code>
├<b>Xizmat:</b> <code>{name}</code>
├<b>Havola:</b> {url}
├<b>Miqdori:</b> <code>{count}</code>
└<b>Narxi:</b> <code>{summa}₽</code>
✅ Buyurtma tastiqlandi ✅
    """
        user = User().get_user_with_user_id(user_id=message.from_user.id)
        balance = float(user['balance'])
        if balance >= summa :
            log = Order().create_instagram_order(url=url,count=int(count),type_id=idv)
            await state.clear()
            new_balance = balance-summa
            User().update_balance(user_id=message.from_user.id, new_balance=str(new_balance))
            order_id=log['id']
            url=log['url']
            count = log['count']
            remains = log['remains']
            status = log['status']

            User().create_order(user_id=message.from_user.id, price=summa, order_id=int(order_id), status=status, count=int(count),remains=int(remains),url=url)

            log_info=f'<b>🔰 Buyurtma statusi 🔰</b>\n├ID : <code>{order_id}</code>\n├URL : {url}\n├Status : {status}\n├Miqdori : {count}\n└Qoldi : {remains}'
            await message.answer(text=order_info, parse_mode=ParseMode.HTML)
            await message.answer(text=log_info, parse_mode=ParseMode.HTML, reply_markup=check_order_status_button(orser_id=str(order_id)))
        else:
            text = f'Buyurtmani amalga oshirish uchun hisobungizda <code>{summa-balance}₽</code> kamlik qilayabti 😞\n<b>Hisobungizni to\'ldirish uchun kerakli tugmani yoki @smm_bot_menejer ga murojat qiling</b>'
            await message.answer(text=text, parse_mode=ParseMode.HTML, reply_markup=pay_list_button(user_id=message.from_user.id))
    elif conf == 'yoq':
        await state.clear()
        await message.answer(text='✅ Buyurtma bekor qilindi ✅')
    else :
        await message.answer(text='Tastiqlaysiz mi ? Ha yoki yoq ?')


@router.callback_query(F.data.startswith('check_order_status_'))
async def check_order_status(call:CallbackQuery):
    order_id = call.data.split('_')[3]
    log = Order().check_order(idv=order_id)
    
    order_id=log['id']
    url=log['url']
    count = log['count']
    remains = log['remains']
    status = log['status']
    log_info=f'<b>🔰 Buyurtma statusi 🔰</b>\n├ID : <code>{order_id}</code>\n├URL : {url}\n├Status : {status}\n├Miqdori : {count}\n└Qoldi : {remains}'
    await call.message.delete()
    await call.message.answer(text=log_info, parse_mode=ParseMode.HTML, reply_markup=check_order_status_button(orser_id=order_id))

        
# like 


# {'id': 475590203, 'url': 'https://www.instagram.com/behruz.beg/', 'start': 0, 'count': 200, 'remains': 200, 'status': 'Pending', 'charge': 0.038, 'currency': 'USD'}