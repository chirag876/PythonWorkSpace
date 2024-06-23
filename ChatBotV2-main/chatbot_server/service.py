# -*- coding: utf-8 -*-

##########################
# AUTHOR : AMAN SINGHAL
##########################

import sys
sys.path.append("..")

# third-party module
from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request, render_template
from logging import FileHandler, WARNING

# our modules
from chatbot_code import Bot


app = Flask(__name__, 
            static_folder='../chatbot_ui/static',
            template_folder='../chatbot_ui/templates/')

file_handler = FileHandler("errorlog.txt")
file_handler.setLevel(WARNING)

app.logger.addHandler(file_handler)

obj = Bot()

@app.route("/")
def home(): 
    return render_template("index.html", botname=obj.bot_name)

@app.route("/web_ui")
def bot():
    Message = request.args.get("Message")
    response = obj.run(Message)
    return render_template("partials/income-msg.html", response=response)

@app.route("/get")
def bot_api():
    Message = request.args.get("Message")
    response = obj.run(Message)
    return response

@app.route("/sms", methods=['POST'])
def sms_reply():
    Body = request.form.get("Body")
    response = obj.run(Body)
    resp = MessagingResponse()
    for i in range(len(response["response"])):
        if ".pdf" in response["response"][i]:
            resp.message(response["response"][i])
        else:
            resp.message(response["response"][i])
        if len(response["buttons"][i]) > 0:
            for btn in response["buttons"][i]:
                resp.message(btn)
    return resp
   
if __name__ == "__main__":
    app.run()