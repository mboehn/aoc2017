#!/usr/bin/env python3

import sys
import math
import csv
import itertools
from pprint import pprint

import func


INPUTFILE = './task05.input'


def main():
    with open(file=INPUTFILE, mode='r') as fileinput:

        
        lines = list(map(int, fileinput.readlines()))
        instructions = lines

        steps = 0
        next_instruction = 0

        while True:
            log = {}
            log['step'] = steps
            log['index'] = next_instruction
            try:
                current_instruction = int(instructions[next_instruction])
                log['current'] = current_instruction
            except IndexError as error:
                print("{}exited maze somehow... took {} steps{}\t\t(original exception: {})".format(func.bcolors.BOLD, steps, func.bcolors.ENDC, error))
                break

            instructions[next_instruction] += 1
            log['new_value'] = instructions[next_instruction]

            if current_instruction == 0:
                log['parse'] = 'zero'
                pass
            elif current_instruction < 0:
                log['parse'] = 'below'
                next_instruction = next_instruction - abs(current_instruction)
            else:
                log['parse'] = 'above'
                next_instruction = next_instruction + current_instruction

            

#            if steps > 100:
#                break  
            steps += 1

            print(
                "step: {} \t| index: {}\t | curr: {}\t({})\t| new: {}".format(
                    log['step'],
                    log['index'],
                    log['current'],
                    log['parse'],
                    log['new_value']
                )
            )


if __name__ == '__main__':
    if len(sys.argv) == 2:
        INPUTFILE = sys.argv[1]
    main()
