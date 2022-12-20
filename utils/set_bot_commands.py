from aiogram import types

async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand('start','Запустить бота'),
        types.BotCommand('help','Помогите'),
        types.BotCommand('photo','photo'),
        types.BotCommand('photo2','photo2')
    ])