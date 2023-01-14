
from aiogram.utils import executor
from Handlers import dp


async def on_startup(_):
    print('Bot started saccesfully! Executor went to post offise.')
    await dp.bot.send_message(chat_id=5345977726, text='My Lord, Bot started!')

executor.start_polling(dispatcher=dp, skip_updates=True, on_startup=on_startup)
