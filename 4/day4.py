#!/usr/bin/python

import re

def parse(line: str) -> dict:
    result = dict()
    line = re.sub(pattern=r'\s+', repl=' ', string=line)
    for piece in line.split(' '):
        pair = piece.split(':')
        result[pair[0]] = pair[1]
    return result

def read() -> list:
    lines = []
    result = []
    with open('input.txt') as f:
        lines = [i for i in f.read().split('\n\n')]
    for i in range(len(lines)):
        result.append(parse(lines[i].strip()))
    return result

def part1() -> int:



if __name__ == '__main__':
    # print(read())
    print(read())