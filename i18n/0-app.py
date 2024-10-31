#!/usr/bin/env python3
"""import module"""
from flask import Flask, render_template

app = Flask(__name__)


"""define route for root URL"""


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
