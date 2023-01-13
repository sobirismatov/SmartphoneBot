from telegram.ext import Updater,CommandHandler,CallbackContext,MessageHandler,Filters,CallbackQueryHandler
from telegram import Update,ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton
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

def about(update: Update, context: CallbackContext):
    chat_id = update.message.chat.id

    keyboar = ReplyKeyboardMarkup([
        ['📝 About Us','📝 About the bot'],
        ['Main menu']
    ])
    bot = context.bot
    bot.sendMessage(
    chat_id=chat_id,
    text='Assalom alaykum xush kelibsiz botimizga 👍',
    reply_markup=keyboar
    )

def contact(update: Update, context: CallbackContext):
    chat_id = update.message.chat.id

    keyboar = InlineKeyboardMarkup([
        [InlineKeyboardButton(text='📞 Phone number',callback_data='number')],
        [InlineKeyboardButton(text='📍 Location',callback_data='location')],
        # [InlineKeyboardButton(text='📞 Phone number',url='txt')]
        
    ])
    bot = context.bot
    bot.sendMessage(
    chat_id=chat_id,
    text='Assalom alaykum xush kelibsiz botimizga 👍',
    reply_markup=keyboar
    )

def query(update: Update, context: CallbackContext):
    query = update.callback_query
    data = query.data
    print(data)
    



updater = Updater(token=TOKEN)

updater.dispatcher.add_handler(CommandHandler('start',start))
updater.dispatcher.add_handler(MessageHandler(Filters.text('📝 About'),about))
updater.dispatcher.add_handler(MessageHandler(Filters.text('📞 Contact'),contact))
updater.dispatcher.add_handler(MessageHandler(Filters.text('Main menu'),start))
updater.dispatcher.add_handler(CallbackQueryHandler(query))

updater.start_polling()
updater.idle()