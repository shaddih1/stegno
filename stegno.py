#!/usr/bin/env python
# -*- coding: utf8 -*-

# library
import sys, argparse, subprocess

def usage():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", metavar="FILE_NAME", help="set file name to hide or to extract")
    parser.add_argument("-e", "--extract", action="store_true", help="extract hidden text from image")
    # no fancy command-line parsing here
    if not len(sys.argv[1:]):
        subprocess.call(["ls", "-l"])
    return parser.parse_args()

def main():
    args = usage()
    if not args.extract:
        file = args.file
    else:
        print("error")



main()
