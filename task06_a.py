#!/usr/bin/env python3

import sys
import math
import csv
import itertools
from pprint import pprint
import operator

import func


INPUTFILE = './task06.input'


def loop_banks(banks):
    steps = 0
    states = {}

    # note to self. skjønne https://stackoverflow.com/questions/626759/whats-the-difference-between-lists-and-tuples
    # jeg prøvde på samme varianten istad, men av en eller annen grunn så fikk jeg det ikke til med lister
    while tuple(banks) not in states:
        states[tuple(banks)] = steps
        index, value = max(
            enumerate(banks),
            key=lambda k: (k[1], -k[0])
        )
        banks[index] = 0

        for loopindex in itertools.islice(
                itertools.cycle(range(
                    len(banks)
                    )),
                index + 1,
                index + value + 1):
            banks[loopindex] += 1
        steps += 1

    # print tar lang tid
#    pprint(states)
    return steps


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
