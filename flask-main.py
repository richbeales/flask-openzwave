#! /usr/bin/env python

import sys
import os
file_path = os.path.dirname(__file__)
sys.path.insert(0, file_path)

from flask import Flask
from backend import Backend

app = Flask(__name__)
backend = Backend()
backend.start()

@app.route('/')
def index():
    return 'Welcome to Flask OpenWave!'

@app.route('/values/<value>')
def values(value):
    try:
        return "Value for %s is %s" % (value, backend.values[value])
    except KeyError:
        return "Value %s not found" % value

@app.route('/switch/<node>/<on_or_off>')
def switch(node, on_or_off):
    if on_or_off == 'on':
        backend.switch_on(node)
    else:
        backend.switch_off(node)
    return "switch %s switched %s" % (node, on_or_off)

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', debug=True, use_reloader=False)
    except KeyboardInterrupt:
        backend.stop()
