import logging
from aiogram import executor, Dispatcher
from src.models.db import on_db_startup, on_db_shutdown
from src.utils.notify_admins import on_startup_notify
from src.utils.set_bot_commands import set_default_commands
import src.handlers

logging.basicConfig(level=logging.INFO,
                    format=u'%(filename)-17s - #%(levelname)-8s : [%(asctime)s]  %(message)s', )


async def on_startup(dp: Dispatcher):
    logging.info("Starting ")
    await on_db_startup(dp)
    await set_default_commands(dp)
    await on_startup_notify(dp)


async def on_shutdown(dp: Dispatcher):
    await on_db_shutdown(dp)


def setup():
    from src.bot import dp

    executor.start_polling(dispatcher=dp,
                           on_startup=on_startup,
                           on_shutdown=on_shutdown)
