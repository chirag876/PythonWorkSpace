# The add_url_rule() function in Flask is used to register a URL rule with the application. A URL rule is a mapping between a URL path and a view function. When a request is made to a URL that matches a registered URL rule, the view function is called to handle the request.

# The add_url_rule() function takes three arguments:

# rule: The URL path that the rule should match.
# endpoint: The name of the view function that should be called when the rule matches.
# view_func: The view function itself. This argument is optional; if it is not provided, the add_url_rule() function will look for a view function with the same name as the endpoint argument.

from flask import Flask

app = Flask(__name__)

@app.route("/")
def run():
    return "Hello, world!"

@app.route("/index")
def index():
    return "This is the index page."

@app.route("/home")
def home():
    return "This is the home page."

if __name__ == "__main__":
    app.run(debug = True,port=8081)

# When this code is run, the Flask application will be started on port 5000. If you visit any of the URLs http://localhost:5000/, http://localhost:5000/index, or http://localhost:5000/home in your web browser, you will see the corresponding message.