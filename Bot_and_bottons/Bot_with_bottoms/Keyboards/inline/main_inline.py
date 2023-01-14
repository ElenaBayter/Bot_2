from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Handlers.callback.call_back import goods


kb_inline = InlineKeyboardMarkup(row_width=2)

btn_add = InlineKeyboardButton(text='add', callback_data='ADD')
btn_remove = InlineKeyboardButton(text='buy', callback_data=goods.new(items='Goods', count='100'))
btn_print = InlineKeyboardButton(text='print', callback_data='PRINT_P')
btn_exit = InlineKeyboardButton(text='exit', callback_data='EXIT')

kb_inline.row(btn_add, btn_remove, btn_print, btn_exit)