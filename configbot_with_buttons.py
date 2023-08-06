from typing import Final
import telegram
from telegram.ext import Updater,CommandHandler,MessageHandler,filters, CallbackContext, CallbackQueryHandler


# Constants
TOKEN: Final[str] = "YOUR_BOT_TOKEN_HERE"
BOT_USERNAME: Final[str] = "@Proto_hamedpro_bot"

# Command handlers
def start_command(update: telegram.Update, context: CallbackContext):
    keyboard = [
        [
            InlineKeyboardButton("Option 1", callback_data='1'),
            InlineKeyboardButton("Option 2", callback_data='2')
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Please choose an option:', reply_markup=reply_markup)

def help_command(update: telegram.Update, context: CallbackContext):
    update.message.reply_text('This is a help message.')

def custom_command(update: telegram.Update, context: CallbackContext):
    update.message.reply_text('This is a custom command.')

# Message handler
def handle_message(update: telegram.Update, context: CallbackContext):
    text = update.message.text.lower()
    if "hello" in text:
        update.message.reply_text("Hello!")
    elif "how are you" in text:
        update.message.reply_text("I'm fine, thank you!")
    elif "elahe" in text or "hamed" in text:
        update.message.reply_text("Salam chetori?")
    else:
        update.message.reply_text("I don't understand.")

# Callback handler
def handle_callback(update: telegram.Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=f"You selected option {query.data}.")

# Error handler
def handle_error(update: telegram.Update, context: CallbackContext):
    print(f"Error: {context.error}")
    update.message.reply_text("Oops! Something went wrong.")

if __name__ == "__main__":
    # Create an Updater object with the bot's token
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register command handlers
    dispatcher.add_handler(CommandHandler("start", start_command))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("custom", custom_command))

    # Register message handler
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Register callback handler
    dispatcher.add_handler(CallbackQueryHandler(handle_callback))

    # Register error handler
    dispatcher.add_error_handler(handle_error)

    # Start the bot
    updater.start_polling()

    # Run the bot until Ctrl-C is pressed
    updater.idle()