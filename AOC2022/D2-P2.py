#!/usr/bin/env python3
from helper import read_file, remove_escpape_char

rock, paper, scissor, loss, draw, win, points = ('A',1), ('B',2), ('C',3), 0, 3, 6, 0

def get_total_points(match: str, result, point: int=0):
    if result == 0:
        if match[0] == 'A' : point = scissor[1]
        if match[0] == 'B' : point = rock[1]
        if match[0] == 'C' : point = paper[1]
    if result == 3:
        if match[0] == 'A' : point = rock[1]
        if match[0] == 'B' : point = paper[1]
        if match[0] == 'C' : point = scissor[1]
    if result == 6:
        if match[0] == 'A' : point = paper[1]
        if match[0] == 'B' : point = scissor[1]
        if match[0] == 'C' : point = rock[1]
    return point + result

if __name__ == "__main__":
    strat = remove_escpape_char((read_file("misc/strat")))
    for match in strat:
        if match[2] == 'X':
            points +=  get_total_points(match, loss)
        if match[2] == 'Y':
            points +=  get_total_points(match, draw)
        if match[2] == 'Z':
            points +=  get_total_points(match, win)
    print(points)