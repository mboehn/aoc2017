#!/usr/bin/env python3

import math
import csv
import itertools
from pprint import pprint

import func


INPUT = (58, 99, 158, 265149) # skal være 265149, de andre er kun for å kontrollregne enklere
#INPUT = (99,)


def main(goal):

    value = get_value(goal)
    print("first value larger than {} is: {}".format(goal, value))


def sum_spiral():
    matrix = {(0, 0) : 1}
    x, y = 0, 0

    # lambda ble enklere, da slipper jeg å ta med variablene ut, men jeg syns syntaxen nok er i styggeste laget.
    # burde sikkert vært en funksjon om jeg bare hadde orka å finne ut av variabelscope-problematikken min. 
    # og jeg som nettopp trodde jeg hadde fått kontroll på det... jaja.
    sumnear = lambda x, y: sum(matrix.get((x2, y2), 0)
                          for x2 in range(x-1, x+2)
                          for y2 in range(y-1, y+2)
                         )


    for run in itertools.count(1, 2):
        # bare looper, så trenger ikke variablet, bruker _ selv om det tydeligvis ikke egentlig er en dummy.
        for _ in range(run):
            x += 1
            matrix[x, y] = sumnear(x, y)
            yield matrix[x, y]

        for _ in range(run):
            y -= 1
            matrix[x, y] = sumnear(x, y)
            yield matrix[x, y]

        for _ in range(run + 1):
            x -= 1
            matrix[x, y] = sumnear(x, y)
            yield matrix[x, y]

        for _ in range(run + 1):
            y += 1
            matrix[x, y] = sumnear(x, y)
            yield matrix[x, y]
        #pprint(matrix)
        # hm, okay, det ser ut som det blir omvendte koordinater av en eller annen grunn.
        # det har vel ikke noe å si så lenge jeg får samme verdiene...?
        # det syns bare hvis man faktisk ser på matrisa, og det kommenterer jeg vekk :-P


def get_value(goal):
    for value in sum_spiral():
        if value > goal:
            return value


if __name__ == '__main__':
    for goal in INPUT:
        print("{}---------------{}".format(func.bcolors.HEADER, func.bcolors.ENDC))
        main(goal)
        print()
