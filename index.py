from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import os

TOKEN = os.environ.get("7867353208:AAHKuV6l4yphWbtZcVpf6H8LV5wLERGlwg8")

def main():
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher
    # Add handlers here (as previously described)

    updater.start_polling()
    updater.idle()

def handler(request):
    main()
    return "Bot is running!"

if __name__ == "__main__":
    main()
