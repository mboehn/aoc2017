#!/usr/bin/env python3

import math
import sys
import csv
from pprint import pprint
import collections
import operator

import func


INPUTFILE = './task12.input'


class Program():

    programs = {}

    def __init__(self, row):
        self.pid = int(row[0])
        self._children = row[2:]
        self.children = []

        self.programs[self.pid] = self

    def __repr__(self):
#        return "pid={} children={}".format(self.pid, self.children)
        return str(self.pid)


    @classmethod
    def fix_children(cls):
        for program in cls.programs.values():
            for child in program._children:
                program.children.append(cls.programs[int(child.strip(','))])





    @classmethod
    def fix_pipes(cls):
        pipes = {}
        for program in cls.programs.values():
            pipes[program.pid] = []
            pipes[program.pid].append(program.pid)

            for child in program.children:
                pipes[program.pid].append(child.pid)

        return pipes


def main():
    with open(file=INPUTFILE, mode='r') as fileinput:
        reader = list(csv.reader(fileinput, delimiter=' '))
        for row in reader:
            Program(row)
        Program.fix_children()
        pipes = Program.fix_pipes()

        print(Program.programs[0].find_group())


if __name__ == '__main__':
    if len(sys.argv) == 2:
        INPUTFILE = sys.argv[1]
    main()
