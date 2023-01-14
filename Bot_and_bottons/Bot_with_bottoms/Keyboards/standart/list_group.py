from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

kb_print = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

btn_print = []
city = ['Kiev', 'Mariupol', 'Odessa', 'Kharkov']

for town in city:
    btn_print.append(KeyboardButton(text=town))

kb_print.row(*btn_print)

