## advent of code 2023
## https://adventofcode.com/2023
## day 14

from enum import StrEnum


class PlatformTile(StrEnum):
    ROCK = "O"
    CUBE = "#"
    EMPTY = "."


def parse_input(lines):
    platform_lines: [[PlatformTile]] = []

    for line in lines:
        if not line:
            continue

        platform_lines.append([PlatformTile(c) for c in line])

    return platform_lines


def part1(platform_lines):
    for row, line in enumerate(platform_lines):
        for col, tile in enumerate(line):
            if tile != PlatformTile.ROCK:
                continue

            line[col] = PlatformTile.EMPTY

            for row_above in reversed(range(row)):
                if platform_lines[row_above][col] in (
                    PlatformTile.ROCK,
                    PlatformTile.CUBE,
                ):
                    # may just be replacing the rock in its current place
                    platform_lines[row_above + 1][col] = PlatformTile.ROCK
                    break
            else:  # it rolled to the top
                platform_lines[0][col] = PlatformTile.ROCK

    return sum(
        len(platform_lines) - row
        for row, line in enumerate(platform_lines)
        for tile in line
        if tile == PlatformTile.ROCK
    )


def part2(data):
    pass
