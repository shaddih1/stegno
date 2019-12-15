from hashlib import *
import sys
import requests
import re

def encrypt():
    encryptionList = ["md5", "sha1", "sha224", "sha256", "sha384", "sha512"]
    encryptionMenu = """
╭────────────────────────────╮
│ [01] md5       [02] sha1   │
│ [03] sha224    [04] sha256 │
│ [05] sha384    [06] sha512 │
╰────────────────────────────╯"""

    print(encryptionMenu)
    choice = input("Choose encryption method: ")
    choice = choice.lstrip("0")
    text = input("Text: ")

    if  1 <= int(choice) <= 6:
        encryption = encryptionList[int(choice)-1]
        print("Hash: " + eval(encryption+"(b\"{}\").hexdigest()".format(text)))
    else:
        print("Invalid choice")


def crack():
    encryptionList= ["md5", "sha1", "sha224", "sha256", "sha384", "sha512"]
    encryptionMenu= """
╭────────────────────────────╮
│ [01] md5       [02] sha1   │
│ [03] sha224    [04] sha256 │
│ [05] sha384    [06] sha512 │
╰────────────────────────────╯"""

    print(encryptionMenu)
    choice = input("Choose encryption: ")
    hashvalue = input("Hash: ")
    if  1 <= int(choice) <= 6:

        online = input("Crack using online resource? [y/N]: ")
        if online.lower().strip() == "n" or "":
            fname = input("File name with passwords: ")
            with open(fname, "r") as f:
                for password in f:
                    encryption = encryptionList[int(choice)-1]
                    if eval(encryption+"(b\"{}\").hexdigest()".format(password.strip())) == hashvalue:
                        print("Text:", password.strip())
                        sys.exit()
                    else:
                        pass
                print("Was not able to crack, try online method")

        else:
            headers = {
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
                }
            r = requests.get('https://hashtoolkit.com/reverse-hash/?hash=' + hashvalue, headers=headers).text
            try:
                text = re.findall(r'hash">(.*)<\/span>', r)[2]
            except:
                print("Was not able to crack, try password list method")
                sys.exit()

            print("Text:", text)
    else:
        print("Invalid choice")


def main():
    choiceMenu = """
╭───────────────────╮
│ [01] Encrypt text │
│ [02] Crack a hash │
╰───────────────────╯"""
    print(choiceMenu)

    choice = input("Choose a function to perform: ")
    choice = choice.lstrip("0")

    if int(choice) == 1:
        encrypt()
    elif int(choice) == 2:
        crack()
    else:
        print("Invalid choice")
        sys.exit()


main()
