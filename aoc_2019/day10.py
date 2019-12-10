from itertools import chain
from typing import List, NamedTuple
from fractions import Fraction
from math import copysign


class Point(NamedTuple):
    row: int
    col: int


def compute_blocked_spots(source: Point, blocker: Point, maxima: Point) -> List[Point]:
    if source == blocker:
        raise ValueError('source {} and blocker {} are on top of each other!'.format(source, blocker))

    row_diff = blocker.row - source.row
    col_diff = blocker.col - source.col

    # correct for same row/col (this avoids dividing by zero)
    if row_diff == 0:
        col_diff = 1
    elif col_diff == 0:
        row_diff = 1
    # otherwise, reduce x_diff/y_diff so they're relatively prime
    else:
        row_over_col = Fraction(row_diff, col_diff)
        row_diff = int(copysign(row_over_col.numerator, row_diff))
        col_diff = int(copysign(row_over_col.denominator, col_diff))

    next_row = blocker.row + row_diff
    next_col = blocker.col + col_diff

    blocked_spots = []

    while next_row in range(maxima.row) and next_col in range(maxima.col):
        blocked_spots.append(Point(next_row, next_col))
        next_row += row_diff
        next_col += col_diff

    return blocked_spots


def visible_asteroids_from(asteroid: Point, maxima: Point, other_asteroids: List[Point]) -> int:
    blocked_spot_lists = list(compute_blocked_spots(asteroid, other, maxima) for other in other_asteroids)
    blocked_spots = list(chain.from_iterable(blocked_spot_lists))

    seen_asteroids = list(other for other in other_asteroids if other not in blocked_spots)
    return len(seen_asteroids)


if __name__ == '__main__':
    with open('10_small_input.txt') as map_input:
        map = [line.strip() for line in map_input.readlines()]

    asteroids = [Point(row, col) for row in range(len(map))
                 for col in range(len(map[row]))
                 if map[row][col] == '#']

    maxima = Point(len(map), len(map[0]))

    for row in range(maxima.row):
        for col in range(maxima.col):
            p = Point(row, col)
            print('.' if p not in asteroids else str(visible_asteroids_from(p, maxima, [a for a in asteroids if a != p])), end='')
        print()
