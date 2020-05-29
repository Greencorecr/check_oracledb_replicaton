#!/usr/bin/python
import os, sys
primary=os.popen("python3 fake_acfsutil.py|grep Primary\ status").readline().strip()
background=os.popen("python3 fake_acfsutil.py|grep Background\ Resources").readline().strip()

if "Running" in primary and "Active" in background:
        print("OK - Cluster in sync.")
        sys.exit(0)
elif "Running" not in primary:
        print("CRITICAL - Check primary.")
        sys.exit(2)
elif "Active" not in background:
        print("WARNING - Check background resources.")
        sys.exit(1)
else:
        print("UKNOWN - Manually check resources.")
        sys.exit(3)