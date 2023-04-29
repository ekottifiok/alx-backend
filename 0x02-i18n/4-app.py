#!/usr/bin/env python3
"""Basic Flask app

Returns:
    _type_: _description_
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """configuration for the babel class
    """
    DEBUG = True
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)
app.url_map.strict_slashes = False


@babel.localeselector
def get_locale() -> str:
    """Create a get_locale function with the babel.localeselector
    decorator. Use request.accept_languages to determine the best
    match with our supported languages.

    Returns:
        str: _description_
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """index page

    Returns:
        str: _description_
    """
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run(debug=True)
