import os
from dotenv import load_dotenv , dotenv_values

load_dotenv()
BOT_TOKEN = "6499678561:AAHxLJ2DSGO0SZJKYjzJ9LTaKO0dHDeIJz8"

import telebot

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


bot.infinity_polling()