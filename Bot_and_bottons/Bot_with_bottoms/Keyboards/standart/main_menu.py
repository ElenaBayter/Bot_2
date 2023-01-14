from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

kb_menu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

btn_start = KeyboardButton(text='/start')
btn_print = KeyboardButton(text='/vacation')
btn_location = KeyboardButton(text='/location', request_location=True)
btn_contact = KeyboardButton(text='/contact', request_contact=True)

kb_menu.row(btn_start, btn_print)
kb_menu.add(btn_location)
kb_menu.add(btn_contact)

