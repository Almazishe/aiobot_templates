from aiogram.dispatcher.filters.state import StatesGroup, State


class ProductCreationState(StatesGroup):
    name = State()
    price = State()
