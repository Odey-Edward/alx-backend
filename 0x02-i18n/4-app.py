#!/usr/bin/env python3
"""Flask App Module"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """configuration class for flask_babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = LANGUAGES[0]
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """determine the best match with our supported languages"""
    if 'locale' in request.args:
        locale = request.args['locale']
        if locale in Config.LANGUAGES:
            return locale

    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route('/')
def index():
    """render index.html file"""

    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(debug=True)
