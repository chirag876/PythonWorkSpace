# App routing is used to map the specific URL with the associated function that is intended to perform some task. It is used to access some particular page like in the web application.

from flask import Flask  
app = Flask(__name__)  
 
@app.route('/home')  
def home():  
    return "This is the first app routing function";  
  
if __name__ =="__main__":  
    app.run(debug = True,port=8081)  