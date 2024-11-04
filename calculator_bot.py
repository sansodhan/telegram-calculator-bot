from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackContext

# Define states
FIRST, SECOND, OPERATION = range(3)

def start(update: Update, context: CallbackContext) -> int:
    update.message.reply_text("FIRST NUMBER - Please enter the first number:")
    return FIRST

def first_number(update: Update, context: CallbackContext) -> int:
    context.user_data['first'] = float(update.message.text)
    update.message.reply_text("SECOND NUMBER - Please enter the second number:")
    return SECOND

def second_number(update: Update, context: CallbackContext) -> int:
    context.user_data['second'] = float(update.message.text)
    update.message.reply_text("What to do? Type 'plus' for addition or 'minus' for subtraction:")
    return OPERATION

def operation(update: Update, context: CallbackContext) -> int:
    first = context.user_data['first']
    second = context.user_data['second']

    if update.message.text.lower() == 'plus':
        result = first + second
        update.message.reply_text(f"Result: {first} + {second} = {result}")
    elif update.message.text.lower() == 'minus':
        result = first - second
        update.message.reply_text(f"Result: {first} - {second} = {result}")
    else:
        update.message.reply_text("Invalid operation! Please type 'plus' or 'minus'.")

    return ConversationHandler.END

def cancel(update: Update, context: CallbackContext) -> int:
    update.message.reply_text("Calculator canceled.")
    return ConversationHandler.END

def main() -> None:
    # Your bot token
    updater = Updater("7867353208:AAHKuV6l4yphWbtZcVpf6H8LV5wLERGlwg8")

    dispatcher = updater.dispatcher

    # Conversation handler to manage the conversation states
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            FIRST: [MessageHandler(Filters.text & ~Filters.command, first_number)],
            SECOND: [MessageHandler(Filters.text & ~Filters.command, second_number)],
            OPERATION: [MessageHandler(Filters.text & ~Filters.command, operation)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    dispatcher.add_handler(conv_handler)

    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
