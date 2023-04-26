#!/usr/bin/env python3
"""Basic Flask app

Returns:
    _type_: _description_
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index() -> str:
    """index page

    Returns:
        str: _description_
    """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(debug=True)
