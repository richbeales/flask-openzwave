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

    def get_temperature(self):
        return 22

    def start(self):
        print "Starting..."

    def stop(self):
        print "Stopping..."

