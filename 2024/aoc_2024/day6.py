from enum import Enum
from typing import NamedTuple


class Location(NamedTuple):
    row: int
    col: int


class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

    def new_location_from(self, loc: Location) -> Location:
        match self:
            case Direction.UP:
                return Location(loc.row - 1, loc.col)
            case Direction.RIGHT:
                return Location(loc.row, loc.col + 1)
            case Direction.DOWN:
                return Location(loc.row + 1, loc.col)
            case Direction.LEFT:
                return Location(loc.row, loc.col - 1)


def traverse_map_with_possible_obstacle(
    original_map, starting_location: Location, obstacle_loc: Location | None = None
) -> tuple[bool, set[Location]]:
    if obstacle_loc:
        map = []

        for r in original_map:
            map.append(r[:])

        map[obstacle_loc.row] = (
            original_map[obstacle_loc.row][: obstacle_loc.col]
            + "#"
            + original_map[obstacle_loc.row][obstacle_loc.col + 1 :]
        )
    else:
        map = original_map

    visited = set()
    visited.add(starting_location)

    visited_with_orientation = set()

    dir = Direction.UP
    current_loc = starting_location
    visited_with_orientation.add((starting_location, dir))

    while True:
        next_loc = dir.new_location_from(current_loc)

        if (
            next_loc.row < 0
            or next_loc.row >= len(map)
            or next_loc.col < 0
            or next_loc.col >= len(map[0])
        ):
            # we're off the board
            return False, visited

        if map[next_loc.row][next_loc.col] == "#":
            dir = Direction((dir.value + 1) % 4)  #  rotate and stay put
        else:
            current_loc = next_loc

            if (current_loc, dir) in visited_with_orientation:
                # we are about to start a loop
                return True, visited

            visited.add(next_loc)
            visited_with_orientation.add((current_loc, dir))


if __name__ == "__main__":
    example = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

    example_input = example.split("\n")

    with open("input/day6.txt") as input:
        problem_input = [i.strip() for i in input.readlines()]

    map = problem_input

    for row_num, row in enumerate(map):
        if "^" in row:
            guard_row_num = row_num
            guard_col_num = row.index("^")
            break
    else:
        raise "couldn't find guard's row"

    starting_location = Location(guard_row_num, guard_col_num)

    _, visited = traverse_map_with_possible_obstacle(map, starting_location)

    print(f"{len(visited)} distinct positions visited")

    obstruction_locs = 0

    print(f"total chars in map: {len(map) * len(map[0])}")

    for r in range(len(map)):
        for c in range(len(map[r])):
            char_no = r * len(map) + c
            if char_no % 1000 == 0:
                print(f"char_no {char_no}")

            if map[r][c] != "#":
                looped, _ = traverse_map_with_possible_obstacle(
                    map, starting_location, Location(r, c)
                )

                if looped:
                    obstruction_locs += 1

    print(f"{obstruction_locs} obstruction locations")
