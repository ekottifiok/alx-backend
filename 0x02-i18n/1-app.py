#!/usr/bin/env py
"""Basic Flask app

Returns:
    _type_: _description_
"""
from flask import Flask, render_template
from flask_babel import Babel


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


@app.route('/')
def index() -> str:
    """index page

    Returns:
        str: _description_
    """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(debug=True)
