# The static files such as CSS or JavaScript file enhance the display of an HTML web page. A web server is configured to serve such files from the static folder in the package or the next to the module. The static files are available at the path /static of the application.

from flask import *  
app = Flask(__name__)  
 
@app.route('/')  
def message():  
      return render_template('static.html')  
if __name__ == '__main__':  
   app.run(debug = True)  