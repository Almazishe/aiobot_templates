import logging
from aiogram import Dispatcher
from tortoise import Tortoise
from src.config import TORTOISE_ORM
from src.utils.notify_admins import notify_on_error

db = Tortoise()


async def on_db_startup(dp: Dispatcher):
    logging.info("Starting database.")
    try:
        await db.init(config=TORTOISE_ORM)
        await db.generate_schemas()

    except ConnectionRefusedError as e:
        await notify_on_error(dp, str(e))
        raise e
    else:
        logging.info("Database started.")


async def on_db_shutdown(dp: Dispatcher):
    db.close_connections()
