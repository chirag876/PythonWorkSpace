# Due to the fact that HTML is a mark-up language and purely used for the designing purpose, sometimes, in the web applications, we may need to execute the statements for the general-purpose computations. For this purpose, Flask facilitates us the delimiter {%...%} which can be used to embed the simple python statements into the HTML.

from flask import *  
app = Flask(__name__)  
  
@app.route('/table/<int:num>')  
def table(num):  
      return render_template('embeddedpython.html',n=num)  
if __name__ == '__main__':  
   app.run(debug = True)  