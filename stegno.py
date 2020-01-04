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
    with open(file, 'a') as append:
        append.write(text)
    print("Text has be hidden inside the image")

def extract(file_name):
    with open(file_name, 'r') as text:
        line = text.readlines()
        extract = [line]

    return extract[-1][-1]

def main():
    # parse args/options
    args = usage()
    file_name = args.file
    if not args.extract:
        append(file_name)
    else:
        print("Text: {}".format(extract()))

main()
