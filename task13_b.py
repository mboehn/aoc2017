#!/usr/bin/env python3

import math
import sys
import csv
from pprint import pprint
import collections
import operator

import func


INPUTFILE = './task13.input'

MY_DEPTH = 0

def main():
    layers = {}
    with open(file=INPUTFILE, mode='r') as fileinput:
        for line in fileinput:
            layer, depth = line.strip().split(': ')
            layers[int(layer)] = int(depth)

    #pprint(layers)

    delay = 0
    last_layer = max(layers) # layer num is the key

    while True:
        position = 0
        severity = 0
        hits = 0
        while position <= last_layer:
#            print("** current position is: {}".format(position))

            try:
                current_depth = layers[position]
#                print("** this layer has a depth of {}".format(current_depth))
            except:
                current_depth = None
#                print("** no scanner at this layer")

            if current_depth:
                scanner_position = (delay + position) % ((current_depth - 1) * 2)
#                print("** the scanner at this layer has a position of: {}".format(scanner_position))

                if scanner_position == MY_DEPTH:
#                    print("!! i was hit by the scanner! adding to severity...")
                    severity += position * current_depth
                    hits += 1

#            print()
            position += 1
#        print("== severity is {}".format(severity))

        if hits == 0:
            print("++ escaped without hits")
            print("== delay was {}".format(delay))
            break
#        print("-- new round. delay was {}".format(delay))
#        print()
        delay += 1



if __name__ == '__main__':
    if len(sys.argv) == 2:
        INPUTFILE = sys.argv[1]
    main()
