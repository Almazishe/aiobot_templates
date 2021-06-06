from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Cat"),
        ],
        [
            KeyboardButton(text="Dog"),
            KeyboardButton(text="Fish"),
        ],
    ],
    resize_keyboard=True
)
