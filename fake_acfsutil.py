import random

if int(round(random.random())):
    pri_status="Running"
else:
    pri_status="Stopped"
if int(round(random.random())):
    status="Active"
else:
    status="Stopped"

print("Site:\t\t\t\tPrimary")
print("Primary hostname:\t\toracle.greencore.co.cr")
print("Primary path:\t\t\t/Historico")
print("Primary status:\t\t\t"+pri_status)
print("Background Resources:\t\t"+status)
