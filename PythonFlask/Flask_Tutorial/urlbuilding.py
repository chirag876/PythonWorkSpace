# The url_for() function is used to build a URL to the specific function dynamically. The first argument is the name of the specified function, and then we can pass any number of keyword argument corresponding to the variable part of the URL.

# This function is useful in the sense that we can avoid hard-coding the URLs into the templates by dynamically building them using this function.

''' Benefits of the Dynamic URL Building
# It avoids hard coding of the URLs.
# We can change the URLs dynamically instead of remembering the manually changed hard-coded URLs.
# URL building handles the escaping of special characters and Unicode data transparently.
# The generated paths are always absolute, avoiding unexpected behavior of relative paths in browsers.
# If your application is placed outside the URL root, for example, in /myapplication instead of /, url_for() properly handles that for you.'''

from flask import *  
   
app = Flask(__name__)  
  
@app.route('/admin')  
def admin():  
    return 'admin'  
  
@app.route('/librarion')  
def librarion():  
    return 'librarion'  
  
@app.route('/student')  
def student():  
    return 'student'  

@app.route('/user/<name>')  
def user(name):  
    if name == 'admin':  
        return redirect(url_for('admin'))  
    if name == 'librarion':  
        return redirect(url_for('librarion'))  
    if name == 'student':  
        return redirect(url_for('student'))  

if __name__ =='__main__':  
    app.run(debug = True, port=8081)  