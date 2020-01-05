#!/usr/bin/env python
# -*- coding: utf8 -*-

# python standard library
import sys, argparse

def usage():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", metavar="FILE_NAME",
    help="set a file name to hide or to extract")
    parser.add_argument("-e", "--extract", action="store_true",
    help="extract hidden text from image ")

    return parser.parse_args()

def append(file_name):
    text = raw_input("Text: ")
    with open(file_name, 'a') as add:
        add.write('\n' + text)
        print("Text has be hidden inside the image")

def extract(file_name):
    with open(file_name, 'r') as text:
        lines = text.readlines()
        extract = [lines][-1][-1]

    return extract

def main():
    # parse args/options
    args = usage()
    file_name = args.file
    if file_name and not args.extract:
        append(file_name)
    else:
        print("Text: {}".format(extract(file_name)))

main()
