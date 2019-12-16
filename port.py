import socket
import argparse

def scan(ip):
    for port in range(0, 65535):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))
            if 0 == result:
                print("{}/tcp       open".format(port))
            sock.close()


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('ip_address', action="store")

    args = parser.parse_args()
    scan(args.ip_address)

if __name__ == "__main__":
    main()
