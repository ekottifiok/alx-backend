#!/usr/bin/env py
"""Basic Flask app

Returns:
    _type_: _description_
"""
from flask import Flask, g, render_template, request
from flask_babel import Babel
from typing import (
    Dict,
    Union
)


class Config:
    """configuration for the babel class
    """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)
app.url_map.strict_slashes = False
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@babel.localeselector
def get_locale() -> str:
    """Create a get_locale function with the babel.localeselector
    decorator. Use request.accept_languages to determine the best
    match with our supported languages.

    Returns:
        str: _description_
    """
    return str(
        request.accept_languages.best_match(app.config["LANGUAGES"])
    )
    

@app.before_request
def before_request() -> None:
    """Performs some routines before each request's resolution.
    """

    g.user = get_user()


@app.route('/')
def index() -> str:
    """index page

    Returns:
        str: _description_
    """
    return render_template('1-index.html')


def get_user() -> Union[Dict, None]:
    """returns a user dictionary or None if the
    ID cannot be found or if login_as was not passed.

    Returns:
        Union[Dict, None]: _description_
    """
    return users.get(
        request.args.get('login_as'),
        None
    )


if __name__ == "__main__":
    app.run(debug=True)
