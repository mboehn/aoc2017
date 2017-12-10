#!/usr/bin/env python3

import sys
import csv
from pprint import pprint
import collections
import operator

import func


INPUTFILE = './task10.input'


def main():

    with open(file=INPUTFILE, mode='r') as fileinput:
        reader = csv.reader(fileinput, delimiter=",")
        lengths = list(map(int, list(reader)[0]))

    # note to self: må skjønne range (det er vel matteproblemet mitt igjen, tenker jeg)
    # ser ut som jeg bomma her en stund, tok range(0, 255), men det skulle være
    # 'list of numbers from 0 to 255'...
    numbers = collections.deque(list(range(0, 256)))
    pos = 0
    skip = 0
    lengths = lengths

    for length in lengths:
        numbers.rotate(-pos)
        rotated_numbers = list(numbers) # må lage ny liste, ikke bare referere til numbers.
        rotated_numbers[:length] = reversed(rotated_numbers[:length])
        numbers = collections.deque(rotated_numbers)
        numbers.rotate(pos)
        pos = (pos + length + skip) % len(numbers)
        skip += 1

    print(numbers)
    print(numbers[0] * numbers[1])

    # 32220 is too high

        
if __name__ == '__main__':
    if len(sys.argv) == 2:
        INPUTFILE = sys.argv[1]
    main()
