import logging
from aiogram import Dispatcher
from aiogram.utils.exceptions import ChatNotFound
from src.config import SUPER_ADMIN


async def notify_admin(dp: Dispatcher, message: str):
    try:
        await dp.bot.send_message(SUPER_ADMIN, message)
    except ChatNotFound as err:
        logging.error(f"Superadmin with chat_id:{SUPER_ADMIN} not found.")


async def on_startup_notify(dp: Dispatcher):
    await notify_admin(dp, "Бот запускается🛫")


async def notify_on_error(dp: Dispatcher, error_message):
    await notify_admin(dp, error_message)
