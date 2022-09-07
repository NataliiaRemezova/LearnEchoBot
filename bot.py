import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings
logging.basicConfig(filename='bot.log', level=logging.INFO)

def greet_user(update, context):
    print('You have pressed /start')
    update.message.reply_text('Hello user! You have pressed /start')

def talk_to_me(update, context):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)

def main():
    echo_bot = Updater(settings.API_KEY, use_context=True)
    
    dp = echo_bot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    logging.info("This bot has started")
    echo_bot.start_polling()
    echo_bot.idle()

if __name__ == "__main__":
    main()