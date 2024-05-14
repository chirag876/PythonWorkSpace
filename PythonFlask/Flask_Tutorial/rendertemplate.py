# Flask facilitates us to render the external HTML file instead of hardcoding the HTML in the view function. Here, we can take advantage of the jinja2 template engine on which the flask is based.

# Flask provides us the render_template() function which can be used to render the external HTML file to be returned as the response from the view function.

from flask import *  
app = Flask(__name__)  
 
@app.route('/')  
def message():  
      return render_template('rendertemplate.html')  
if __name__ == '__main__':  
   app.run(debug = True) 