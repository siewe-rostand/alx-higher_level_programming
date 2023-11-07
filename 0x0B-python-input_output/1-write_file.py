#!/usr/bin/python3
""" Module that contains a function that returns the number of lines
    of a text file
"""


def number_of_lines(filename=""):
    """Count number of lines in file
    Args:
        filename (str): string of path to file
    Returns:
        number of lines in file

    """
    nb_lines = 0
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            nb_lines += 1
    return nb_lines
