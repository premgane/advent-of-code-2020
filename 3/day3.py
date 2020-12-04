#!/usr/bin/python

def read() -> list:
    lines = []
    with open('input.txt') as f:
        lines = [i for i in f.readlines()]
    return lines

def part1(right: int, down: int) -> int:
    result = 0
    lines = read()

    width = len(lines[0])
    print(width)
    pos = 0
    for i in range(0, len(lines), down):
        if i < len(lines):
            line = lines[i]
            print(pos, width)
            print(line[pos])
            if line[pos] == '#':
                result += 1
            pos = (pos + right) % (width-1)
    return result

if __name__ == '__main__':
    print(part1(3, 1))
    print('----')
    one = (part1(1, 1))
    three = (part1(3, 1))
    five = (part1(5, 1))
    seven = (part1(7, 1))
    one_two = (part1(1, 2))

    print(one * three * five * seven * one_two)