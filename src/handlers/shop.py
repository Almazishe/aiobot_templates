import logging
from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery
from src.bot import dp
from src.keyboards.inlines import choice, product_keyboard, create_product_choice_markup
from src.keyboards.callbacks import buy_callback
from src.models.products import Product


@dp.message_handler(Command("products"))
async def cmd_products(message: Message):
    products = await Product.all()
    await message.answer(text="We have such products",
                         reply_markup=create_product_choice_markup(products))


@dp.callback_query_handler(buy_callback.filter())
async def buy_product(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    await call.message.answer(
        text=f"U wanna buy {callback_data.get('quantity')} {callback_data.get('item_name')}",
        reply_markup=product_keyboard)


@dp.callback_query_handler(text="cancel")
async def cancel_shop(call: CallbackQuery):
    await call.answer("You canceled products.", show_alert=True)
    await call.message.edit_reply_markup(reply_markup=None)
