import logging
from aiogram import executor, types
from bot import dp
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
from handlers import *

logging.basicConfig(level=logging.INFO,
                    format=u'%(filename)-17s - #%(levelname)-8s : [%(asctime)s]  %(message)s',)


async def on_startup(dispatcher):
    logging.info("Bot started")
    await set_default_commands(dispatcher)
    await on_startup_notify(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
