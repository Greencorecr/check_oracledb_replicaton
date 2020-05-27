import random

if int(round(random.random())):
    pri_status="Online"
else:
    pri_status="Offline"
if int(round(random.random())):
    status="Up"
else:
    status="Down"
print("Primary Status:\t\t"+pri_status)
print("ACFS Status:\t\t"+status)
