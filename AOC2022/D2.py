#!/usr/bin/env python3
from helper import read_file, remove_escpape_char

rock, paper, scissor, loss, draw, win, points = ('A','X',1), ('B','Y',2), ('C','Z',3), 0, 3, 6, 0

def get_total_points(match: str, result, point: int=0):
    if match[2] == 'X' : point = rock[2]
    if match[2] == 'Y' : point = paper[2]
    if match[2] == 'Z' : point = scissor[2]
    return point + result

if __name__ == "__main__":
    strat = remove_escpape_char((read_file("msic/strat")))
    for match in strat:
        # all wins
        if match[0] == 'C' and match[2] == 'X' or match[0] == 'B' and match[2] == 'Z' or match[0] == 'A' and match[2] == 'Y':
            points +=  get_total_points(match, win)
        # all losses
        if match[0] == 'A' and match[2] == 'Z' or match[0] == 'B' and match[2] == 'X' or match[0] == 'C' and match[2] == 'Y':
            points +=  get_total_points(match, loss)
        # all draws
        if match[0] == 'A' and match[2] == 'X' or match[0] == 'B' and match[2] == 'Y' or match[0] == 'C' and match[2] == 'Z':
            points +=  get_total_points(match, draw)
    print(points)
 