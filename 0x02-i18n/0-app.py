#!/usr/bin/env python3
"""
This module defines the root route.
"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def root():
    """
    Renders 'Hello world' on the browser when the root
    route is requested for.
    """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run()
