import re
import os

os.system("arp -a -n > /tmp/wifi.txt")

print("IP Adress        | MAC Adress")

with open("/tmp/wifi.txt", "r") as f:
    for device in f:
        IP = re.findall(r'\(.*\)', device)[0].replace("(", "").replace(")","")
        MAC = re.findall(r'at (.*) on', device)[0]
        print(f"{IP:<17}| {MAC}")
