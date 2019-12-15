from zipfile import ZipFile
import sys

passwordList = input("Password list: ")
zipFile = input("Zip file: ")


with ZipFile(zipFile) as zf:
    with open(passwordList, "r") as f:
        for password in f:
            try:
                zf.extractall(pwd=password.strip().encode())

                print(f"Found: {password}")
                sys.exit()

            except RuntimeError:
                pass
