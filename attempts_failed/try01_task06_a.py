#!/usr/bin/env python3

import sys
import math
import csv
import itertools
from pprint import pprint
import operator

import func


INPUTFILE = '../task06.input'


def find_max(banks):

    max_value = 0
    max_index = []

    for index, value in enumerate(banks):
        if value > max_value:
            max_index = [index, ]
            max_value = value
        elif value == max_value:
            max_index.append(index)

    max_index = max(max_index)

    print("largest index: {}\t|\tlargest value: {}".format(max_index, max_value))
    return max_value, max_index


def loop_banks(banks):
    print("starting loop")
    states = []
    steps = 0

    while True:

        if states.count(banks) > 0:
            print("whaaaat.")
            print(banks)
            break

        steps += 1
        print("-----------")
        states.append(list(banks))
        max_value, max_index = find_max(banks)

        next_index = max_index + 1
        if next_index > len(banks):
            next_index = 0
        print("next index: {}".format(next_index))

        distribution_value = max_value / len(banks)
        distribution_value_self = math.ceil(distribution_value)
        if distribution_value % len(banks):
            distribution_value_self = math.floor(distribution_value)
        distribution_value = math.ceil(distribution_value)
        print("bank {} will be: {}".format(max_index, distribution_value_self))
        print("all other banks get {} added".format(distribution_value))

        for bi, bv in enumerate(banks):
            if bi != max_index:
                banks[bi] += distribution_value
            else:
                banks[bi] = distribution_value_self


        pprint(states)
    print()

    return(steps)


def main():
    with open(file=INPUTFILE, mode='r') as fileinput:
        reader = csv.reader(fileinput, delimiter="\t")
        banks = list(map(int, list(reader)[0]))

        print()
        steps = loop_banks(banks)
        print("this took... {} steps...".format(steps))
        
        


if __name__ == '__main__':
    if len(sys.argv) == 2:
        INPUTFILE = sys.argv[1]
    main()
