#! /usr/bin/env python

import sys
import os
file_path = os.path.dirname(__file__)
sys.path.insert(0, file_path)

from flask import Flask, render_template
from backend import Backend
#from fake_backend import Backend

app = Flask(__name__)

backend = Backend()


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/values/<value>')
def values(value):
    try:
        return "Value for %s is %s" % (value, backend.values[value])
    except KeyError:
        return "Value %s not found" % value


@app.route('/temperature')
def temperature():
    return backend.get_temperature()

@app.route('/json/values')
def json_values():
    return "%s" % backend.get_sensor_json()

@app.route('/switch/<node>/<on_off_check>')
def switch(node, on_off_check):
    if on_off_check == 'on':
        backend.switch_on(node)
        return "switch %s switched on" % node
    elif on_off_check == 'off':
        backend.switch_off(node)
        return "switch %s switched on" % node
    elif on_off_check == 'check':
        val = backend.get_switch_status(node)
        if val:
            return "switch %s is currently on" % node
        else:
            return "switch %s is currently off" % node
    else:
        return "unrecognised command - choose on/off/check"

if __name__ == '__main__':
    try:
        backend.start()
        app.run(host='0.0.0.0', debug=True, use_reloader=False)
    except KeyboardInterrupt:
        backend.stop()
