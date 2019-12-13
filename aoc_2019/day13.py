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


def paint_screen(current_score, tiles, window: curses.window):
    window.addstr(0, 0, '==== score: {:>5} ===='.format(current_score))

    for y in range(23):
        for x in range(42):
            type = tiles.get(Point(x, y), TileType.EMPTY)

            if type == TileType.WALL:
                # print('⬛️️', end='')
                # window.attrset(curses.color_pair(curses.COLOR_BLACK))
                window.addch(y + 1, x, '-' if y == 0 else '|')
            elif type == TileType.BLOCK:
                # print('🟥', end='')
                # window.attrset(curses.color_pair(curses.COLOR_RED))
                window.addch(y + 1, x, '*')
            elif type == TileType.PADDLE:
                # print('⬜️', end='')
                # window.attrset(curses.color_pair(curses.COLOR_WHITE))
                window.addch(y + 1, x, '_')
            elif type == TileType.BALL:
                # print('🟦', end='')
                # window.attrset(curses.color_pair(curses.COLOR_BLUE))
                window.addch(y + 1, x, 'O')
            else:
                # print('🟨', end='')
                # window.attrset(curses.color_pair(curses.COLOR_YELLOW))
                window.addch(y + 1, x, ' ')

    window.refresh()


def main(stdscr):
    with open('aoc_2019/13_input.txt') as intcode_input:
        machine = IntcodeMachine(intcode_input.readline().strip())

    machine.memory[0] = 2

    current_ball_pos = None
    current_paddle_pos = None

    tiles = {}

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

        paint_screen(current_score, tiles, stdscr)


if __name__ == '__main__':
    curses.wrapper(main)
