#!/usr/bin/env python3

import csv

import func


INPUTFILE = './task02-a.input'
checksum = 0

with open(INPUTFILE, mode='r') as csvfile:
    reader = csv.reader(csvfile, delimiter="\t")

    for row in reader:
        row = list(map(int, row))
        print(row)
        rowdiff = int(max(row)) - int(min(row))
        print("{}current checksum: {}\t|max: {}\t| min: {}\t| diff: {}\t| new checksum: {}{}".format(func.bcolors.BOLD, checksum, max(row), min(row), rowdiff, checksum + rowdiff, func.bcolors.ENDC))
        checksum = checksum + rowdiff

print("checksum is: {}".format(checksum))
