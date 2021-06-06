from aiogram.dispatcher.filters.state import StatesGroup, State


class Test(StatesGroup):
    first_name = State()
    last_name = State()
    phone = State()
