from flask import *  
app = Flask(__name__)  
  
@app.route('/')  
def customer():  
   return render_template('form.html')  
  
@app.route('/success',methods = ['POST', 'GET'])  
def print_data():  
   if request.method == 'POST':  
      result = request.form  
      return render_template("form1.html",result = result)  
   
if __name__ == '__main__':  
   app.run(debug = True)  

# In the following example, the / URL renders a web page form.html that contains a form which is used to take the customer details as the input from the customer.

# The data filled in this form is posted to the /success URL which triggers the print_data() function. The print_data() function collects all the data from the request object and renders the form1.html file which shows all the data on the web page.