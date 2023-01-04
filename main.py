from transliterate import to_latin, to_cyrillic
import telebot

# Bu yerga botFatherdan olingan tokenni joylang
TOKEN = ''
bot = telebot.TeleBot(TOKEN, parse_mode=None)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    javob = """Assalomu alaykum, Xush kelibsiz! Matn kiriting: 
Здравствуйте, добро пожаловать! Введите текст:
Hello, Welcome! Enter the text:"""
    bot.reply_to(message, javob)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text
    javob = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    # Yuqoridagini kengroq yozilgan shakli 👇
    # if msg.isascii():
    #     javob = to_cyrillic(msg)
    # else:
    #     javob = to_latin(msg)
    bot.reply_to(message, javob(msg))


bot.infinity_polling()
