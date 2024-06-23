from flask import Flask, request
#import json,os,requests
from datetime import date
from Functions import preprocess

def create_app(connectionstring):
    app = Flask(__name__)

    @app.route("/preprocess", methods=["GET"])
    def data_request():
        credentials=request.get_json()
        status=preprocess(credentials)
        return status

    @app.route('/heartbeat', methods=['GET','POST'])
    def heartbeat():
        time=date.today()
        msg='API is working'
        return {'date' : time, 'status' : msg}

    return app