from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from src.config import API_TOKEN
from src.filters import IsAdminFilter

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)
dp.filters_factory.bind(IsAdminFilter)
