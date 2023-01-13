from telegram.ext import Updater,CommandHandler,CallbackContext,MessageHandler,Filters
from telegram import Update,ReplyKeyboardMarkup
import os

# get token from env
TOKEN = os.environ['TOKEN']



def start(update: Update, context: CallbackContext):
    chat_id = update.message.chat.id

    keyboar = ReplyKeyboardMarkup([
        ['🛍 Shop','📦 Cart'],
        ['📞 Contact','📝 About']
    ])
    bot = context.bot
    bot.sendMessage(
    chat_id=chat_id,
    text='Assalom alaykum xush kelibsiz botimizga 👍',
    reply_markup=keyboar
    )


updater = Updater(token=TOKEN)

updater.dispatcher.add_handler(CommandHandler('start',start))

updater.start_polling()
updater.idle()