#!/usr/bin/env python
# -*- coding: utf8 -*-

# python standard library
import sys, argparse, subprocess

def usage():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", metavar"FILE_NAME",
    help="set a file name to hide or to extract")
    parser.add_argument("-e", "--extract", action="store_true",
    help="extract hidden text from image ")

    return parser.parse_args()

def main():
    # parse args/options
    args = usage()
    file = args.file
    if file and not a:
        text = raw_input("Text: ")
        append = subprocess.call(['echo {} >> {}'.format(text, file)], shell=True)
        print("Text has be hidden inside the image")
    else:
        text = subprocess.call(['echo', 'strings {} | tail -1'.format(file)])
        print("Text: {}".format(extract))

if __name__ == '__main__':
    try:
        main()
    except (KeyboardInterrupt):
        pass
    finally:
        print("")
