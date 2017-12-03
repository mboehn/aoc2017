#!/usr/bin/env python3

import math
import csv

import func


INPUT = (58, 99, 265149) # skal være 265149, 99 er kun for å kontrollregne enklere
#INPUT = 265149
SQ_PER_LEVEL = 8
DIM_PER_LEVEL = 2
NS_START = 1
WE_START = 3


def calc_levels(goal):
#    level = 0
#    squares = 0
#
#    while (squares <= goal):
#            
#        if level == 0:
#            new_squares = 1
#        else:
#            new_squares = level * SQ_PER_LEVEL
#        last_level_squares = squares
#        squares = squares + new_squares
#        
#        print("level {}: {} squares (added: {}, last level had: {})".format(level, squares, new_squares, last_level_squares))
#        level = level + 1

    # snarvei til å finne antall levels...
    levels = round(math.sqrt(goal) / 2)
    inside_level_squares = math.floor(math.sqrt(goal)) ** 2
    level_squares = inside_level_squares + (levels * SQ_PER_LEVEL)
    return levels, inside_level_squares, level_squares


def get_dim(level):
    level = level - 1 # første levelet er et unntak fra regelen (bare 1 square)
    ns = NS_START + (DIM_PER_LEVEL * level)
    we = WE_START + (DIM_PER_LEVEL * level)
    return ns, we


def get_startend(level):
    # x, y
    start = (level, -(level - 1))
    end = (level, -level)
    return start, end


def new_where(where, square):
    print("at {} (sq {})".format(where, square))
    return where, square


def walk_level(goal, ns, we, start, end, startsquare, endsquare):
    where, square = new_where(start, startsquare)

    for dir in ('up', 'left', 'down', 'right'):

        if square == goal:
            break

        # ikke helt sikker på logikken i +/- på we, men det blir visst riktig med 99-eksemplet mitt
        # på ns er det +1 på vei ned fordi jeg begynner en over nederste høyre hjørnet
        if dir == 'up':
            dirlen = ns
        elif dir == 'down':
            dirlen = ns + 1
        elif dir == 'left':
            dirlen = we - 1
        elif dir == 'right':
            dirlen = we - 1
        else:
            raise NotImplementedError

        if square + dirlen <= goal:
            go = dirlen
        else:
            go = goal - square
        print("walking {} {}".format(go, dir))

        if dir == 'up':
            to0 = where[0]
            to1 = where[1] + go
        elif dir == 'down':
            to0 = where[0]
            to1 = where[1] - go
        elif dir == 'left':
            to0 = where[0] - go
            to1 = where[1]
        elif dir == 'right':
            to0 = where[0] + go
            to1 = where[1]
        else:
            raise NotImplementedError
        where, square = new_where((to0, to1), square + go)

    return where


def calc_distance(where):
    return abs(where[0]) + abs(where[1])



def main(goal):
    print("working with square {}".format(goal))

    levels, inside_level_squares, level_squares = calc_levels(goal)
    print("number of levels: {}".format(levels))
    print("current level gives {} squares, level inside was {} squares".format(level_squares, inside_level_squares))
    print("current level contains {} squares".format(levels * SQ_PER_LEVEL))

    ns, we = get_dim(levels)
    print("level {} levels has {} squares NS and {} squares WE".format(levels, ns, we))

    startsquare = inside_level_squares + 1
    endsquare = level_squares
    start, end = get_startend(levels)
    print("level {} starts at {} (sq {}) and ends at {} (sq {})".format(levels, start, startsquare, end, endsquare))

    print()
    print("starting the walk...")
    where = walk_level(goal, ns, we, start, end, startsquare, endsquare)
    print("arrived at goal {} square {}".format(where, goal))
    print()
    distance = calc_distance(where)
    print("{}the distance is {} steps{}".format(func.bcolors.BOLD, distance, func.bcolors.ENDC))



if __name__ == '__main__':
    for i in INPUT:
        print("{}---------------{}".format(func.bcolors.HEADER, func.bcolors.ENDC))
        main(i)
        print()
