#!/usr/bin/env python3

import sys
import math
import csv
import itertools
from pprint import pprint

import func


INPUTFILE = './task05.input'


def main():
    with open(file=INPUTFILE, mode='r') as fileinput:
        lines = list(map(int, fileinput.readlines()))

        steps = 0
        index = 0
        reading = None

        # hvis index går under 0 eller over lengden på input, så er vi ute av labyrinten
        while index >= 0 and index < len(lines):
            reading = lines[index]

            if reading >= 3:
                lines[index] -= 1
            else:
                lines[index] += 1
            
            index += reading

            steps += 1
        

        print(steps)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        INPUTFILE = sys.argv[1]
    main()
