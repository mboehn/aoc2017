#!/usr/bin/env python3

import sys
import math
import csv
import itertools
from pprint import pprint
import operator
from collections import Counter


### endte opp med å ikke bruke anytree
#from anytree.importer import DictImporter
#from anytree import RenderTree
#from anytree.exporter import DotExporter
###

import func


INPUTFILE = './task07.input'


# note to self: i classmethods, så kan ikke class-referansen hete `class`,
# ser ut som de fleste bruker `cls` istedet

# note to self: masse nytt lært om klasser. får prøve å huske på noe av det.

class Program():
    # denne var smart, må huske på denne. kjekk plass å lagre det!
    programs = {}

    def __init__(self, row):
        self.name = row[0]
        self.weight = int(row[1][1:-1])
        self._children = []
        self.parent = None # placeholder for collect_parents()
        self.depth = 0 # placeholder for collect_depths()
        self.total_weight = self.weight # self.weight + childrens weight. see collect_weights()
        if "->" in row:
            self._children = [child.strip(',') for child in row[3:]]
        Program.programs[self.name] = self

    # dette blir jo part 1-svaret
    @classmethod
    def get_root(cls):
        first = list(cls.programs.values())[0]
        while first.parent is not None:
            first = first.parent
        return first

    @classmethod
    def collect_weights(cls):
        for program in sorted(cls.programs.values(), key=lambda k: k.depth, reverse=True):
            program.total_weight += sum(p.total_weight for p in program.children)

    @classmethod
    def collect_depths(cls):
        queue = [cls.get_root(), ]
        while queue:
            parent = queue.pop(0)
            for program in parent.children:
                program.depth = parent.depth + 1
            queue.extend(parent.children)


    @classmethod
    def collect_parents(cls):
        for program in cls.programs.values():
            for child in program.children:
                child.parent = program

    @property
    def children(self):
        return {Program.programs[p] for p in self._children}

    def __str__(self):
        return self.name


def main():

    with open(file=INPUTFILE, mode='r') as fileinput:
        reader = csv.reader(fileinput, delimiter=" ")

        for row in reader:
            Program(row)

        Program.collect_parents()
        Program.collect_depths()
        Program.collect_weights()

        root = Program.get_root()
        children = root.children

        diff = None
        while True:
            weights = Counter(p.total_weight for p in children).most_common()
            if len(weights) == 1:
                break

            # https://wiki.python.org/moin/UsingAssertionsEffectively
            assert len(weights) == 2
            assert weights[1][1] == 1

            if diff is None:
                diff = weights[1][0] - weights[0][0]

            wanted_weight = weights[1][0]
            parent = [p for p in children if p.total_weight == wanted_weight][0]
            children = parent.children

        print("{}: {}".format(parent, (parent.weight - diff)))


if __name__ == '__main__':
    if len(sys.argv) == 2:
        INPUTFILE = sys.argv[1]
    main()
