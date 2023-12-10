## advent of code 2023
## https://adventofcode.com/2023
## day 10

from enum import StrEnum, auto, nonmember


class Pipe(StrEnum):
    GROUND = auto()
    START = auto()
    VERTICAL = auto()
    HORIZONTAL = auto()
    L_BEND = auto()
    J_BEND = auto()
    SEVEN_BEND = auto()
    F_BEND = auto()

    PIPES_BY_CHAR: dict[str, "Pipe"] = nonmember(
        {
            ".": GROUND,
            "S": START,
            "|": VERTICAL,
            "-": HORIZONTAL,
            "L": L_BEND,
            "J": J_BEND,
            "7": SEVEN_BEND,
            "F": F_BEND,
        }
    )


def parse_input(lines) -> [[Pipe]]:
    pipe_map = []

    for l in lines:
        if not l:
            continue

        map_row = []

        for c in l:
            map_row.append(Pipe.PIPES_BY_CHAR[c])

        pipe_map.append(map_row)

    return pipe_map


def part1(pipe_map):
    for l in pipe_map:
        for p in l:
            print(
                str(p),
            )
        print()


def part2(data):
    pass
