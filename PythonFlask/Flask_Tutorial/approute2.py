#Flask facilitates us to add the variable part to the URL by using the section. We can reuse the variable by adding that as a parameter into the view function.

from flask import Flask  
app = Flask(__name__)  
 
@app.route('/home/<name>')  
def home(name):  
    #return "hello this is the second app routing function,"+name;  
     return f"hello {name}, this is the second app routing function" #formatted string
  
if __name__ =="__main__":  
    app.run(debug = True, port=8081)  