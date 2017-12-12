#!/usr/bin/env python3

import math
import sys
import csv
from pprint import pprint
import collections
import operator

import func


INPUTFILE = './task12.input'

def group(start, pipes):
    group = {start}
    q = {start}
    while q:
        next_q = set()
        for i in q:
            next_q.update(pipes[i])
        q = next_q - group
        group.update(next_q)
    return group


def main():
    pipes = {}
    with open(file=INPUTFILE, mode='r') as fileinput:
        for line in fileinput:
            pid, _, children = line.split(maxsplit=2)
            pipes[int(pid)] = set(map(int, children.split(', ')))
    start = 0
    print(len(group(start, pipes)))


    rest = set(pipes)
    print(rest)
    count = 0
    while rest:
        count += 1
        curr = group(rest.pop(), pipes)
        rest -= curr
        print(rest)
    print(count)
    # 2000 er for høyt



if __name__ == '__main__':
    if len(sys.argv) == 2:
        INPUTFILE = sys.argv[1]
    main()
