from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_menu = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text='Улица Урицкого'),KeyboardButton(text='Рассвет'),KeyboardButton(text='СпортКорпус')
               ]
        ,
        [KeyboardButton(text='Горсовет'),KeyboardButton(text='Улица Косякова'),KeyboardButton(text='Кинотеатр Родина')]

    ],
    resize_keyboard=True
)