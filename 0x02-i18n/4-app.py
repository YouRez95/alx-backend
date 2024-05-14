#!/usr/bin/env python3
'''
    Basic Babel setup
'''


from flask import Flask, render_template, request
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


@babel.localeselector
def get_locale() -> str:
    '''
        Retrieve the locale
    '''
    local = request.args.get('locale')
    if '|' in local:
        local = local[1:-1].split('|')
        for lang in local:
            if lang in app.config['LANGUAGES']:
                return lang

    if local in app.config['LANGUAGES']:
        return local
    request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def home_route() -> str:
    '''
        function that serve the route /
    '''
    return render_template('3-index.html')


if __name__ == "__main__":
    app.run(debug=True)
