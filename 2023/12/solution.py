## advent of code 2023
## https://adventofcode.com/2023
## day 12

from enum import StrEnum
from dataclasses import dataclass


class Spring(StrEnum):
    UNKNOWN = "?"
    DAMAGED = "#"
    OK = "."


@dataclass
class SpringSet:
    springs: [Spring]
    damaged_spring_groups: [int]


def parse_input(lines):
    spring_sets = []

    for l in lines:
        if not lines:
            continue

        springs, groups = l.split()

        spring_sets.append(
            SpringSet([Spring(c) for c in springs], [int(c) for c in groups.split(",")])
        )

    return spring_sets


def part1(spring_sets):
    sum_arrangements = 0

    for ss in spring_sets:
        sum_groups = sum(ss.damaged_spring_groups)
        sum_unknown = sum(1 for s in ss.springs if s == Spring.UNKNOWN)

        if sum_groups == sum_unknown:
            sum_arrangements += 1


def part2(spring_sets):
    pass
