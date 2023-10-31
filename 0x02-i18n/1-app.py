#!/usr/bin/env python3
"""
This module introduces basic babel setup.
"""
from flask import Flask, render_template
from flask_babel import Babel
from typing import List
app = Flask(__name__)
# Instantiate Babel and store it in a module-level variable named 'babel'
babel = Babel(app)


class Config:
    """
    Configures available languages in our app.
    """
    LANGUAGES: List[str] = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# Set the Flask app's config from the Config class
app.config.from_object(Config)


@app.route('/')
def root():
    """
    Renders 'Hello world' when a request is made to this route.
    """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run()
