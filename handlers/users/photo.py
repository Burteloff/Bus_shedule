from aiogram import types
from loader import dp
import shedule
@dp.message_handler(text='/photo')
async def command_photo(message: types.Message):
    chat_id = message.from_user.id
    url="https://yandex.ru/maps/21644/roshal'/stops/stop__9686635/?ll=39.854465%2C55.663425&tab=overview&z=18.23"
    photo=shedule.photo_change(url)

    await dp.bot.send_photo(chat_id,photo=photo)