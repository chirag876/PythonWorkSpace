from app import read_input_files

# Replace 'your_flask_app' with the actual name of your Flask application package
# and 'create_app' with the function that creates your Flask app instance.

app = read_input_files()

if __name__ == "__main__":
    # Run the application using the development server for testing purposes.
    app.run()
