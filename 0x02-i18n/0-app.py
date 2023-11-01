#!/usr/bin/env python3
"""
Basic Flask app that serves an HTML page with title and header
"""

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.htmk')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
