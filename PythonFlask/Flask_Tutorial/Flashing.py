from flask import *  
app = Flask(__name__)  
app.secret_key = "abc"  
 
@app.route('/index')  
def home():  
    return render_template("Flashing.html")  
 
@app.route('/login',methods = ["GET","POST"])  
def login():  
    error = None;  
    if request.method == "POST":  
        if request.form['pass'] != 'jtp':  
            error = "invalid password"  
        else:
            flash("you are successfuly logged in")  
            return redirect(url_for('home'))  
    return render_template('Flashing1.html',error=error)  
  
      
if __name__ == '__main__':  
    app.run(debug = True)  
