## advent of code 2023
## https://adventofcode.com/2023
## day 10

from enum import Enum, auto, nonmember


class Direction(Enum):
    NORTH = auto()
    EAST = auto()
    SOUTH = auto()
    WEST = auto()


class Pipe(Enum):
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

    @classmethod
    def for_char(cls, c) -> "Pipe":
        match c:
            case ".":
                return Pipe.GROUND
            case "S":
                return Pipe.START
            case "|":
                return Pipe.VERTICAL
            case "-":
                return Pipe.HORIZONTAL
            case "L":
                return Pipe.L_BEND
            case "J":
                return Pipe.J_BEND
            case "7":
                return Pipe.SEVEN_BEND
            case "F":
                return Pipe.F_BEND
            case _:
                raise ValueError(f"bad char: {c}")

    def next_direction(self, heading=Direction) -> Direction:
        ve = ValueError(f"can't be coming from {heading} into {self}")

        match heading:
            case heading.SOUTH:
                match self:
                    case Pipe.VERTICAL:
                        return Direction.SOUTH
                    case Pipe.L_BEND:
                        return Direction.EAST
                    case Pipe.J_BEND:
                        return Direction.WEST
                    case _:
                        raise ve

            case Direction.NORTH:
                match self:
                    case Pipe.VERTICAL:
                        return Direction.NORTH
                    case Pipe.SEVEN_BEND:
                        return Direction.WEST
                    case Pipe.F_BEND:
                        return Direction.EAST
                    case _:
                        raise ve

            case Direction.WEST:
                match self:
                    case Pipe.HORIZONTAL:
                        return Direction.WEST
                    case Pipe.F_BEND:
                        return Direction.SOUTH
                    case Pipe.L_BEND:
                        return Direction.NORTH
                    case _:
                        raise ve

            case Direction.EAST:
                match self:
                    case Pipe.HORIZONTAL:
                        return Direction.EAST
                    case Pipe.J_BEND:
                        return Direction.NORTH
                    case Pipe.SEVEN_BEND:
                        return Direction.SOUTH
                    case _:
                        raise ve

        raise ValueError(f"bad heading: {heading}")


def start_type(pipe_map, start_row, start_col):
    pipe_above = pipe_map[start_row - 1][start_col] if start_row > 0 else Pipe.GROUND

    pipe_below = (
        pipe_map[start_row + 1][start_col]
        if start_row < len(pipe_map) - 1
        else Pipe.GROUND
    )

    pipe_left = pipe_map[start_row][start_col - 1] if start_col > 0 else Pipe.GROUND

    pipe_right = (
        pipe_map[start_row][start_col + 1]
        if start_col < len(pipe_map[0]) - 1
        else Pipe.GROUND
    )

    up = pipe_above in [Pipe.VERTICAL, Pipe.SEVEN_BEND, Pipe.F_BEND]
    down = pipe_below in [Pipe.VERTICAL, Pipe.L_BEND, Pipe.J_BEND]
    lt = pipe_left in [Pipe.HORIZONTAL, Pipe.L_BEND, Pipe.F_BEND]
    rt = pipe_right in [Pipe.HORIZONTAL, Pipe.J_BEND, Pipe.SEVEN_BEND]

    if sum(1 for c in [up, down, lt, rt] if c) != 2:
        raise ValueError("wrong number of connecting pipes!")

    if up:
        if down:
            return Pipe.VERTICAL
        if lt:
            return Pipe.J_BEND
        return Pipe.L_BEND

    if down:
        if lt:
            return Pipe.SEVEN_BEND
        return Pipe.F_BEND

    return Pipe.HORIZONTAL


def parse_input(lines) -> ([[Pipe]], int, int):
    pipe_map = []
    start_row = -1
    start_col = -1

    for row, l in enumerate(lines):
        if not l:
            continue

        map_row = []

        for col, c in enumerate(l):
            map_row.append(Pipe.for_char(c))

            if c == "S":
                start_row = row
                start_col = col

        pipe_map.append(map_row)

    return pipe_map, start_row, start_col


def tiles_in_loop(pipe_map, start_row, start_col) -> set((int, int)):
    start_pipe_type = start_type(pipe_map, start_row, start_col)

    r, c = (start_row, start_col)
    current_pipe = start_pipe_type

    match current_pipe:
        case Pipe.SEVEN_BEND | Pipe.VERTICAL:
            direction = Direction.SOUTH
        case Pipe.J_BEND | Pipe.HORIZONTAL:
            direction = Direction.WEST
        case Pipe.F_BEND:
            direction = Direction.EAST
        case Pipe.L_BEND:
            direction = Direction.NORTH

    visited = set()

    while True:
        visited.add((r, c))

        match direction:
            case Direction.SOUTH:
                next_row, next_col = r + 1, c
            case Direction.NORTH:
                next_row, next_col = r - 1, c
            case Direction.EAST:
                next_row, next_col = r, c + 1
            case Direction.WEST:
                next_row, next_col = r, c - 1

        r, c = next_row, next_col
        current_pipe = pipe_map[r][c]

        if current_pipe == Pipe.START:
            break

        direction = current_pipe.next_direction(direction)

    return visited


def part1(pipe_map, start_row, start_col):
    loop_tiles = tiles_in_loop(pipe_map, start_row, start_col)

    return len(loop_tiles) // 2


def part2(pipe_map, start_row, start_col):
    pass
