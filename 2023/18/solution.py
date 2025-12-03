## advent of code 2023
## https://adventofcode.com/2023
## day 18

from dataclasses import dataclass
from enum import StrEnum


@dataclass
class LagoonTile:
    dug: bool
    color: (int, int, int)


class Direction(StrEnum):
    RIGHT = "R"
    DOWN = "D"
    LEFT = "L"
    UP = "U"


def parse_input(lines):
    data_list = map(lambda line: line.split(), lines)
    return list(
        map(lambda data: (Direction(data[0]), int(data[1]), data[2]), data_list)
    )


def part1(directions):
    current_loc = (0, 0)
    rows = 1
    cols = 1

    for dir, distance, color in directions:
        match dir:
            case Direction.RIGHT:
                current_loc[]


def part2(data):
    pass
