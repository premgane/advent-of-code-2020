#!/usr/bin/python

def read() -> list:
    lines = []
    with open('input.txt') as f:
        lines = [int(i.strip()) for i in f.readlines()]
    return lines

def part1(target: int, lines: list, avoid_idx: int) -> int:
    # O(N^2), but it's a short enough list that I'm ok with it
    result = -1
    for i in range(len(lines)):
        for j in range(i+1, len(lines)):
            if i == avoid_idx or j == avoid_idx:
                continue
            if lines[i] + lines[j] == target:
                print(str(lines[i]) + ' + ' + str(lines[j]) + ' == ' + str(target))
                result = lines[i] * lines[j]
                print('part1: ' + str(result))
    return result

def part2(target: int, lines: list) -> int:
    for i in range(len(lines)):
        reduced_target = target - lines[i]
        result = part1(reduced_target, lines, i)
        if result != -1:
            print(str(lines[i]) + ' + ' + str(result) + ' == ' + str(target))
            result *= lines[i]
            print('part 2: ' + str(result))
    return result

if __name__ == '__main__':
    part1(2020, read(), -1)
    print('----')
    part2(2020, read())