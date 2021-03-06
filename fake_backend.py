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

    def get_sensor_values(self):
        lines = open("/home/rich/code/flask-openzwave/sensors.csv", "r").readlines()
        return_list = []
        for line in lines:
            line = line[:-1]  # remove newline
            d = {'Date': line.split(',')[0], 'Temperature': line.split(',')[1], 'Humidity': line.split(',')[2],
                 'Lux': line.split(',')[3]}
            return_list.append(d)
        return return_list

    def get_temperature(self):
        return 22

    def start(self):
        print "Starting..."

    def stop(self):
        print "Stopping..."

