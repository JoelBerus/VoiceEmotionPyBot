import telebot

bot = telebot.TeleBot("1791987070:AAF6rlODgpy4u0AFrzPor40uBe0NESGq-e0")

@bot.message_handler(commands=["helps"])
def enviar(message):
    bot.reply_to(message, "Hola, Soy un bot de el grupo de procesos de soft.")

@bot.message_handler(commands=["start"])
def enviar(message):
    bot.reply_to(message, "Hola, bienvenido")
    
@bot.message_handler(commands=["saludame"])
def enviar(message):
    bot.reply_to(message, "Hola "+ message.from_user.first_name+", ¿como estas?" )

@bot.message_handler(commands=['nude'])
def send_photo(message):
    image = open("\tmp\bot.png", 'rb')
    bot.send_photo(message.chat.id,image )
    #https://drive.google.com/file/d/1-nJ64_E4_Gmm5iSt7RB86N6D6_HKntZs/view
    #bot.reply_to(message, "Hola "+ message.from_user.first_name+", ¿como estas?" )

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling()