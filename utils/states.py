from aiogram.fsm.state import StatesGroup , State 

class InstaOrder(StatesGroup):
    service = State()
    price_one = State()
    idv = State()
    count = State()
    url = State()
    confirm = State()

class Rassilka(StatesGroup):
    image = State()
    desctiption = State()
    confirm = State()