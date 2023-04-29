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

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"
    



app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
babel = Babel(app)

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
babel.init_app(app, locale_selector=get_locale)
app.config.from_object(Config)
app.url_map.strict_slashes = False


@app.route('/')
def index() -> str:
    """index page

    Returns:
        str: _description_
    """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(debug=True)
