from create_bot import dp
from aiogram.types import Message
from Keyboards import kb_menu


@dp.message_handler(commands=['start'])
async def start_bot(message: Message):
    name = message.from_user.full_name
    await message.answer(f'{name}, hello! Choose one of item from menu!', reply_markup=kb_menu)