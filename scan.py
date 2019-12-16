import re
import os
import requests

def vendor(mac):
    r = requests.get(f"https://macvendors.co/api/{mac}")

    if r.status_code != 404:
        return r.json().get("result").get("company")

    return "N/A"

def main():
    os.system("arp -a -n > /tmp/wifi.txt")

    print("IP Adress       | MAC Adress        | Vendor")

    with open("/tmp/wifi.txt", "r") as f:
        count = 0
        for device in f:
            IP = re.findall(r'\(.*\)', device)[0].replace("(", "").replace(")","")
            MAC = re.findall(r'at (.*) on', device)[0]
            print(f"{IP:<16}| {MAC:<17} | {vendor(MAC)}")
            count+=1
        print(f"Total devices: {count}")

main()
