#!/usr/bin/env python3
from helper import read_file, remove_escpape_char

if __name__ == "__main__":
    moves = remove_escpape_char((read_file("misc/crates")))
    stacks = [['Q','M','G','C','L'],['R','D','L','C','T','F','H','G'],['V','J','F','N','M','T','W','R'],['J','F','D','V','Q','P'],['N','F','M','S','L','B','T'],
    ['R','N','V','H','C','D','P'],['H','C','T'],['G','S','J','V','Z','N','H','P'],['Z','F','H','G']]
    for move in moves:
        move = move.replace('move ','').replace(' from', '').replace('to ', '').split(' ')
        anzahl = int(move[0])
        von = int(move[1])-1
        nach = int(move[2])-1
        vonliste = stacks[von][-anzahl:]
        stacks[nach].extend(vonliste)
        for i in range(int(move[0])):
            stacks[int(move[1])-1].pop()
    ret = ''
    for stack in stacks:
        ret = ret + str(stack[-1:])
    print(ret)