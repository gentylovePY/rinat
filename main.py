from asyncio import sleep
from aiogram import Bot, types
from aiogram.bot import api
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.utils import executor
from sqlalchemy.ext.declarative import declarative_base
from states import Mailing,storage
from config import *
from db import *




PATCHES_URL="https://telegg.ru/orig/bot{token}/{method}"
setattr(api,"API_URL",PATCHES_URL)


bot = Bot(token=TOKEN)
dp = Dispatcher(bot,storage=storage)
Base = declarative_base()




@dp.message_handler(commands=["start"])
async def process_start_command(message: types.message):
    if not check_if_exists(message.from_user.id):

        register_new_user(message.from_user.id)

    await bot.send_photo( message.from_user.id,   start_photo,caption=start, reply_markup=greet_kb1)
  



@dp.message_handler(text=["Короткий гайд"])
async def process_start_command2(message: types.Message):

   await bot.send_photo(message.from_user.id, gaid_photo, caption=gaid,reply_markup=greet_kb2)


@dp.message_handler(text=["Заработать 1000Р",'Назад к заданию'])
async def process_start_command3(message: types.Message):
    await bot.send_photo(message.from_user.id, money_photo, caption="Пример к заполнению")
    await message.answer(money, reply_markup=greet_kb3)

@dp.message_handler(text=["❤ГОТОВО"])
async def process_start_command4(message: types.Message):
   await message.answer(done,reply_markup=greet_kb4)


@dp.message_handler(text=["Отправить форму"])
async def process_start_command5(message: types.Message):
   await message.answer(send_form,reply_markup=greet_kb5)



@dp.message_handler(user_id=ADMIN_ID, commands=["total_users"])
async def mailig(message: types.Message):
    c.execute("SELECT COUNT(*) as count FROM user")
    res = c.fetchall()
    total_users = res[0][0]
    await message.answer(total_users)




@dp.message_handler(user_id=ADMIN_ID, commands=["tell_everyone"])
async def mailing(message: types.Message):

    await message.answer(("Пришлите текст рассылки"))
    await Mailing.Text.set()



@dp.message_handler(user_id=ADMIN_ID, state=Mailing.Text)
async def mailing_start(message: types.Message, state: FSMContext):
    text = message.text
    c.execute("SELECT * FROM user")
    result = c.fetchall()
    for user in result:
        users = user[0]
        try:
            await bot.send_message(chat_id=users,text=text)
            await sleep(0.5)
        except Exception:
            pass
    await message.answer(("Рассылка выполнена."))
    await state.finish()

if __name__ == '__main__':
    executor.start_polling(dp)
