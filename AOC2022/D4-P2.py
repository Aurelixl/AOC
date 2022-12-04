#!/usr/bin/env python3
from helper import read_file, remove_escpape_char

def range_to_list(sections: int):
    ret_list = []
    sections = sections.split('-')
    for i in range(int(sections[0]), int(sections[1]) + 1):
        ret_list.append(i)
    return ret_list

if __name__ == "__main__":
    sections = remove_escpape_char((read_file("msic/sections")))
    count = 0
    for sections in sections:
        sections = sections.split(',')
        section_range1, section_range2 = range_to_list(sections[0]), range_to_list(sections[1])
        dup = set(section_range1) & set(section_range2)
        if len(dup) > 0:
            count += 1
    print(count)