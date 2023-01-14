from create_bot import dp
from aiogram.types import Message

@dp.message_handler(commands=['end'])
async def end_bot(message: Message):
    await message.answer(text='Hello too')