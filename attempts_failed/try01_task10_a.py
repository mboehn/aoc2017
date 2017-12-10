#!/usr/bin/env python3

import sys
import csv
from pprint import pprint
import collections
import operator

import func


INPUTFILE = '../task10.input'


def main():

    with open(file=INPUTFILE, mode='r') as fileinput:
        reader = csv.reader(fileinput, delimiter=",")
        lengths = list(map(int, list(reader)[0]))

    numbers = list(range(0, 255))
    pos = 0
    skip = 0
    lengths = lengths

    for length in lengths:
        pos2 = pos + length
        if pos > len(numbers):
            pos -= len(numbers)
        
        if pos2 > len(numbers):
            pos2 -= len(numbers)
        
        reverse = reversed(numbers[pos:pos2])
        numbers[pos:pos2] = reverse
        print("numbers: {}".format(numbers))

        print("pos before: {}".format(pos))
        pos = pos + length + skip
        print("pos after: {}".format(pos))
        print("skip length before: {}".format(skip))
        skip += 1
        print("skip length after: {}".format(skip))
        

        print()

    print(numbers[0] * numbers[1])
    # 8556 er ikke riktig (dette var med *...)
    # 185 er ikke riktig... (dette var med + istedet for *)



if __name__ == '__main__':
    if len(sys.argv) == 2:
        INPUTFILE = sys.argv[1]
    main()
