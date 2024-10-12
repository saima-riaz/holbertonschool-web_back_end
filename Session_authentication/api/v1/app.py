#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os
# Import the Auth class
from api.v1.auth.auth import Auth
from api.v1.auth.basic_auth import BasicAuth
from api.v1.auth.session_auth import SessionAuth


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

# Initialize the auth variable based on the AUTH_TYPE environment variable
auth = None
auth_type = getenv("AUTH_TYPE")
if auth_type == "session_auth":
    auth = SessionAuth()
else:
    from api.v1.auth.auth import Auth
    auth = Auth()


@app.before_request
def before_request_func():
    """ Method to filter requests before routing """
    if auth is None:
        return
    excluded_paths = ['/api/v1/status/',
                      '/api/v1/unauthorized/', '/api/v1/forbidden/']
    if not auth.require_auth(request.path, excluded_paths):
        return
    if auth.authorization_header(request) is None:
        return jsonify({"error": "Unauthorized"}), 401
    if auth.current_user(request) is None:
        return jsonify({"error": "Forbidden"}), 403


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized_error(error):
    """ Custom handler for 401 Unauthorized errors """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden_error(error):
    """ Custom handler for 403 Forbidden errors """
    return jsonify({"error": "Forbidden"}), 403


@app.before_request
def before_request_handler():
    """ Handler for filtering requests before they reach the view functions """
    if auth is None:
        return

    excluded_paths = ['/api/v1/status/', '/api/v1/unauthorized/',
                      '/api/v1/forbidden/']

    # If the request path does not require auth, continue
    if not auth.require_auth(request.path, excluded_paths):
        return

    # If there is no authorization header, abort with 401 Unauthorized
    if auth.authorization_header(request) is None:
        abort(401)

    # If the current user is not found, abort with 403 Forbidden
    request.current_user = auth.current_user(request)
    if auth.current_user(request) is None:
        abort(403)


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
