from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.bot import api
from config import *
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

import sqlite3
con = sqlite3.connect("database.db")
cur = con.cursor()


PATCHES_URL="https://telegg.ru/orig/bot{token}/{method}"
setattr(api,"API_URL",PATCHES_URL)



CAT_BIG_EYES = "https://avatars.mds.yandex.net/get-pdb/404799/e98ba488-cffa-4b42-8ed2-d6eb0914c01d/s1200?webp=false"




bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
Base = declarative_base()
greet_kb1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(KeyboardButton('Короткий гайд'))
greet_kb2 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(KeyboardButton('Заработать 1000Р'))
greet_kb3 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(KeyboardButton('❤ГОТОВО'))
greet_kb5 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(KeyboardButton('Назад к заданию'))
greet_kb4 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(KeyboardButton('Отправить форму'))



@dp.message_handler(commands=["start"])
async def process_start_command(message: types.message):
    await message.answer(start)
  



@dp.message_handler(text=["Короткий гайд"])
async def process_start_command2(message: types.Message):
   await message.answer(gaid)


@dp.message_handler(text=["Заработать 1000Р",'Назад к заданию'])
async def process_start_command3(message: types.Message):
    await message.answer(money)

@dp.message_handler(text=["❤ГОТОВО"])
async def process_start_command4(message: types.Message):
   await message.answer(done,reply_markup=greet_kb4)


@dp.message_handler(text=["Отправить форму"])
async def process_start_command5(message: types.Message):
   await message.answer(send_form,reply_markup=greet_kb5)


@dp.message_handler(commands=['photo'])
async def process_photo_command(message: types.Message):
    print(message.from_user.id)
    await bot.send_photo(message.from_user.id,CAT_BIG_EYES)




if __name__ == '__main__':
    executor.start_polling(dp)
