from create_bot import dp
from aiogram.types import CallbackQuery
from Keyboards.Standart import main_menu

@dp.callback_query_handler(text='ADD')
async def add_cmd(callback: CallbackQuery):
    print(callback)
    await callback.answer('Added saccessfully!', show_alert=True)