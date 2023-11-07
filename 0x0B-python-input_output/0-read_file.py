#!/usr/bin/python3

""" Where the functions to read a file is stored """

def read_file(filename=""):
    """ function that reads a text file
    Args:
        filename: filename

    """

    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            print(line, end='')
