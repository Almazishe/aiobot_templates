from aiogram import types
from aiogram.dispatcher.filters import Command, Text
from src.bot import dp
from src.keyboards import menu


@dp.message_handler(Command('menu'))
async def cmd_menu(message: types.Message):
    await message.answer(text="Choose something.",
                         reply_markup=menu)


@dp.message_handler(Text(equals=['Dog', 'Cat', 'Fish']))
async def menu_choice(message: types.Message):
    await message.answer(text=f"{message.text} is good choice",
                         reply_markup=types.ReplyKeyboardRemove())
