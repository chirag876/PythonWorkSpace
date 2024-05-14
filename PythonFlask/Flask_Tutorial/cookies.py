from flask import *

# Create a Flask app
app = Flask(__name__)

# Define a route for the cookie page
@app.route('/cookie')
def cookie():

    # Create a response object with the text "cookie is set"
    res = make_response("<h1>cookie is set</h1>")

    # Set the cookie "Chirag" with the value "Flask"
    res.set_cookie('Chirag', 'Flask')

    # Return the response object
    return res

# Run the app in debug mode
if __name__ == '__main__':
    app.run(debug=True)
