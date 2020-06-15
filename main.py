from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

from config import TOKEN, help_text

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

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


    with open('start.jpg', 'rb') as photo:
        await message.answer_photo(photo,reply_markup=greet_kb1,
                                   caption='📢 Сразу к делу!\n\nЭтот бот создан с целю заработка и в его основе лежит заработок на реферальной системе в различных ее проявлениях! Именно поэтому я могу гарантировать каждому, кто честно выполнит условия выплату вознаграждения!\n\n✅ Мне просто нет смысла обманывать тебя, так как я заработаю благодаря тебе и поделюсь с тобой!\nПришлю тебе элементарное задание и уже спустя 10 минут ты заберёшь у меня 1000 рублей.\n\n😎 Нажимай кнопку "Короткий гайд" и получишь самую важную информацию и уже через пару минут приступишь к заработку!')


@dp.message_handler(text=["Короткий гайд"])
async def process_start_command(message: types.Message):
    with open('photo_2020-03-18_15-07-20.jpg ', 'rb') as photo:
        await message.answer_photo(photo, reply_markup=greet_kb2, caption='😉О чем тебе не стоит переживать:\n\n1.Задание в этом боте абсолютно легальны и не нарушают законы!\n2. Я гарантировано оплачиваю честный труд! \n3. Где бы ты не вводил личные данные тебе ничего не грозит! Я лично и мои родные прошли это задание.\n\n🕵️ Что тебе нужно соблюдать:\n\n1. Хочешь быстро получить вознаграждение - выполняй инструкции бота на все 100%\n2. Не хитри, не обрезай скриншоты, не делай левых действий.\n\n🤑 Приступим к заработку монеты!\nНа задание у тебя уйдет порядка 7-10 минут и ты получишь от меня 1000 рублей!\n\nГотов? - Нажимай "ЗАРАБОТАТЬ 1000Р"')


@dp.message_handler(text=["Заработать 1000Р",'Назад к заданию'])
async def process_start_command(message: types.Message):
    with open('photo.jpg', 'rb') as photo:
        await message.answer_photo(photo, reply_markup=greet_kb3, caption='Пример к заполнению')
    await message.answer('💵 Собственно задание:\n\nВремя выполнения: ≈7-10 мин\nВознаграждение: 1000 руб.\nУровень сложности: Легкий\nТип: Регистрация с действием\n\nУсловия:\n1. Зайти на сайт: https://bets-money.ru/ \n2. Выбрать способ регистрации «по номеру телефона»\n3. Ввести в поле свой телефон \n4. Нажать кнопку «выслать смс»\n5. Ввести код подтверждения\n6. Выбрать гарантированный бонус (любой)\n7. Ввести промо-код ml_1358\n\n🥳 Поздравляю, ты зарегистрировал аккаунт, сохрани данные и запомни логин, который тебе пригодится для подтверждения, чтобы получить деньги.\n\n8. После того как зашёл в аккаунт, ты должен пополнить счёт от 50 рублей любым удобным способом.\n\n😉 Сделал? Только не обманывай, я проверяю все в ручную. Аккаунт должен быть зарегистрирован не раньше этого дня. Прошлые, старые аккаунты не принимаются. Только новый и только пополненный от 50 руб.\n\nНажми кнопку ❤️ ГОТОВО, если выполнил все условия.')

@dp.message_handler(text=["❤ГОТОВО"])
async def process_start_command(message: types.Message):
   await message.answer('🎉 Отлично, осталось получить свои деньги за выполнение задания! Заполняй форму ниже и я скину тебе твои честно, заработанные деньги!\n\nФорма для выплаты:\nВАЖНО! СОБЛЮДАЙ ОБРАЗЕЦ 1 К 1! СООБЩЕНИЯ НЕ ПО ФАОРМЕ РАСМАТРИВАЮТСЯ В ПОСЛЕДНЮЮ ОЧЕРЕДЬ!\n1. Номер счета который ты зарегестрировал: \n(Тут ты пиши номер счета, не номер телефона, не почту а именно логин, который тебе прислали вместе с паролем)\n2. Твой QIWI кошелек, или банковская карточка, на которую отправить деньги:\n3. Все скриншоты которые ты сделал\n\nКакое сообщение ты в итоге должен мне отправить:\n\nПривет, я выполнил все условия\nЛогин аккаунта: 0000000\nМой Qiwi: +7 или карту\n🌋Все скриншоты которые ты делал\n\nЕсли ты задумал меня обмануть то не стоит, каждое действие будет проверяться и так же будет проверяться твой аккаунт по логину который ты дашь.\n\nГотов отправить мне заполненную форму? Нажимай "Отправить форму"',reply_markup=greet_kb4)


@dp.message_handler(text=["Отправить форму"])
async def process_start_command(message: types.Message):
   await message.answer('👩‍💻 Контакты:\n\nЛично сама Даша которая платит: @dasha_fastmoney  \n👆 форму отправлять сюда\n\nВажно! Скинул форму по образцу, скинул скрины и сиди жди! Если будешь кидать еще сообщения, то с каждым сообщением ты будешь повышать свою очередь на выплату!\n\n✊🙏 Друг, 1 просьба. Вот я честно оплачиваю труд каждого, не пытайся меня обмануть, подделав скриншот или еще чего. Давай ты делай так, чтобы мне упала копейка, а я поделюсь с тобой.',reply_markup=greet_kb5)


@dp.message_handler(commands=['photo'])
async def process_photo_command(message: types.Message):

    await bot.send_photo(message.from_user.id,)

if __name__ == '__main__':
    executor.start_polling(dp)
