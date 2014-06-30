#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Backend():

    def __init__(self):
        self.values = {"Temperature": 22}

    def switch_on(self, name):
        print("Activating switch %s" % name)

    def switch_off(self, name):
        print("Deactivating switch %s" % name)

    def get_switch_status(self, name):
        print("Querying switch %s" % name)
        return True

    def get_sensor_json(self):
        lines = open("/home/rich/code/flask-openzwave/sensors.csv", "r").readlines()
        json = []
        for line in lines:
            json.append('{"Date":"%s","Temperature":"%s","Humidity":"%s","Lux":"%s"}' % tuple(line.split(',')))
        return json

    def get_temperature(self):
        return 22

    def start(self):
        print "Starting..."

    def stop(self):
        print "Stopping..."

