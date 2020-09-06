#!/usr/bin/python3
""" Script that starts a Flask web application. """

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Returns a string at the root route """
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Returns a string at the /hbnb route """
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """ Returns a string at the /c/<text> route """
    text = text.replace('_', ' ')
    return "C {}".format(text)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
