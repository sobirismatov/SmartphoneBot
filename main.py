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
        [InlineKeyboardButton(text='📞 Phone number',callback_data='number'),InlineKeyboardButton(text='📧 Email',callback_data='email')],
        [InlineKeyboardButton(text='📍 Location',callback_data='location'),InlineKeyboardButton(text='📌 Address',callback_data='address')],
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
    chat_id = query.message.chat_id
    data = query.data
    bot = context.bot
    if data=='number':
        phone_1 ='+998661234567'
        phone_2 ='+998661234567'
        text = f'Our phone numbers:\n{phone_1}\n{phone_2}'
        bot.sendMessage(text=text,chat_id=chat_id)
    elif data=='email':
        email = 'Our email: smartphone@gmail.com'
        bot.sendMessage(text=email,chat_id=chat_id)
        
    elif data=='address':
        address = 'Our address: Samarkand, Uzbekistan'
        bot.sendMessage(text=address,chat_id=chat_id)

    elif data=='location':
        # 39.644053, 66.973233

        lat = 39.644053
        lon = 66.973233
        bot.sendLocation(chat_id=chat_id,latitude=lat,longitude=lon)

    query.answer('Hi')
    print(data)
    

def photo(update: Update, context: CallbackContext):
    chat_id = update.message.chat.id        
    bot = context.bot
    bot.sendMessage(chat_id=chat_id,text='Photo qabul qilindi')

def shop(update: Update, context: CallbackContext):
    chat_id = update.message.chat.id

    iphone = InlineKeyboardButton(text='Iphone',callback_data='phone iphone')
    samsung = InlineKeyboardButton(text='Samsung',callback_data='phone samsung')
    huawei = InlineKeyboardButton(text='Huawei',callback_data='phone huawei')
    xiaomi = InlineKeyboardButton(text='Xiaomi',callback_data='phone xiaomi')
    vivo = InlineKeyboardButton(text='Vivo',callback_data='phone vivo')
    oppo = InlineKeyboardButton(text='Oppo',callback_data='phone oppo')

    # Define keyboard
    keyboar = InlineKeyboardMarkup([
        [iphone,samsung,huawei],
        [xiaomi,vivo,oppo]
    ])

    bot = context.bot
    bot.sendMessage(chat_id=chat_id,text='Choose a phone',reply_markup=keyboar)

def phone(update: Update, context: CallbackContext):
    query = update.callback_query
    chat_id = query.message.chat_id
    data,brand = query.data.split()

    bot = context.bot
    if brand=='iphone':
        model= 'iPhone XR'
        color = 'Black'
        ram= '4GB'
        memory= '64GB'
        price = '400$'
        img_url ='https://images-na.ssl-images-amazon.com/images/I/51qBzX0pGYL._SL1000_.jpg'
        text = f'Phone model: {model}\nColor: {color}\nRAM: {ram}\nMemory: {memory}\nPrice: {price}'
        bot.sendPhoto(chat_id=chat_id,caption=text,photo=img_url)
        

        


    query.answer('Phone')
    print(brand)

updater = Updater(token=TOKEN)

updater.dispatcher.add_handler(CommandHandler('start',start))
# Add handler for photo message
updater.dispatcher.add_handler(MessageHandler(Filters.photo,photo))
updater.dispatcher.add_handler(MessageHandler(Filters.text('🛍 Shop'),shop))
updater.dispatcher.add_handler(MessageHandler(Filters.text('📝 About'),about))
updater.dispatcher.add_handler(MessageHandler(Filters.text('📞 Contact'),contact))
updater.dispatcher.add_handler(MessageHandler(Filters.text('Main menu'),start))
updater.dispatcher.add_handler(CallbackQueryHandler(phone,pattern='phone'))
updater.dispatcher.add_handler(CallbackQueryHandler(query))

updater.start_polling()
updater.idle()