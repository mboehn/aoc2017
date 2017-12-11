#!/usr/bin/env python3

import math
import sys
import csv
from pprint import pprint
import collections
import operator

import func


INPUTFILE = './task11.input'


def main():
    with open(file=INPUTFILE, mode='r') as fileinput:
        reader = list(csv.reader(fileinput, delimiter=','))

        storage = []

        x, y, z = 0, 0, 0
        for char in reader[0]:
#            print(char)
            if char == 'n':
                y += 1
                x -= 1
            elif char == 's':
                y -= 1
                x += 1
            elif char == 'ne':
                z -= 1
                y += 1
            elif char == 'sw':
                z += 1
                y -= 1
            elif char == 'se':
                z -= 1
                x += 1
            elif char == 'nw':
                z += 1
                x -= 1

            storage.append(max(abs(x), abs(y), abs(z)))
        #print((x, y, z))
        print(max(abs(x), abs(y), abs(z)))
        print(max(storage))


if __name__ == '__main__':
    if len(sys.argv) == 2:
        INPUTFILE = sys.argv[1]
    main()
