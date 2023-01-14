
import os
from aiogram import Bot, Dispatcher
from aiogram.types import Message

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)