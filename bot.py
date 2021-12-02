import telebot
import config
import random

bot = telebot.TeleBot(config.TOKEN)

qt_list = ['chal bc','go to hell','F*k U','Nikkal','Kya hi kr lega','Ek bar or try kr fir btata hu tujhe','bss ruk bhi ja ab','le ke hi maanega']


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(
        message.chat.id,
        'OMG! I know ur bank A/c Details')


@bot.message_handler(commands=['quotes'])
def quotes_sender(message):
    rndm = random.randint(0,len(qt_list)-1)
    bot.send_message(message.chat.id,qt_list[rndm])


bot.polling(non_stop=True)
