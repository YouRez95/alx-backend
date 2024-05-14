#!/usr/bin/env python3
'''
    Basic Flask app
'''


from flask import Flask, render_template
from flask.typing import ResponseReturnValue

app = Flask(__name__)


@app.route('/')
def home_route() -> ResponseReturnValue:
    '''
        function that serve the route /
    '''
    return render_template('0-index.html')


app.run(debug=True)
