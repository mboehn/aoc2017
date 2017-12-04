#!/usr/bin/env python3

import math
import csv
import itertools
from pprint import pprint

import func


INPUTFILE = './task04.input'


def is_anagram(word, word2):
#    return sorted(word.lower()) == sorted(word2.lower()) # vi har bare lowercase, sikker kjappere uten lower()
    return sorted(word) == sorted(word2)


def main():
    accept = 0
    with open(INPUTFILE, mode='r') as csvfile:
        reader = csv.reader(csvfile, delimiter=" ")
        lines = list(reader)
        for line in lines:
#            print("----")
            reject_line = False
#            print("line debug 1: {}".format(line))
            for word in list(line):
#                print(word)
                line.remove(word)
                for word2 in line:
                    if word == word2:
                        print("{}{} is a duplicate of {}...{}".format(func.bcolors.OKBLUE, word, word2, func.bcolors.ENDC))
                        reject_line = True
                    elif is_anagram(word, word2):
                        print("{}{} is an anagram of {}, perhaps...{}".format(func.bcolors.FAIL, word, word2, func.bcolors.ENDC))
                        reject_line = True
#            print("line debug 2: {}".format(line))
#            print()




            if not reject_line:
                accept = accept + 1

        lines_count = len(lines)
        print("{}file {} contains {} lines{}".format(func.bcolors.HEADER, INPUTFILE, lines_count, func.bcolors.ENDC))
        print("{}we accept {} of them{}".format(func.bcolors.BOLD, accept, func.bcolors.ENDC))



if __name__ == '__main__':
    main()
