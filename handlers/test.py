import logging

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from bot import dp
from states.test import Test


@dp.message_handler(Command('test'), state=None)
async def cmd_test(message: types.Message):
    logging.info(message.text)
    await message.answer("What is your name?")
    await Test.first_name.set()


@dp.message_handler(state=Test.first_name)
async def wait_first_name(message: types.Message, state: FSMContext):
    first_name = message.text
    await state.update_data(first_name=first_name)
    await message.answer("What is your last name?")
    await Test.next()


@dp.message_handler(state=Test.last_name)
async def wait_first_name(message: types.Message, state: FSMContext):
    last_name = message.text
    await state.update_data(last_name=last_name)
    await message.answer("What is your phone number?")
    await Test.next()


@dp.message_handler(state=Test.phone)
async def wait_first_name(message: types.Message, state: FSMContext):
    phone = message.text
    data = await state.get_data()
    data['phone'] = phone
    text = f"🤟🏿Welcome {data['first_name']} {data['last_name']} with phone number {data['phone']}👰"
    await message.answer(text)
