from aiogram import types
from loader import dp
from aiogram.dispatcher.filters import Command
from keyboards import kb_menu
from utils.misc import rate_limit


@rate_limit(limit=5)
@dp.message_handler(Command('start'))
async def command_start(message: types.Message):
    await message.answer("Выбери число",reply_markup=kb_menu)