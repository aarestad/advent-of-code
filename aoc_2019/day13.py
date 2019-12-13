from enum import Enum
from math import copysign

from aoc_2019.intcode import IntcodeMachine
from aoc_2019.utils import Point


class TileType(Enum):
    EMPTY = 0
    WALL = 1
    BLOCK = 2
    PADDLE = 3
    BALL = 4


if __name__ == '__main__':
    with open('13_input.txt') as intcode_input:
        machine = IntcodeMachine(intcode_input.readline().strip())

    machine.memory[0] = 2

    current_ball_pos = None
    current_paddle_pos = None

    while True:
        if not (current_ball_pos and current_paddle_pos):
            machine.send(0)
        else:
            paddle_ball_diff = current_ball_pos.x - current_paddle_pos.x
            machine.send(0 if paddle_ball_diff == 0 else int(copysign(1, paddle_ball_diff)))

        (tile_x, tile_y, tile_type) = (machine.receive(), machine.receive(), machine.receive())

        if any((tile_x is None, tile_y is None, tile_type is None)):
            break

        if tile_x == -1 and tile_y == 0:
            print('current score is {}'.format(tile_type))
            continue

        pos = Point(tile_x, tile_y)
        type = TileType(tile_type)

        if type == TileType.PADDLE:
            current_paddle_pos = pos

        if type == TileType.BALL:
            current_ball_pos = pos
