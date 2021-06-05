from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
from .callbacks import buy_callback

choice = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Buy coke", callback_data=buy_callback.new(
                item_name='Coke',
                quantity=1,
            )),
            InlineKeyboardButton(text="Buy pepsi", callback_data=buy_callback.new(
                item_name='Pepsi',
                quantity=1
            )),
        ],
        [
            InlineKeyboardButton(text="Buy dizzy", callback_data=buy_callback.new(
                item_name='Dizzy',
                quantity=1,
            )),
            InlineKeyboardButton(text="Buy Fanta", callback_data=buy_callback.new(
                item_name='Fanta',
                quantity=1
            )),
        ],
        [
            InlineKeyboardButton(text="Cancel", callback_data='cancel'),
        ]
    ],
)

product_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Buy here",
                                 url='https://www.youtube.com/')
        ]
    ]
)
