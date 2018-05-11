from telegram.ext import Updater, CommandHandler


def greet_user(bot, updater):
    mytext = """Привет пользователь!
    я простой бот и понимаю только команду /start
    """
    #print('Вызван /start')
    updater.message.reply_text(mytext)

def main():
    updtr = Updater('596855786:AAExs1OHdwVyH1HjHDLii00qa7DPbwt8Wr')
    dp = updtr.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    updtr.start_polling()
    updtr.idle()


if __name__ == '__main__':
    main()

