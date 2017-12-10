#!/usr/bin/env python3

import sys
import csv
from pprint import pprint
import collections
import operator

import func


INPUTFILE = './task08.input'


class Instruction():
    instructions = []

    def __init__(self, row):
        self.register_to_modify = row[0]
        self.action = row[1]
        self.action_value = int(row[2])
        # row[3] == if
        self.condition_register = row[4]
        self.condition_type = row[5]
        self.condition_value = int(row[6])

        self.instructions.append(self)

    def __repr__(self):
        return("{} {} {} if {} {} {}".format(
            self.register_to_modify,
            self.action,
            self.action_value,
            self.condition_register,
            self.condition_type,
            self.condition_value
        ))

    @classmethod
    def solve(cls, registers):

        operators = {
            '>': (lambda x, y: x > y),
            '<': (lambda x, y: x < y),
            '<=': (lambda x, y: x <= y),
            '>=': (lambda x, y: x >= y),
            '==': (lambda x, y: x == y),
            '!=': (lambda x, y: x != y),
            'inc': (lambda x, y: x + y),
            'dec': (lambda x, y: x - y)
        }

        for instruction in cls.instructions:
            condition_check_value = registers[instruction.condition_register]

            if operators[instruction.condition_type](condition_check_value, instruction.condition_value):
                registers[instruction.register_to_modify] = operators[instruction.action](registers[instruction.register_to_modify], instruction.action_value)


        sort_registers = sorted(registers.items(), key=operator.itemgetter(1))
        pprint(sort_registers)
        max_register = sort_registers[-1][0]
        max_value = sort_registers[-1][1]
        print("register {}: {}".format(max_register, max_value))



def main():

    with open(file=INPUTFILE, mode='r') as fileinput:
        reader = csv.reader(fileinput, delimiter=" ")

        for row in reader:
            Instruction(row)

    # default i dicten er 0 (int)
    registers = collections.defaultdict(int)

    Instruction.solve(registers)
    #pprint(Instruction.instructions)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        INPUTFILE = sys.argv[1]
    main()
