#The converter can also be used in the URL to map the specified variable to the particular data type. 

#The following converters are used to convert the default string type to the associated data type.

# string: default
# int: used to convert the string to the integer
# float: used to convert the string to the float.
# path: It can accept the slashes given in the URL.
# email: It can accept the email addresses.
# phone: It can accept the phone numbers.
# ip: It can accept the IP addresses.
# uuid: It can accept the UUIDs.
# json: It can accept the JSON documents.
# json_array: It can accept the JSON arrays.

from flask import Flask  
app = Flask(__name__)  
 
@app.route('/home/<int:age>')  
def age(age):  
    return "Age = %d"%age; 

@app.route('/home/<string:name>')
def name(name):
    return "Name = %s"%name;

@app.route('/home/<string:name>/<int:age>')
def name_age(name,age):
    return "Name = %s, Age = %d"%(name,age);

@app.route('/home/<path:path>')
def path(path):
    return "Path = %s"%path;

@app.route('/home/<path:path>/<int:age>')
def path_age(path,age):
    return "Path = %s, Age = %d"%(path,age);

@app.route('/home/<email:email>')
def email(email):
    return "Email = %s"%email;

@app.route("/weight/<float:weight>")
def weight(weight):
    return "Weight = %f"%weight;

@app.route("/is_raining/<boolean:is_raining>")
def is_raining(is_raining):
    return "Is it raining? %r"%is_raining;

@app.route("/list_of_colors/<list:list_of_colors>")
def list_of_colors(list_of_colors):
    return "My favorite colors are %s"%list_of_colors;

@app.route("/dictionary_of_foods/<dict:dictionary_of_foods>")
def dictionary_of_foods(dictionary_of_foods):
    return "My favorite foods are %s"%dictionary_of_foods;

if __name__ =="__main__":  
    app.run(debug = True,port=8081)  