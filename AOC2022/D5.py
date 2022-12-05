#!/usr/bin/env python3
from helper import read_file, remove_escpape_char

if __name__ == "__main__":
    moves = remove_escpape_char((read_file("misc/crates")))
    stacks = [['Z', 'N'],['M', 'C', 'D'],['P']]
    for move in moves:
        move = move.replace('move ','').replace(' from', '').replace('to ', '').split(' ')
        for i in range(int(move[0])):
            stacks[int(move[2])-1].append(stacks[int(move[1])-1][-1:][0])
            stacks[int(move[1])-1].pop()
    ret = ''
    for stack in stacks:
        ret = ret + str(stack[-1:])
    print(ret)
