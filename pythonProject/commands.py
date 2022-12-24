import random

from bot_config import dp, bot
from aiogram import types

count = 150

@dp.message_handler(commands=['start'])
async def start_bot(message: types.Message):
    await bot.send_message(message.from_user.id,
                           text=f'{message.from_user.first_name}, hello. Lets play one game. '
                                f'You have to take some ammount of candies from 1 to 28')

async def bot_turn(message):
    global count
    if count > 28:
        take = random.randint(1, 28)
    else:
        take = count
    count -= take
    await bot.send_message(message.from_user.id,
                           text=f'Bot took {take}, on the table stay {count} candies')

async def player_turn(message):
    await bot.send_message(message.from_user.id,
                           text=f'{message.from_user.first_name} now is your turn')



@dp.message_handler()
async def start_bot(message: types.Message):
    global count
    name = message.from_user.first_name
    text = message.text
    if message.text.isdigit():
        count -= int(message.text)
        await bot.send_message(message.from_user.id,
                                text=f'{name} took {text} candies, on the table stay {count} candies')
    else:
        await bot.send_message(message.from_user.id,
                                text=f'{name} write correctly how mach candies do you want to take')

    await bot_turn(message)
    await player_turn(message)





