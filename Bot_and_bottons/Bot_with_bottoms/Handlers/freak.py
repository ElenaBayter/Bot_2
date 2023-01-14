from create_bot import dp
from aiogram.types import Message

@dp.message_handler()
async def everything(message: Message):
    if message.text.isdigit():
        await message.answer(text=f'I found a digit {message.text}')
    else:
        await message.answer(text='I dont like that!')
    await dp.bot.send_message(chat_id=5345977726, text=f'{message.from_user.full_name} wrote you something!')