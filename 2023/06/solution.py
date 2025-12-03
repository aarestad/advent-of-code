## advent of code 2023
## https://adventofcode.com/2023
## day 06

from dataclasses import dataclass
from functools import reduce
from operator import mul
from math import sqrt


@dataclass
class Race:
    time: int
    distance: int

    def num_ways_to_win(self) -> int:
        return (
            self.time
            - 2 * int((-self.time + sqrt(self.time**2 - 4 * self.distance)) / -2)
            - 1
        )


def parse_input(lines):
    times = [int(t) for t in lines[0].split()[1:]]
    distances = [int(d) for d in lines[1].split()[1:]]

    part_2_time = int("".join(lines[0].split()[1:]))
    part_2_distance = int("".join(lines[1].split()[1:]))

    races = [Race(t, d) for t, d in zip(times, distances)]
    races.append(Race(part_2_time, part_2_distance))
    return races


def part1(races):
    return reduce(mul, (r.num_ways_to_win() for r in races[:-1]))


def part2(races):
    return races[-1].num_ways_to_win()
