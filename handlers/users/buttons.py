from aiogram import types
from loader import dp
from aiogram.dispatcher.filters import Command
from keyboards import kb_menu

import shedule
from utils.misc import rate_limit


@rate_limit(limit=120,key="Улица Урицкого")
@dp.message_handler(text='Улица Урицкого')
async def command_start(message: types.Message):
    chat_id = message.from_user.id
    url="https://yandex.ru/maps/21644/roshal'/stops/stop__9690487/?ll=39.848265%2C55.663412&tab=overview&z=18.23"
    photo = shedule.photo_change(url)
    await dp.bot.send_photo(chat_id,photo=photo,reply_markup=kb_menu)

@rate_limit(limit=120,key="Рассвет")
@dp.message_handler(text='Рассвет')
async def command_start(message: types.Message):
    chat_id = message.from_user.id
    url = "https://yandex.ru/maps/21644/roshal'/stops/stop__9686635/?ll=39.854465%2C55.663425&tab=overview&z=18.23"
    photo = shedule.photo_change(url)
    await dp.bot.send_photo(chat_id, photo=photo, reply_markup=kb_menu)

@rate_limit(limit=120,key="СпортКорпус")
@dp.message_handler(text='СпортКорпус')
async def command_start(message: types.Message):
    chat_id = message.from_user.id
    url = "https://yandex.ru/maps/21644/roshal'/stops/stop__9688463/?ll=39.859747%2C55.663631&tab=overview&z=19.03"
    photo = shedule.photo_change(url)
    await dp.bot.send_photo(chat_id, photo=photo, reply_markup=kb_menu)

@rate_limit(limit=120,key="Горсовет")
@dp.message_handler(text='Горсовет')
async def command_start(message: types.Message):
    chat_id = message.from_user.id
    url = "https://yandex.ru/maps/21644/roshal'/stops/stop__9675963/?ll=39.867317%2C55.661275&tab=overview&z=18.37"
    photo = shedule.photo_change(url)
    await dp.bot.send_photo(chat_id, photo=photo, reply_markup=kb_menu)
@rate_limit(limit=120,key="Улица Косякова")
@dp.message_handler(text='Улица Косякова')
async def command_start(message: types.Message):
    chat_id = message.from_user.id
    url = "https://yandex.ru/maps/21644/roshal'/stops/stop__9690183/?ll=39.873109%2C55.658386&tab=overview&z=17.21"
    photo = shedule.photo_change(url)
    await dp.bot.send_photo(chat_id, photo=photo, reply_markup=kb_menu)
@rate_limit(limit=120,key="Кинотеатр Родина")
@dp.message_handler(text='Кинотеатр Родина')
async def command_start(message: types.Message):
    chat_id = message.from_user.id
    url = "https://yandex.ru/maps/21644/roshal'/stops/stop__9678414/?ll=39.881612%2C55.658909&tab=overview&z=17.64"
    photo = shedule.photo_change(url)
    await dp.bot.send_photo(chat_id, photo=photo, reply_markup=kb_menu)