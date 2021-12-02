import telebot
import config
import random
import time

bot = telebot.TeleBot(config.TOKEN)

qt_list = ['chal hurrrrrr','go to hell','Bhaad m ja','Nikkal','Kya hi kr lega','Ek bar or try kr fir btata hu tujhe','bss ruk bhi ja ab','kime le k maanega']


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(
        message.chat.id,
        'Kya hal')


@bot.message_handler(commands=['quotes'])
def quotes_sender(message):
    rndm = random.randint(0,len(qt_list)-1)
    bot.send_message(message.chat.id,qt_list[rndm])


@bot.message_handler(commands=['help'])
def help_fxn(message):
    keyboard = telebot.types.InlineKeyboardMarkup()

    keyboard.add(
        telebot.types.InlineKeyboardButton(
            'Idhar mar le',url='telegram.me/querty456'
            )
        )
    bot.send_message(
        message.chat.id,
        'To help chahiye tujhe\n'+
        'Ek kam kr\n'+
        'Button Dikh rha neeche?\n'+
        'Dba le usne or dm kr de\n\n'+
        'Or kch alkas khatam kr ske to\n'+
        '/help for help\n'+
        '/grab for your info\n'+
        '/start for starting\n'+
        '/quotes for motivational quotes\n',reply_markup=keyboard)

@bot.message_handler(commands=['grab'])
def grab_fxn(message):
    user = message.from_user
    data = 'Your user id is : '+str(user.id) + '\nYour first name is : '+user.first_name

    if user.last_name:
        data += '\nYour last name is : ' + user.last_name
    if user.username:
        data += '\nYour username is : ' + user.username

    bot.reply_to(message,data)
    time.sleep(3)
    bot.send_message(message.chat.id,'Ab kya kundli nikalu kya?')





bot.polling(non_stop=True)
