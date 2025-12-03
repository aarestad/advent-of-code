## advent of code 2023
## https://adventofcode.com/2023
## day 13

from enum import StrEnum
from dataclasses import dataclass
from typing import List


class LavaTile(StrEnum):
    ASH = "."
    ROCK = "#"


@dataclass
class Pattern:
    tiles: List[List[LavaTile]]


def parse_input(lines):
    pass


def part1(data):
    pass


def part2(data):
    pass
