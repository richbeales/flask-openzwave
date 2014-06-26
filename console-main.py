#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from backend import Backend

backend = Backend()
backend.start()
while True:  # spin the main thread, wait for notifications from sensors
    try:
        time.sleep(0.5)
    except KeyboardInterrupt:
        break
backend.stop()
print "Finished"