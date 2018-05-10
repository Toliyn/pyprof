from telegram.ext import Updater, CommandHandler


def greet_user(bot, updater):
    #mytext = 'Привет пользователь'
    print('Вызван /start')


def main():
    updtr = Updater('')
    dp = updtr.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    updtr.start_polling()
    updtr.idle()


if __name__ == '__main__':
    main()

