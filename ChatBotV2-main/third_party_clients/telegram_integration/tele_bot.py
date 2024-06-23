# -*- coding: utf-8 -*-

##########################
# AUTHOR : AMAN SINGHAL
##########################


import config as keys
from telegram.ext import *
import requests
import os

print("Bot Started...")

# This is start command response. Whenever user start the chat with bot start command will be initialized.
# you can type /start to start the chat
def start(update, context):
    update.message.reply_text(f'Hello {update.effective_user.first_name}, I am Alice, your Virtual Assistant')
    update.message.reply_text("I'm here to show you some chatbot examples and demo our product features. You can choose to chat with me via Text or Voice")
    update.message.reply_text("I would like to know your name for a better experience")

# This is help command. To initialize the help you can type /help
def help(update, context):
    update.message.reply_text('Please read README file for help')

# This function handles the messages sent by user and get the repsponse from our chatbot api.
def handle_message(update, context):
    # getting message typed by user in telegram
    text = update.message.text
    
    # Call chatbot API to get response
    url = keys.CHATBOT_URL
    params = {
        "Message": str(text)
    }
    response = requests.get(url, params=params).json()
    print(response)
    for i in range(len(response['response'])):
        if ".pdf" in response['response'][i]:
            filename = os.path.join(keys.FILES_PATH, response['response'][i])
            url = f"https://api.telegram.org/bot{keys.API_KEY}/sendDocument?chat_id={update.effective_chat.id}"
            files = [
            ('document', open(filename,'rb'))
            ]
            response = requests.post(url, files = files)
            print(response.status_code)

        else:
            update.message.reply_text(response['response'][i])

        if len(response['buttons'][i]) > 0:
            for btn in response['buttons'][i]:
                update.message.reply_text(btn)

# This is an error handler function
def error(update, context):
    print(f"Updates {update} caused error {context.error}")

# Main method to run the telegram API
def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
