# The abort() function is used to handle the cases where the errors are involved in the requests from the client side, such as bad requests, unauthorized access and many more. However, the error code is to be mentioned due to which the error occurred.

# The syntax to use the abort() function is given below.

# Flask.abort(code)  

from flask import *  
app = Flask(__name__)  
 
@app.route('/')  
def home ():  
    return render_template("Abort.html")  
 
@app.route('/login')  
def login():  
    return render_template("Abort1.html");  
 
@app.route('/validate', methods = ["POST"])  
def validate():  
    if request.method == 'POST' and request.form['pass'] == 'jtp':  
        return redirect(url_for("success"))  
    else:  
        abort(401)  
 
@app.route('/success')  
def success():  
    return "logged in successfully"  
  
if __name__ == '__main__':  
    app.run(debug = True)  