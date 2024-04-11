#!/usr/bin/env python3
"""Flask App Module"""

from flask import Flask, render_template, request
from flask import g
from flask_babel import Babel


class Config(object):
    """configuration class for flask_babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = LANGUAGES[0]
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(user_id):
    """retrive a user data"""
    if user_id is not None:
        user = users.get(int(user_id))
        if user is not None:
            return user
    return None


@app.before_request
def before_request():
    """method execute before every request"""
    g.user = get_user(request.args.get("login_as"))


@babel.localeselector
def get_locale():
    """determine the best match with our supported languages"""
    if 'locale' in request.args:
        locale = request.args['locale']
        if locale in Config.LANGUAGES:
            return locale

    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route('/', strict_slashes=False)
def index():
    """render index.html file"""

    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(port="5000", host='0.0.0.0', debug=True)
