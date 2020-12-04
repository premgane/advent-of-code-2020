#!/usr/bin/python

import re
from typing import Callable


def parse(line: str) -> tuple:
    pieces = line.strip().split(':')
    return (pieces[0].strip(), pieces[1].strip())


def read() -> list:
    lines = []
    with open('input.txt') as f:
        lines = [parse(i) for i in f.readlines()]
    return lines


def count_regex(chr: str, pwd: str, min: int, max: int) -> bool:
    print(min, max, chr)
    regex = str(chr) + '{' + str(min) + ',' + str(max) + '}'
    print (regex, pwd)
    m = re.findall(regex, pwd)
    if len(m) > 0:
        print('valid!')
        return True

    print('invalid')
    return False


def count_str(chr: str, pwd: str, min: int, max: int) -> bool:
    count = pwd.count(chr)
    if count >= min and count <= max:
        return True
    return False


def xor_rule(chr: str, pwd: str, min: int, max: int) -> bool:
    return (((pwd[min - 1] == chr) or (pwd[max - 1] == chr)) and
                ((pwd[min - 1] != chr) or (pwd[max - 1] != chr)))

def part1(acceptor: Callable) -> int:
    lines = read()
    result = 0

    for line in lines:
        rule = line[0]
        pwd = line[1]

        m = re.search(r'(\d+)-(\d+) (\w)', rule)
        min = int(m.group(1))
        max = int(m.group(2))
        chr = m.group(3)

        print(line)
        if acceptor(chr, pwd, min, max):
            print('valid')
            result += 1

    return result



if __name__ == '__main__':
    print(part1(count_str))
    print('----')
    print(part1(xor_rule))