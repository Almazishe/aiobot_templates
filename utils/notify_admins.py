import logging
from aiogram import Dispatcher
from aiogram.utils.exceptions import ChatNotFound
from bot import SUPER_ADMIN


async def on_startup_notify(dp: Dispatcher):
    try:
        await dp.bot.send_message(SUPER_ADMIN, "Бот полетел🛫")

    except ChatNotFound as err:
        logging.error(f"Superadmin with chat_id:{SUPER_ADMIN} not found.")
