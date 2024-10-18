# import time

import telebot
from telebot import types
bot = telebot.TeleBot('7715803066:AAHRpvNmzXN3OEj_B8H_NJtr0L3WgsL6cvw')

# @bot.message_handler(commands=['help', 'start'])
# def send_welcome(message):
    # msg = bot.reply_to(message, """\
# Привет, я бот Прогноза погоды.
# Как тебя зовут?
#""")
    #bot.register_next_step_handler(msg, process_name_step)

 
# user_dict = {}
# users_actions = {1:[...], 2:[...]}

# class User:
    # def __init__(self, name):
        # self.name = name
        # self.city = None
        
# def process_name_step(message):
    # try:
        # chat_id = message.chat.id
        # name = message.text
        # user = User(name)
        # user_dict[chat_id] = user
        # msg = bot.reply_to(message, 'В каком городе показать погоду?')
        # bot.register_next_step_handler(msg, process_city_step)
    # except Exception as e:
        # bot.reply_to(message, 'oooops')

# Enable saving next step handlers to file "./.handlers-saves/step.save".
# Delay=2 means that after any change in next step handlers (e.g. calling register_next_step_handler())
# saving will hapen after delay 2 seconds.
# bot.enable_save_next_step_handlers(delay=2)

# Load next_step_handlers from save file (default "./.handlers-saves/step.save")
# WARNING It will work only if enable_save_next_step_handlers was called!
# bot.load_next_step_handlers()

#пример взят: https://github.com/eternnoir/pyTelegramBotAPI/blob/master/examples/step_example.py


@bot.message_handler(commands=['start'])
def start_message(message):
    # bot.send_photo(message.chat.id, photo=open('./mao.jpeg', 'rb'), caption="Добро пожаловать в бот!")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    key1=types.KeyboardButton("❄️☔Погода☀️☁️")
    key2=types.KeyboardButton("🌍Город")
    key3=types.KeyboardButton("✍🏻Рекомендации")
    key4=types.KeyboardButton("↩️Другое")

    markup.add(key1, key2, key3, key4)

    bot.send_message(message.chat.id,f'Привет, {message.from_user.first_name}', reply_markup = markup )


@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == '❄️☔Погода☀️☁️':
            bot.send_message(message.chat.id,f'Привет, {message.from_user.first_name}. Погода на сегодня:')

        elif message.text == '✍🏻Рекомендации':
            bot.send_message(message.chat.id,f'{message.from_user.first_name}, Ваша рекомендация на сегодня:')

        elif message.text == '🌍Город':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            key1=types.KeyboardButton("Новороссийск")
            key2=types.KeyboardButton("Краснодар")
            back=types.KeyboardButton("↩️Назад")
            markup.add(key1, key2, back)

            bot.send_message(message.chat.id, '🌍Город', reply_markup=markup)

        elif message.text == '↩️Другое':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            key1=types.KeyboardButton("О боте")
            back=types.KeyboardButton("↩️Назад")
            markup.add(key1, back)

            bot.send_message(message.chat.id, '↩️Другое', reply_markup=markup)

        elif message.text == '↩️Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            key1=types.KeyboardButton("❄️☔Погода☀️☁️")
            key2=types.KeyboardButton("🌍Город")
            key3=types.KeyboardButton("✍🏻Рекомендации")
            key4=types.KeyboardButton("↩️Другое")

            markup.add(key1, key2, key3, key4)
            bot.send_message(message.chat.id, '↩️Назад', reply_markup=markup)


bot.infinity_polling()
        

        


    # markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # key1=types.KeyboardButton("Погода")
    # markup.add(key1)
    # bot.send_message(message.chat.id, 'Выберите что вам надо', reply_markup=markup) 

# хочу реализовать, туплю как
# @bot.message_handler()
# def info(message):
    # if message.text.lower() == 'привет':
        # bot.send_message(message.chat.id,f'Привет, {message.from_user.first_name}')

# @bot.message_handler(content_types='text')
# def message_reply(message):
#   if message.text=="Погода":
 #       markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
  #      key2=types.KeyboardButton("test1")
   #     markup.add(key2)
    #    bot.send_message(message.chat.id,'Выберите что вам надо',reply_markup=markup)
    # elif message.text=="test1":
     #   bot.send_message(message.chat.id,'https://openweathermap.org/')