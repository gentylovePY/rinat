from bd import mdb, search_or_save

def sms(bot, update):
    user = search_or_save(mdb, bot.effective_user, bot.message)  # получаем данные из базы данных
    print(user)

    print('Кто-то отправил команду /start. Что мне делать?')  # вывод сообщения в консоль при отправки команды /start
    bot.message.reply_text('Здравствуйте, {}! \nПоговорите со мной {}!'
                           .format(bot.message.chat.first_name))  #