#!/usr/bin/env python3

def read_file(file: str):
    return open(file,"r").readlines()

def remove_escpape_char(list: list):
    for i in range(len(list)):
        list[i] = list[i].replace("\n", '')
    return list
    