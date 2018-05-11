import logging
import settings
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level = logging.INFO, filename='bot.log')

def greet_user(bot, updater):
    mytext = 'Привет {}! я простой бот и понимаю только команду /start'.format(updater.message.chat.first_name)
    updater.message.reply_text(mytext)

def chat(bot, updater):
	text = updater.message.text
	logging.info(text)
	updater.message.reply_text(text)

def main():
    updtr = Updater(settings.TLG_API_KEY)
    dp = updtr.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, chat))
    updtr.start_polling()
    updtr.idle()


if __name__ == '__main__':
    logging.info('Bot started')
    main()

