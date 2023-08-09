import os
from dotenv import load_dotenv, dotenv_values
import telebot
from telebot import types
import helpers as hp
load_dotenv()
BOT_TOKEN = "6523955590:AAFb9J4LAtTO0zoiVirg3FbDE9jUL6HNsWA"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Button 1", callback_data='button1')
    button2 = types.InlineKeyboardButton("Button 2", callback_data='button2')
    button3 = types.InlineKeyboardButton("Button 3", callback_data='button3')
    button4 = types.InlineKeyboardButton("create account", callback_data='button4')
    markup.add(button1, button2, button3, button4)

    bot.reply_to(message, "Howdy, how are you doing?", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
    user_id = call.from_user.id
    if call.data == 'button1':
        bot.answer_callback_query(call.id, "You clicked Button 1")
    elif call.data == 'button2':
        bot.answer_callback_query(call.id, "You clicked Button 2")
    elif call.data == 'button3':
        bot.answer_callback_query(call.id, "You clicked Button 3")
    elif call.data == 'button4':
        account = hp.create_new_account(user_id) 
        if account :
            bot.answer_callback_query(call.id, f"here is your account config, and account info\n {account}")
        else:
            bot.answer_callback_query(call.id, "there is no free account in json-file")
bot.infinity_polling()
