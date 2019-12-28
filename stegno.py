#!/usr/bin/env python
# -*- coding: utf8 -*-

# library
import sys

def usage():
    print("""Stegno Tool

Usage: stegno.py -h file_name
--help               -  show this help message and exit
-h, --hide           -  file name to hide
-t, --text           -  set a text
-e, --extract        -  file name to extract

Examples:
./stegno.py -h pic.png -t text
./stegno.py -e pic.png
""")

def main():
    # no fancy command-line parsing here
    if not len(sys.argv[1:]):
        usage()

    # read the command-line options
    try:
        opts, args = getopt.getopt(sys.argv[1:], ":ht:e:", ["help", "hide", "text", "extract"])
    except getopt.GetoptError as e:
        print(str(e))
        usage()

    for o, a in opts:
        if o in ("--help"):
            usage()
        elif o in ("-h", "--hide"):
            hide = a
        elif o in ("-t", "--text"):
            text = str(a)
        elif o in ("-e", "--extract"):
            extract = a
        else:
            assert False, "Unhandable Option"

    if not hide and text:
        if extract:



main()
