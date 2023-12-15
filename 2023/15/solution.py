## advent of code 2023
## https://adventofcode.com/2023
## day 15


def parse_input(lines):
    return lines[0].split(",")


def hash_string(s) -> int:
    hash = 0

    for c in s:
        hash += ord(c)
        hash *= 17
        hash %= 256

    return hash


def part1(init_steps):
    return sum(hash_string(s) for s in init_steps)


def part2(data):
    pass
