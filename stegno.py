#!/usr/bin/env python

# library
import sys, argparse, subprocess

def usage():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", metavar="FILE_NAME",
    help="set a file name to hide or to extract")
    parser.add_argument("-e", "--extract", action="store_true",
    help="extract hidden text from image ")
    if not len(sys.argv[1:]):
        subprocess.check_call(['bash', 'stegno.sh'])
    return parser.parse_args()

def main():
    args = usage()
    file = args.file
    if not args.extract:
        text = raw_input("Text: ")
        append = subprocess.call(['echo', '{} >> {}'.format(text, file)])
        print("Text has be hidden inside the image")
    else:
        text = subprocess.call(['echo', 'strings {} | tail -1'.format(file)])
        print("Text: {}".format(extract))

try:
    main()
except KeyboardInterrupt:
    sys.exit(0)
