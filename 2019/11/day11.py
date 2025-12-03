from enum import Enum
from itertools import repeat

from aoc_2019.intcode import IntcodeMachine
from aoc_2019.utils import Point


class Direction(Enum):
    UP = 0
    LEFT = 1
    DOWN = 2
    RIGHT = 3


class Color(Enum):
    BLACK = 0
    WHITE = 1


if __name__ == "__main__":
    with open("11_input.txt") as program:
        machine = IntcodeMachine(program.readline().strip())

    current_pos = Point(0, 0)
    current_orientation = Direction.UP

    painted_tiles = {current_pos: Color.WHITE}

    while True:
        try:
            current_color = painted_tiles[current_pos]
        except KeyError:
            current_color = Color.BLACK

        machine.send(current_color.value)
        new_color_raw = machine.receive()

        if new_color_raw is None:
            break

        new_color = Color(new_color_raw)

        painted_tiles[current_pos] = new_color

        rotation = machine.receive()

        if rotation is None:
            break

        # noinspection PyTypeChecker
        current_orientation = Direction(
            (current_orientation.value + (-1 if rotation == 0 else 1)) % 4
        )

        if current_orientation == Direction.UP:
            current_pos = Point(current_pos.x, current_pos.y + 1)
        elif current_orientation == Direction.DOWN:
            current_pos = Point(current_pos.x, current_pos.y - 1)
        elif current_orientation == Direction.RIGHT:
            current_pos = Point(current_pos.x + 1, current_pos.y)
        elif current_orientation == Direction.LEFT:
            current_pos = Point(current_pos.x - 1, current_pos.y)
        else:
            raise ValueError("unknown direction: {}".format(current_orientation))

    max_x = max(p.x for p in painted_tiles.keys())
    min_x = min(p.x for p in painted_tiles.keys())
    max_y = max(p.y for p in painted_tiles.keys())
    min_y = min(p.y for p in painted_tiles.keys())

    canvas = []

    for _ in range(max_y - min_y + 1):
        canvas.append(list(repeat(" ", max_x - min_x + 1)))

    for tile, color in painted_tiles.items():
        if color == Color.WHITE:
            y = tile.y - min_y
            x = tile.x - min_x
            canvas[y][x] = "#"

    canvas[-min_y][-min_x] = "@"

    # turn it upside down!
    for line in reversed(canvas):
        print("".join(reversed(line)))
