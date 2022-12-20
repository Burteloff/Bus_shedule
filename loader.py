from aiogram import Bot,types,Dispatcher
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from data import config

bot=Bot(token=config.BOT_TOKEN,parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=MemoryStorage())
