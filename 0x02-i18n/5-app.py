#!/usr/bin/env python3
'''
    Basic Babel setup
'''


from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config:
    '''
        config class for the flask app
    '''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
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


def get_user(user_id, users):
    if user_id and int(user_id) in users.keys():
        return users[int(user_id)]
    return None


@app.before_request
def before_request():
    user_id = request.args.get('login_as')
    user = get_user(user_id, users)
    g.user = user


@babel.localeselector
def get_locale() -> str:
    '''
        Retrieve the locale
    '''
    local = request.args.get('locale')
    if local and '|' in local:
        local = local[1:-1].split('|')
        for lang in local:
            if lang in app.config['LANGUAGES']:
                return lang

    if local in app.config['LANGUAGES']:
        return local
    request.accept_languages.best_match(app.config['LANGUAGES'])
# babel.init_app(app, locale_selector=get_locale)


@app.route('/')
def home_route() -> str:
    '''
        function that serve the route /
    '''
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run(debug=True)
