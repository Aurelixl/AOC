#!/usr/bin/env python3
from helper import read_file, remove_escpape_char

prio, alph = 0, "abcdefghijklmnopqrstuvwxyz"
if __name__ == "__main__":
    rucksack = remove_escpape_char((read_file("msic/rucksack")))
    for item in rucksack:
        item1 = item[0:len(item)//2]
        item2 = item[len(item)//2:]
        for char in item1:
            if char in item2:
                if char.isupper():
                    char = char.lower()
                    for i in range(len(alph)):
                        if alph[i]==char:
                            prio += i + 1 + 26
                else:
                    for i in range(len(alph)):
                        if alph[i]==char:
                            prio += i + 1
                break
    print(prio)