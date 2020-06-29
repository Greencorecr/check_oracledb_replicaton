#!/usr/bin/python3

"""
Nagios command for checking the status of an ACFS replication
Used to check the status of an OracleDB replication
Copyright 2020, Greencore Solutions
Licensed GPLv3
"""

import os
import sys

ACFS_COMMAND = "python3 fake_acfsutil.py"

primary = os.popen(ACFS_COMMAND+"|grep Primary\ status").readline().strip()
background = os.popen(ACFS_COMMAND+"|grep Background\ Resources").readline().strip()

if "Running" in primary and "Active" in background:
    print("OK - Cluster in sync.")
    sys.exit(0)
elif "Running" not in primary or "Active" not in background:
    print("CRITICAL - Check primary.")
    sys.exit(2)
else:
    print("UKNOWN - Manually check resources.")
    sys.exit(3)
