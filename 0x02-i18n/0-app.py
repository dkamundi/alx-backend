#!/usr/bin/env python3
"""
Basic Flask app that serves an HTML page with title and header
"""

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def hello_world():
    """
    returns a html template that prints
    `Welcome to Holberton` as a title
    and `Hello world`as a header
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
