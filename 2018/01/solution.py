## advent of code 2018
## https://adventofcode.com/2018
## day 01


def parse_input(lines):
    return [int(l) for l in lines]


def part1(data):
    return sum(data)


def part2(data):
    current_freq = 0
    seen_frequencies = {0}

    while True:
        for delta in data:
            current_freq += delta
            if current_freq in seen_frequencies:
                return current_freq
            seen_frequencies.add(current_freq)
