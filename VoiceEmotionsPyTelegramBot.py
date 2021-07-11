import telebot
bot = telebot.TeleBot("1791987070:AAF6rlODgpy4u0AFrzPor40uBe0NESGq-e0")
@bot.message_handler(commands=["helps", "start"])

def enviar(message):
    bot.reply_to(message, "Hola, ¿como estas?")
bot.polling()