import os
from enum import Enum
from math import copysign

from aoc_2019.intcode import IntcodeMachine
from aoc_2019.utils import Point
import curses


class TileType(Enum):
    EMPTY = 0
    WALL = 1
    BLOCK = 2
    PADDLE = 3
    BALL = 4


def paint_screen(current_score, tiles):
    os.system('clear')

    print('==== {:>6} ===='.format(current_score))

    for y in range(23):
        for x in range(42):
            p = Point(x, y)

            if p not in tiles:
                print('🟨', end='')
                continue

            type = tiles[p]

            if type == TileType.EMPTY:
                print('🟨', end='')
            elif type == TileType.WALL:
                print('⬛️️', end='')
            elif type == TileType.BLOCK:
                print('🟥', end='')
            elif type == TileType.PADDLE:
                print('⬜️', end='')
            elif type == TileType.BALL:
                print('🟦', end='')

        print()


if __name__ == '__main__':
    with open('aoc_2019/13_input.txt') as intcode_input:
        machine = IntcodeMachine(intcode_input.readline().strip())

    machine.memory[0] = 2

    current_ball_pos = None
    current_paddle_pos = None

    tiles = {}

    max_x = 0
    max_y = 0
    current_score = 0

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
            current_score = tile_type
            continue

        pos = Point(tile_x, tile_y)
        type = TileType(tile_type)

        if type == TileType.PADDLE:
            current_paddle_pos = pos

        if type == TileType.BALL:
            current_ball_pos = pos

        tiles[pos] = type

        paint_screen(current_score, tiles)
