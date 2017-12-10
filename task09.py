#!/usr/bin/env python3

import sys
import csv
from pprint import pprint
import collections
import operator

import func


INPUTFILE = './task09.input'


def main():

    with open(file=INPUTFILE, mode='r') as fileinput:
        line = list(fileinput)[0].strip()

        index = 0
        garbage = False
        storage = []
        score_total = 0
        score = 0
        while index < len(line):
            #print(line[index])

            if line[index] == '!':
                # escape
                index += 1
            elif garbage:
                if line[index] == '>':
                    garbage = False
            elif line[index] == '{':
                score += 1
                storage.append(score)
            elif line[index] == '<':
                garbage = True
            elif line[index] == '}':
                score -= 1
                score_total += storage.pop()
            index += 1
        print("part 1: {}".format(score_total))


if __name__ == '__main__':
    if len(sys.argv) == 2:
        INPUTFILE = sys.argv[1]
    main()
