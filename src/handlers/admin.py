import logging

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from src.bot import dp
from src.states.product import ProductCreationState
from src.models.products import Product


@dp.message_handler(Command('new-product'), is_admin=True)
async def cmd_new_product(message: types.Message):
    await message.answer(f"Hi admin {message.from_user.username}.\n"
                         f"Please enter new product name:🤪")
    await ProductCreationState.name.set()


@dp.message_handler(state=ProductCreationState.name, is_admin=True)
async def wait_product_name(message: types.Message, state: FSMContext):
    product_name = message.text
    await state.update_data(name=product_name)
    await message.answer(f"What will be price of {product_name}?🤑")
    await ProductCreationState.price.set()


@dp.message_handler(state=ProductCreationState.price, is_admin=True)
async def wait_product_price(message: types.Message, state: FSMContext):
    product_price_str = message.text
    try:
        product_price = float(product_price_str)
    except Exception as e:
        await message.answer(f"{product_price_str} don't look like number🤨")
        await ProductCreationState.price.set()
    else:
        await state.update_data(price=product_price)
        data = await state.get_data()
        product = await Product.create(**data)
        await message.answer(f"{data.get('name')} created successfully😽")
        await state.finish()
        logging.info(f"{product} instance created")