#!/usr/bin/env python

# library
import sys, argparse, subprocess

def usage():
    parser = parser.ArgumentParser():
    parser.add_argument("-f", "--file", metavar="FILE_NAME",
    help="set a file name to hide or to extract")
    parser.add_argument("-e", "--extract", action="store_true",
    help="extract hidden text from image ")
    if not len(sys.argv[1:]):
        subprocess.call(['ls', '-l'])
    return parser.parse_args()

def main():
    args = usage()
    file = args.file
    if not args.extract:
        print(0)
    else:
        print(1)

main()
