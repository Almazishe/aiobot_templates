from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart, CommandHelp
from src.bot import dp


@dp.message_handler(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(f"Hi, {message.from_user.full_name}!✋")


@dp.message_handler(CommandHelp())
async def cmd_help(message: types.Message):
    await message.answer(text=f"I can't help you sorry.🙇")
