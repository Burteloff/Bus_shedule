from aiogram import types
from loader import dp
import shedule
@dp.message_handler(text='/photo2')
async def command_photo(message: types.Message):
    chat_id = message.from_user.id
    url="https://yandex.ru/maps/21644/roshal'/stops/stop__9690487/?ll=39.848265%2C55.663412&tab=overview&z=18.23"
    photo=shedule.photo_change(url)

    await dp.bot.send_photo(chat_id,photo=photo)