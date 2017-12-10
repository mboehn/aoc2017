#!/usr/bin/env python3

import math
import sys
import csv
from pprint import pprint
import collections
import operator

import func


INPUTFILE = './task10.input'

SIZE = 256
BLOCKSIZE = int(math.sqrt(SIZE))
ROUNDS = 64
SUFFIX = [17, 31, 73, 47, 23]


def main():

    lengths = []
    with open(file=INPUTFILE, mode='r') as fileinput:
        # her glemte jeg å tenke på newline.... strip() er fint!
        for char in fileinput.readline().strip():
            lengths.append(ord(char))

    lengths.extend(SUFFIX) # suffix per instructions

    # note to self: må skjønne range (det er vel matteproblemet mitt igjen, tenker jeg)
    # ser ut som jeg bomma her en stund, tok range(0, 255), men det skulle være
    # 'list of numbers from 0 to 255'...
    numbers = collections.deque(list(range(SIZE)))
    pos = 0
    skip = 0
    lengths = lengths
    print(lengths)
    for _ in range(ROUNDS):
        for length in lengths:
            numbers.rotate(-pos)
            rotated_numbers = list(numbers) # må lage ny liste, ikke bare referere til numbers.
            rotated_numbers[:length] = reversed(rotated_numbers[:length])
            numbers = collections.deque(rotated_numbers)
            numbers.rotate(pos)
            pos = (pos + length + skip) % len(numbers)
            skip += 1

    sparse = list(numbers)
    #blocks = [numbers[i:i + BLOCKSIZE] for i in range(0, len(numbers), BLOCKSIZE)]
    dense = []
    for block in range(0, len(sparse), BLOCKSIZE):
        res = 0
        group = sparse[block: block+BLOCKSIZE]
        print()
        print("group: {}".format(group))
        # ikke den peneste måten, men jeg måtte debugge. hadde en forløkke her tidligere :-P
        res = group[0] ^ group[1] ^ group[2] ^ group[3] ^ group[4] ^ group[5] ^group[6] ^ group[7] ^ group[8] ^ group[9] ^ group[10] ^ group[11] ^ group[12] ^ group[13] ^ group[14] ^ group[15]
        dense.append(res)
        print("dense: {}".format(dense))

    # .strip('0x') fjerner visst begge chars, ikke stringen '0x'...
    #print("".join([hex(i).replace('0x', '') for i in dense])) # leading zeroes forsvinner nok her....
    print("".join(list(map(lambda x: "{:02x}".format(x), dense))))


if __name__ == '__main__':
    if len(sys.argv) == 2:
        INPUTFILE = sys.argv[1]
    main()
