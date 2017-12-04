#!/usr/bin/env python3

import math
import csv

import func


INPUT = (58, 99, 158, 265149) # skal være 265149, de andre er kun for å kontrollregne enklere



def get_last_square(goal):
    odd = math.ceil(math.sqrt(goal))
    if not odd % 2:
        odd = odd + 1
    return odd ** 2


def get_level(last_square):
    return int((math.sqrt(last_square -1) / 2))


def get_sidelen(last_square):
    # antall steps for å gå hele sida er - 1, da du jo starter på en square
    # bruker egentlig ikke disse tallene, men det var nyttig for å skjønne litt mer...
    return int(math.sqrt(last_square))


def get_axises(last_square, level):
    return list(reversed((
        last_square - level,
        last_square - (level * 3),
        last_square - (level * 5),
        last_square - (level * 7)
    )))


def get_steps_to_axis(goal, axises):
    steps = []
    for axis in axises:
        steps.append(abs(goal - axis))
    
    return min(steps)


def main(goal):

    print("current goal is: {}".format(goal))

    last_square = get_last_square(goal)
    print("last square is: {}".format(last_square))

    level = get_level(last_square)
    print("last level is: {}".format(level))

    sidelen = get_sidelen(last_square)
    print("side length is: {}".format(sidelen))

    axises = get_axises(last_square, level)
    print("the axises are {}".format(axises))

    steps_to_axis = get_steps_to_axis(goal, axises)
    print("there are {} steps from {} to nearest axis".format(steps_to_axis, goal))

    steps_total = steps_to_axis + level
    print("{}there are {} steps from {} to center (sq 1){}".format(func.bcolors.BOLD, steps_total, goal, func.bcolors.ENDC))

if __name__ == '__main__':
    for i in INPUT:
        print("{}---------------{}".format(func.bcolors.HEADER, func.bcolors.ENDC))
        main(i)
        print()
