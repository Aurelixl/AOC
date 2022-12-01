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
    max3= 0
    all_elves = get_calories_per_elve()
    for i in range(3):
        max = (0,0)
        for elve in all_elves:
                if elve[1] > max[1]:
                    max = elve
        all_elves.remove(max)
        max3 = max[1] + max3
    print(max3)
