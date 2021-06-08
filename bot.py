# 1. Enable Logging
# we want to know about the activities(warning,errors) in a systematic manner
# thats why we need logging
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# logger object will help us create the logs in this program
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


TOKEN = "1701925941:AAHNOV5z5z6S100tno5eqO1fMnytLfnHq74"

# CommandHandlers
# def start(bot, update):
#     print(update)
#     author=update.message.from_user.first_name
#     # msg=update.message.text
#     reply="Hi! {}",format(author)
#     bot.send_message(chat_id=update.message.chat_id, text=reply)
def start(update, context):
   print(update)
   author=update.message.from_user.first_name
   reply="Hi! {}".format(author)
   context.bot.sendMessage(chat_id=update.message.chat_id, text=reply)

def _help(update, context):
    help_text="Hey! This is a help text."
    context.bot.send_message(chat_id=update.message.chat_id, text=help_text)

def echo_text(update, context):
    reply =update.message.text
    context.bot.send_message(chat_id=update.message.chat_id, text=reply)

def echo_sticker(update, context):
    context.bot.send_sticker(chat_id=update.message.chat_id,sticker=update.message.sticker.file_id)
def error(bot,update):
    logger.error("Update '%s' caused error '%s'",update, update.error)


def main():
    # this will try to recieve updates for the bot
    updater = Updater(TOKEN)
    # this will keep on handling the updates
    dp=updater.dispatcher

    dp.add_handler(CommandHandler("start",start))
    dp.add_handler(CommandHandler("help",_help))
    dp.add_handler(MessageHandler(Filters.text, echo_text))
    dp.add_handler(MessageHandler(Filters.sticker,echo_sticker))
    dp.add_error_handler(error)
    updater.start_polling()
    logger.info("Started polling...")
    updater.idle()

if __name__=="__main__":
    main()
