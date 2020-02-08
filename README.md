# Stegno

![language](https://img.shields.io/badge/language-shell-green.svg)
![language](https://img.shields.io/badge/language-python-blue.svg)

## About

      Hide text inside image and Extract hidden text from image

## Python Module
      
      sys, argparse
      
   How to install argparse
      
      easy_install pip && pip install argparse
     
## Menu

      [1] Hide text inside image
      [2] Extract hidden text from image
            
      Chose option:

## Usage

      usage: stegno.py [-h] [-f FILE_NAME] [-e]

      optional arguments:
        -h, --help            show this help message and exit
        -f FILE_NAME, --file FILE_NAME
                        set a file name to hide or to extract
        -e, --extract         extract hidden text from image
 
 ## Examples 

     $ python stegno.py -f pic.png      ----->   Hide text inside image
     $ python stegno.py -f pic.png -e   ----->   Extract hidden text from image
     $ bash stegno.sh                   ----->   Interactive menu
