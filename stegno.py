#!/usr/bin/env python
# -*- coding: utf8 -*-

# library
import sys
import os
import subprocess
import argparse

def usage():
    parser = argparse.ArgumentParser()
    parser.add_argument("-w", "--wrap", metavar="FILE_NAME", help="set a file name")
    parser.add_argument("-t", "--text", metavar="\"TEXT\"", help="set a text to hide")
    parser.add_argument("-e", "--extract", metavar="FILE_NAME", help="set a file name")
    # no fancy command-line parsing here
    if not len(sys.argv[1:]):
        subprocess.call(['bash', 'stegno.sh'])
    return parser.parse_args()

def shutdown():
    print("[Error] - Badly combined commands")
    print("$ python stegno.py -h")
    sys.exit(0)

def append(wrap, text):
    os.system('echo {} >> {}'.format(text, wrap))

def extract(extract):
    os.system('echo $(strings {} | tail -1)'.format(extract))

def main():
    args = usage()
    if not args.wrap and not args.text:
        if args.extract:
            extract(args.extract)
    elif args.wrap and args.text:
        if not args.extract:
            append(args.wrap, str(args.text))
        else:
            shutdown()
    else:
        shutdown()

main()
