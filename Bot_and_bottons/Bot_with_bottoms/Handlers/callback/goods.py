from create_bot import dp
from aiogram.types import CallbackQuery
from Handlers.callback.call_back import goods
from Keyboards import kb_inline

@dp.callback_query_handler(goods.filter(items='Goods'))
async def add_cmd(callback: CallbackQuery):
    new_text = f'Goods added to cart {callback.data.split(":")[-1]}'
    await  dp.bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id,
                                    text=new_text, reply_markup=kb_inline)
    await callback.answer('Added saccessfully!', show_alert=False)