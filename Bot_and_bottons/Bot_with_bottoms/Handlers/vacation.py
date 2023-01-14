from create_bot import dp
from aiogram.types import Message
from Keyboards import kb_inline

@dp.message_handler(commands=['vacation'])
async def end_bot(message: Message):
    await message.answer(text='I can offer you where to rest', reply_markup=kb_inline)