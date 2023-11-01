#!/usr/bin/env python3
"""
Basic Flask app with Flask-Babel extension.
"""
from flask import Flask, render_template
from flask_babel import Babel


app = flask(__name)


babel = Babel(app)


class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/')
def index():
    return render_template('1-index.html')


if __name__ == '__main""':
    app.run(host='0.0.0.0', port=5000)