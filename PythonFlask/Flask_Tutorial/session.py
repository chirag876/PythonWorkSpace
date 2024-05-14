from flask import *

# Create a Flask app
app = Flask(__name__)

# Set the secret key
app.secret_key = "Chirag"

# Define a route for the home page
@app.route('/')
def home():

    # Create a response object with a link to the get page
    res = make_response("<h4>session variable is set, <a href='/get'>Get Variable</a></h4>")

    # Set the session variable
    session['response'] = 'session#1'

    # Return the response object
    return res

# Define a route for the get page
@app.route('/get')
def getVariable():

    # Check if the response session variable exists
    if 'response' in session:

        # Get the value of the response session variable
        s = session['response']

        # Render the session.html template with the response variable as the name
        return render_template('session.html', name=s)

# Run the app in debug mode
if __name__ == '__main__':
    app.run(debug=True)
