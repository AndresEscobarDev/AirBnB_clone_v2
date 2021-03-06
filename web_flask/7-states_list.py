#!/usr/bin/python3
""" Script that starts a Flask web application. """

from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ Returns a template at the /states_list route """
    states = sorted([v for v in storage.all().values()])
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(error):
    """ Closes the storage on teardown """
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
