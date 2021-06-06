from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
from .callbacks import buy_callback


def create_product_choice_markup(items):
    inline_keyboard = []

    for item in items:
        item_button = [
            InlineKeyboardButton(text=f"Buy {item.name}",
                                 callback_data=buy_callback.new(
                                     item_name=item.name,
                                     quantity=1,
                                 ))
        ]
        inline_keyboard.append(item_button)

    markup = InlineKeyboardMarkup(
        inline_keyboard=inline_keyboard
    )

    return markup


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
