from flask import Flask, jsonify, request
from flask_jwt_extended import create_access_token
import secrets
import string

def generate_secret_key(length=24):
    # Define characters to be used for the secret key (letters, digits, and punctuation)
    key_characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a random key by choosing characters randomly 'length' number of times
    secret_key = ''.join(secrets.choice(key_characters) for _ in range(length))
    return secret_key

# Generate a new key
new_key = generate_secret_key()

def authenticate_login():
    # Retrieve JSON data from the request
    data = request.get_json()
    # Check if the provided username and password are valid
    if data.get('username') == 'chirag876' and data.get('password') == 'chirag@1706':
        # Create an access token for the provided username
        access_token = create_access_token(identity=data.get('username'))
        # Return the access token upon successful authentication
        return jsonify(access_token=access_token), 200
    # Return error for invalid credentials
    return jsonify({'message': 'Invalid credentials'}), 401