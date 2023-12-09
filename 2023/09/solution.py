## advent of code 2023
## https://adventofcode.com/2023
## day 09


def parse_input(lines):
    return [[int(n) for n in l.split()] for l in lines]


def extrapolate(data) -> int:
    if all(d == 0 for d in data):
        extrapolated = 0
    else:
        extrapolated = data[-1] + extrapolate(
            [n2 - n1 for n1, n2 in zip(data, data[1:])]
        )

    return extrapolated


def part1(data):
    return sum(extrapolate(d) for d in data)


def part2(data):
    pass
