from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN,help_text

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
Base = declarative_base()

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши мне что-нибудь!")
    await bot.send_vo


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.answer(help_text)


@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)



if __name__ == '__main__':
    executor.start_polling(dp)