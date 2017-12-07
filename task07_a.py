#!/usr/bin/env python3

import sys
import math
import csv
import itertools
from pprint import pprint
import operator
from collections import Counter


import func


INPUTFILE = './task07.input'


def main():

    programs = []

    with open(file=INPUTFILE, mode='r') as fileinput:
        reader = csv.reader(fileinput, delimiter=" ")

        for row in reader:
            row = [n.strip(',') for n in row]
            try:
                del row[2]
            except:
                pass
            del row[1]
#            print(row)
            programs = programs + row

    counter = Counter(programs)
    print(set(counter.most_common()[:-1-1:-1]))

if __name__ == '__main__':
    if len(sys.argv) == 2:
        INPUTFILE = sys.argv[1]
    main()
