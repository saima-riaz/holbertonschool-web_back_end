#!/usr/bin/env python3
"""
Session authentication views
"""
from flask import Flask, request, jsonify
from models.user import User  # Ensure you have User model imported
from api.v1.app import auth  # Import auth where needed to avoid circular import

app = Flask(__name__)

@app.route('/api/v1/auth_session/login', methods=['POST'], strict_slashes=False)
@app.route('/auth_session/login', methods=['POST'], strict_slashes=False)  # Slash tolerant
def login():
    """ Handles login for session authentication """
    email = request.form.get('email')
    password = request.form.get('password')

    # Check for missing email
    if not email:
        return jsonify({"error": "email missing"}), 400
    
    # Check for missing password
    if not password:
        return jsonify({"error": "password missing"}), 400

    # Retrieve User instance based on email
    user = User.search(email)
    if user is None:
        return jsonify({"error": "no user found for this email"}), 404

    # Check if the password is valid
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    # Create a session ID for the User ID
    session_id = auth.create_session(user.id)

    # Return the User JSON representation and set the session cookie
    response = jsonify(user.to_json())
    session_name = getenv('SESSION_NAME')  # Use the environment variable for cookie name
    response.set_cookie(session_name, session_id)  # Set the session cookie

    return response
