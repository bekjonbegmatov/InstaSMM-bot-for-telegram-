from aiogram.utils.keyboard import InlineKeyboardBuilder
from database.data import User
from api.manage_service import ManageBot

def menu_button(user_id: int):
    user = User().get_user_with_user_id(user_id=user_id)
    builder = InlineKeyboardBuilder()
    builder.button(text=f"💳 Hisobni tuldirish ( {user['balance']}₽ )", callback_data="top_up_balance")
    builder.button(text="👥 Obunachilar", callback_data="get_followers")
    builder.button(text="❤️ Layklar", callback_data="get_likes")
    builder.button(text="👀 Prasmotr video", callback_data="get_views_video")
    builder.button(text="🌠 Prasmotr istoriya", callback_data="get_views_story")
    builder.button(text="💬 Izohlar (Comment)", callback_data="get_comments")
    builder.button(text="🔰 Sohraneniya", callback_data="get_saves")
    builder.button(text="📈 Ohvat va Topga chiqish", callback_data="get_ohvat")
    builder.button(text="💼 Acount", callback_data='get_my_account')
    builder.adjust(1, 2, 1)
    return builder.as_markup()

def followers_button():
    manager = ManageBot()
    builder = InlineKeyboardBuilder()
    follow_service = manager.get_from_category(category='1')
    for ser in follow_service:
        service_id = ser['ID']
        builder.button(
            text=ser['name'],
            callback_data=f'get_fol_{service_id}'
        )
    builder.button(text='⬅️ Ortga' , callback_data='back_to_menu')
    builder.adjust(1)
    return builder.as_markup()

# def folowers_item