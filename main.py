from telegram.ext import *
# import keys
    
print('Starting a bot....')
     
async def start_commmand(update, context):
    await update.message.reply_text('Hello! Welcome To Store!')

#listen for chat-requiests

#adding him to waiting pool or link him up with someone waiting

# listen for incoming messgaes for his date

# pass his message along

if __name__ == '__main__':
    application = Application.builder().token("6067047983:AAGR7HIiXAKXQTzxztLxLc1oSobI4ESrlJ8").build()

    # Commands
    application.add_handler(CommandHandler('start', start_commmand))

    # Run bot
    application.run_polling(1.0)
