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


def part1() -> list:
    data = read()
    result = []
    for datum in data:
        keys = datum.keys()
        if len(datum) < 8:
            if len(datum) == 7 and 'cid' not in set(keys):
                result.append(datum)
        else:
            result.append(datum)
    return result


def part2() -> int:
    data = part1()
    result = 0

    for datum in data:
        valid = True
        for key in datum.keys():
            val = datum[key].strip()
            if key == 'byr' and not (len(val) == 4
                                     and int(val) >= 1920
                                     and int(val) <= 2002):
                # print(key, val)
                valid = False
                break
            elif key == 'iyr' and not (len(val) == 4
                                       and int(val) >= 2010
                                       and int(val) <= 2020):
                # print(key, val)
                valid = False
                break
            elif key == 'eyr' and not (len(val) == 4
                                       and int(val) >= 2020
                                       and int(val) <= 2030):
                # print(key, val)
                valid = False
                break
            elif key == 'hgt':
                if re.search(pattern=r'^\d+(cm|in)$', string=val) is None:
                    # print(key, val)
                    valid = False
                    break
                height = int(val[:-2])
                if val[-2:] == 'cm' and not (height >= 150
                                             and height <= 193):
                    # print(key, val)
                    valid = False
                    break
                elif val[-2:] == 'in' and not (height >= 59 and height <= 76):
                    # print(key, val)
                    valid = False
                    break
            elif key == 'hcl' and not (re.search(pattern=r'^#[a-f0-9]{6}$', string=val) is not None):
                # print(key, val)
                valid = False
                break
            elif key == 'ecl':
                if not (val in set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])):
                    # print(key, val)
                    valid = False
                    break
            elif key == 'pid' and not (re.search(pattern=r'^\d{9}$', string=val) is not None):
                # print(key, val)
                valid = False
                break

            if not valid:
                break

        if valid:
            print(datum)
            result += 1
    print('---')
    return result


if __name__ == '__main__':
    # print(read())
    print(part2())