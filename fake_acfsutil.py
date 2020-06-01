#!/usr/bin/python3
"""
Script used in testing of the Nagios command
It fakes the information acfsutil would print, with random to check the
different possible states.
Copyright 2020, Greencore Solutions
Licensed GPLv3
"""

import random

if int(round(random.random())):
    PRI_STATUS = "Running"
else:
    PRI_STATUS = "Stopped"
if int(round(random.random())):
    STATUS = "Active"
else:
    STATUS = "Stopped"

print("Site:\t\t\t\tPrimary")
print("Primary hostname:\t\toracle.greencore.co.cr")
print("Primary path:\t\t\t/Historico")
print("Primary status:\t\t\t"+PRI_STATUS)
print("Background Resources:\t\t"+STATUS)
