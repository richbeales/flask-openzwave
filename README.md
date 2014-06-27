flask-openzwave
===============

A basic http interface to python-openzwave using Flask

Created using Python 2.7, Flask (pip install Flask) and python-openzwave-0.2.4 (https://python-openzwave.googlecode.com/)

Created on debian/jessie x86 on an Asus EEEPC901, must be run as root to access the usb system

Using an Aeon Labs Z-Stick S2 USB controller, a Aeon Labs Multisensor and a TKBHome plug socket

Demo assumes the plug socket is node 3, and the usb stick is /dev/ttyUSB0.

The flask website runs in debug mode on http://localhost:5000 and has urls for checking values
(e.g. /values/Temperature) as well as controlling the switch (e.g. /switch/3/off).

Each time the temperature changes, it logs to a CSV file, and makes sure it's under 25 degrees C.  If it exceeds
25deg then it'll turn the socket on (e.g. to turn on a fan to stop a room getting too hot).

This will expand as I learn more about OZW and buy more devices :-)