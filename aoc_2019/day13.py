from enum import Enum

from aoc_2019.intcode import IntcodeMachine
from aoc_2019.utils import Point


class TileType(Enum):
    EMPTY = 0
    WALL = 1
    BLOCK = 2
    PADDLE = 3
    BALL = 4


class JoystickPos(Enum):
    LEFT = -1
    NEUTRAL = 0
    RIGHT = 1


if __name__ == '__main__':
    with open('13_input.txt') as intcode_input:
        machine = IntcodeMachine(intcode_input.readline().strip())

    machine.memory[0] = 2
    machine.start()

    while True:
        machine.send(JoystickPos.NEUTRAL.value)
        (tile_x, tile_y, tile_type) = (machine.receive(), machine.receive(), machine.receive())

        if any((tile_x is None, tile_y is None, tile_type is None)):
            break

        if tile_x == -1 and tile_y == 0:
            print('current score is {}'.format(tile_type))
            continue

        pos = Point(tile_x, tile_y)
        type = TileType(tile_type)

        if type == TileType.PADDLE:
            print('paddle at {}'.format(pos))

        if type == TileType.BALL:
            print('ball is at {}'.format(pos))
