from flask import Flask, request
#import json,os,requests
from datetime import date
from Functions import schedule_pipeline

def create_app():
    app = Flask(__name__)
    
    @app.route("/preprocess", methods=["GET"])
    def data_request():
        #credentials=request.get_json()
        schedule_pipeline()
        return 'added the changes!' 
    
    @app.route('/heartbeat', methods=['GET','POST'])
    def heartbeat():
        time=date.today()
        msg='API is working'
        return {'date' : time, 'status' : msg}
    
    return app