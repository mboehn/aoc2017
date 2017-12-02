#!/usr/bin/env python3

import csv


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

INPUTFILE = './task02-a.input'
checksum = 0

with open(INPUTFILE, mode='r') as csvfile:
    reader = csv.reader(csvfile, delimiter="\t")

    for row in reader:
        row = list(map(int, row))
        print(row)
        rowdiff = int(max(row)) - int(min(row))
        print("{}current checksum: {}\t|max: {}\t| min: {}\t| diff: {}\t| new checksum: {}{}".format(bcolors.BOLD, checksum, max(row), min(row), rowdiff, checksum + rowdiff, bcolors.ENDC))
        checksum = checksum + rowdiff

print("checksum is: {}".format(checksum))
