#!/usr/bin/env python3
"""
Module emulates a user login system
"""

import pytz
from flask import Flask, render_template, request, g
from flask_babel import Babel, _

app = Flask(__name__)
babel = Babel(app)

class Config:
    """
    Defines a class with a LANGUAGES class attribute equal to ["en", "fr"]
    """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


# Mock user table
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_user(user_id):
    """
    returns a user dictionary or None if the ID cannot be found
    or if login_as was not passed.
    """
    return users.get(user_id)

def is_valid_timezone(timezone):
    """
    returns a valid timezone
    """
    try:
        pytz.timezone(timezone)
        return True
    except pytz.exceptions.UnknownTimeZoneError:
        return False

@app.route('/')
def hello_world():
    """
    returns a html template that prints
    `Welcome to Holberton` as a title
    and `Hello world`as a header
    """
    return render_template('index.html')

@babel.localeselector
def get_locale():
    """
    Check if the incoming request contains locale argument
    ----
    if value is a supported locale, return it.
    If not or if the parameter is not present,
    resort to the previous default behavior.
    """
    if "locale" in request.args:
        if request.args["locale"] in app.config["LANGUAGES"]:
            return request.args["locale"]
    elif (
        g.user
        and g.user.get("locale")
        and g.user.get("locale") in app.config["LANGUAGES"]
    ):
        return g.user.get("locale")
    else:
        return request.accept_languages.best_match(app.config["LANGUAGES"])


@babel.timezoneselector
def get_timezone():
    """
    returns a timezone
    ---
    Gets timezone parameter in URL parameters or from user settings
    validate that it is a valid time zone
    """
    if 'timezone' in request.args and is_valid_timezone(request.args['timezone']):
        return request.args['timezone']

    # Check for the timezone from the user's settings
    if g.user and g.user.get('timezone') and is_valid_timezone(g.user.get('timezone')):
        return g.user.get('timezone')

    # Default to UTC if no valid timezone is found
    return app.config['BABEL_DEFAULT_TIMEZONE']

# Define the before_request function to set the user as a global on flask.g
@app.before_request
def before_request():
    """
    uses get_user to find a user if any,
    and set it as a global on flask.g.user.
    """
    user_id = request.args.get('login_as')
    g.user = get_user(int(user_id)) if user_id else None

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

