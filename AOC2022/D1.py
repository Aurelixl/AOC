#!/usr/bin/env python3

def get_calories_per_elve():
    calories_per_elve = []
    all_calories = []
    elve = 0

    f = open("elves","r")
    lines = f.readlines() + ["\n"]
    for line in lines:
        if line != '\n':
            calories_per_elve.append(int(line.replace("\n", "")))
        else: 
            elve += 1
            cal = 0
            for i in calories_per_elve:
                cal = cal + i
            all_calories.append((elve,cal))
            calories_per_elve = []
        
    return all_calories

if __name__ == '__main__':
    max = (0,0)
    for elve in get_calories_per_elve():
            if elve[1] > max[1]:
                max = elve
    print(max)
