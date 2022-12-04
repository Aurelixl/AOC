#!/usr/bin/env python3
from helper import read_file, remove_escpape_char

prio, alph = 0, "abcdefghijklmnopqrstuvwxyz"

def total_prio(prio: int, char: str):
    if char.isupper():
        charL = char.lower()
        for i in range(len(alph)):
            if alph[i]==charL:
                prio += i + 1 + 26
    else:
        for i in range(len(alph)):
            if alph[i]==char:
                prio += i + 1
    return prio

def find_batch(rucksack):
    for char in rucksack[0]:
        print('str 1',rucksack[0])
        print('current char:', char)
        if char in rucksack[1]:
            for char1 in rucksack[1]:
                if char in rucksack[2] and char1 == char:
                    print(char)
                    return char

if __name__ == "__main__":
    rucksack = remove_escpape_char((read_file("misc/rucksack")))
    while '' in rucksack:
        rucksack.remove("")
    prio = 0
    while rucksack != []:
        prio = total_prio(prio, find_batch(rucksack))
        for i in range(3):
            rucksack.pop(0)

    print(prio)
    