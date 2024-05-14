#!/usr/bin/env python3
'''
    Basic Flask app
'''


from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home_route():
    '''
        function that serve the route /
    '''
    return render_template('0-index.html')


app.run(debug=True)
