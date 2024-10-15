import telebot
from telebot import types
bot = telebot.TeleBot('7715803066:AAHRpvNmzXN3OEj_B8H_NJtr0L3WgsL6cvw')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,'Привет')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    key1=types.KeyboardButton("Погода")
    markup.add(key1)
    bot.send_message(message.chat.id, 'Выберите что вам надо', reply_markup=markup)

@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text=="Погода":
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        key2=types.KeyboardButton("test1")
        markup.add(key2)
        bot.send_message(message.chat.id,'Выберите что вам надо',reply_markup=markup)
    elif message.text=="test1":
        bot.send_message(message.chat.id,'https://openweathermap.org/')
bot.infinity_polling()