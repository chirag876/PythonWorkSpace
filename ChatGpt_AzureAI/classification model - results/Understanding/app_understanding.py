# Import necessary libraries
import numpy as np
from flask import Flask, request, render_template, jsonify
import utils  # Assuming utils contains the Model class definition

# Create an instance of the Flask class
app = Flask(__name__)

# Load the machine learning model using the utils module
model = utils.Model()

# Define a route for the home page
@app.route('/')
def home():
    # Uncomment the next line for a simple health check
    # return jsonify({"Health check": "Ok"})
    return render_template('index.html')

# Define a route for handling predictions
@app.route('/predict', methods=['GET', 'POST'])
def result():
    try:
        # Check if the request method is GET
        if request.method == "GET":
            # Get data from the query parameters
            data = request.args.get
            print("Data:::", data)

            # Extract the 'text' parameter from the query
            Value = data(('text'))
            print("text:", Value)

            # Split the input text into a list
            input_list = [data for data in Value.split(';')]
            print("input_list::", input_list)

        else:
            # If the request method is POST, get data from the form
            data = request.form.get
            print("Data:::", data)

            # Extract the 'text' parameter from the form
            Value = data(('text'))
            print("text:", Value)

            # Split the input text into a list
            input_list = [data for data in Value.split(';')]
            print("input_list::", input_list)

        # Perform prediction using the loaded model
        out = model.prediction(input_list)

        # Combine input and output into a list of tuples
        ouput_list = list(zip(input_list, out))

        # Create a dictionary for rendering in the template
        dict1 = {}
        for ind, data in enumerate(input_list):
            dict1.update({f"data_{ind}": data, f"Target Column_{ind}": out[ind]})
        print("Dictionary::", dict1)

        # Uncomment the next line for JSON response
        # return jsonify({"Result {data : Target column}:": ouput_list})
        
        # Render the template with the prediction result
        return render_template('index.html', prediction=ouput_list)

    except Exception as e:
        # Handle exceptions and print the error
        print("Error: ", e)

# Run the Flask app if the script is executed directly
if __name__ == "__main__":
    app.run(debug=True)  # For local testing
