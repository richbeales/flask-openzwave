#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from louie import dispatcher
import sys
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('openzwave')

from openzwave.network import ZWaveNetwork
from openzwave.option import ZWaveOption
import time

started = False


class Backend():

    def __init__(self):
        device = "/dev/ttyUSB0"
        options = ZWaveOption(device, config_path="/home/rich/openzwave/config", user_path=".", cmd_line="")
        options.set_log_file("OZW_Log.log")
        options.set_append_log_file(False)
        options.set_console_output(False)
        options.set_save_log_level('Debug')
        options.set_logging(True)
        options.lock()

        self.values = {}
        dispatcher.connect(self._network_started, ZWaveNetwork.SIGNAL_NETWORK_STARTED)
        dispatcher.connect(self._network_failed, ZWaveNetwork.SIGNAL_NETWORK_FAILED)
        dispatcher.connect(self._network_ready, ZWaveNetwork.SIGNAL_NETWORK_READY)
        self.network = ZWaveNetwork(options, autostart=False)

    def _network_started(self, network):
        print("network started - %d nodes were found." % network.nodes_count)

    def _network_failed(self, network):
        print("network failed :(")

    def _network_ready(self, network):
        print("network : ready : %d nodes were found." % network.nodes_count)
        print("network : controller is : %s" % network.controller)
        dispatcher.connect(self._node_update, ZWaveNetwork.SIGNAL_NODE)
        dispatcher.connect(self._value_update, ZWaveNetwork.SIGNAL_VALUE)

    def _node_update(self, network, node):
        print('node update: %s.' % node)

    def _value_update(self, network, node, value):
        print('value update: %s is %s.' % (value.label, value.data))
        self.values[value.label] = value.data
        if value.label == 'Temperature':
            self.process_temp_change(value.data)

    def process_temp_change(self, value):
        if value > 25:
            print('too hot - turn on fan')
            self.switch_on(3)
        else:
            print('cool enough - turn off fan')
            self.switch_off(3)
        with open("temperature.csv", "a") as temp_log_file:
            temp_log_file.write("%s,%s\n" % (datetime.date().strftime("%c"), value))

    def switch_on(self, name):
        print("Activating switch %s" % name)
        parsed_id = 0
        try:
            parsed_id = int(name)
        except ValueError:
            pass
        for key, node in self.network.nodes.iteritems():
            if node.name == name or node.node_id == parsed_id:
                for val in node.get_switches():
                    node.set_switch(val, True)

    def switch_off(self, name):
        print("Deactivating switch %s" % name)
        parsed_id = 0
        try:
            parsed_id = int(name)
        except ValueError:
            pass
        for key, node in self.network.nodes.iteritems():
            if node.name == name or node.node_id == parsed_id:
                for val in node.get_switches():
                    node.set_switch(val, False)

    def start(self):
        global started
        if started:
            return
        started = True
        self.network.start()

        print "Starting..."
        for i in range(0, 90):
            if self.network.state >= self.network.STATE_READY:
                break
            else:
                sys.stdout.write(".")
                sys.stdout.flush()
                time.sleep(1.0)

    def stop(self):
        self.network.stop()
