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


@babel.localeselector
def get_locale():
    """
    Use request.accept_languages to determine the best
    match with supported languages.
    """
    return request.accept_languages.best_match(
            app.config['LANGUAGES'])


@app.route('/')
def root() -> str:
    """
    Renders 'Hello world' when a request is made to this route.
    """
    return render_template('2-index.html')


if __name__ == "__main__":
    app.run()
