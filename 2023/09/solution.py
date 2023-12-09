## advent of code 2023
## https://adventofcode.com/2023
## day 09


def parse_input(lines):
    return [[int(n) for n in l.split()] for l in lines]


def extrapolate_next(data) -> int:
    if all(d == 0 for d in data):
        return 0

    return data[-1] + extrapolate_next([n2 - n1 for n1, n2 in zip(data, data[1:])])


def extrapolate_previous(data) -> int:
    if all(d == 0 for d in data):
        return 0

    return data[0] - extrapolate_previous([n2 - n1 for n1, n2 in zip(data, data[1:])])


def part1(data):
    return sum(extrapolate_next(d) for d in data)


def part2(data):
    return sum(extrapolate_previous(d) for d in data)
