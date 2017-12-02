#!/usr/bin/env python3

import csv

import func


# Input from A.
INPUTFILE = './task02-a.input'


def checkrow(row):
    first = 0
    second = 0
    result = 0
    for index, cell in enumerate(row):
#        print("DEBUG: i:{} c:{}".format(index, cell))
        for insideindex, insidecell in enumerate(row):
            if index == insideindex:
                continue
            if not cell % insidecell:
                first = cell
                second = insidecell 
                result = int(first / second)
                print("{} (i:{}) is divisible by {} (i:{}), the result is: {}".format(cell, index, insidecell, insideindex, result))
                break

    return (first, second, result)


def main():
    with open(INPUTFILE, mode='r') as csvfile:
        reader = csv.reader(csvfile, delimiter="\t")

        sum = 0
        for row in reader:
            row = list(map(int, row))
#            print(row)
            first, second, result = checkrow(row)
            sum = sum + result
#            print("{} / {} = {}".format(first, second, result))

        print("{}the sum is: {}{}".format(func.bcolors.BOLD, sum, func.bcolors.ENDC))


if __name__ == '__main__':
    main()
