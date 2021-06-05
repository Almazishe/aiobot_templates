from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery
from bot import dp
from keyboards.inlines import choice, product_keyboard
from keyboards.callbacks import buy_callback


@dp.message_handler(Command("products"))
async def cmd_products(message: Message):
    await message.answer(text="We have such products",
                         reply_markup=choice)


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
