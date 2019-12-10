from itertools import chain
from typing import List, NamedTuple
from fractions import Fraction
from math import copysign, atan2, sqrt, pi as π


class Point(NamedTuple):
    row: int
    col: int


def vector_from_90(origination: Point, dest: Point) -> float:
    translated_dest = Point(dest.row - origination.row, dest.col - origination.col)
    angle = atan2(translated_dest.row, translated_dest.col)

    adjusted_angle = angle - π / 2
    return adjusted_angle if adjusted_angle >= 0 else angle + 3 * π / 2


def distance(p1: Point, p2: Point) -> float:
    translated_p2 = Point(p2.row - p1.row, p2.col - p2.col)
    return sqrt(translated_p2.row ** 2 + translated_p2.col ** 2)


def compute_blocked_spots(source: Point, blocker: Point, maxima: Point) -> List[Point]:
    if source == blocker:
        raise ValueError('source {} and blocker {} are on top of each other!'.format(source, blocker))

    row_diff = blocker.row - source.row
    col_diff = blocker.col - source.col

    # correct for same row/col (this avoids dividing by zero)
    if row_diff == 0:
        col_diff = int(copysign(1, col_diff))
    elif col_diff == 0:
        row_diff = int(copysign(1, row_diff))
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
    blocked_spots = set(chain.from_iterable(
        compute_blocked_spots(asteroid, other, maxima) for other in other_asteroids))

    # print('point {} blocked:'.format(asteroid))

    # for row in range(maxima.row):
    #     for col in range(maxima.col):
    #         p = Point(row, col)
    #         print('.' if p not in blocked_spots else 'B' if p in blocked_spots else '@', end='')
    #     print()

    return sum(1 for other in other_asteroids if other not in blocked_spots)


if __name__ == '__main__':
    print(vector_from_90(Point(0, 0), Point(0, 1)))

    # with open('10_input.txt') as map_inp` ut:
    #     map = [line.strip() for line in map_input.readlines()]
    #
    # asteroids = set(Point(row, col) for row in range(len(map))
    #                 for col in range(len(map[row]))
    #                 if map[row][col] == '#')
    #
    # maxima = Point(len(map), len(map[0]))
    #
    # best_num_visible = 0
    # best_location = None
    #
    # for row in range(maxima.row):
    #     for col in range(maxima.col):
    #         p = Point(row, col)
    #
    #         if p not in asteroids:
    #             # print('.', end='')
    #             continue
    #
    #         num_visible = visible_asteroids_from(p, maxima, [a for a in asteroids if a != p])
    #
    #         if num_visible > best_num_visible:
    #             best_num_visible = num_visible
    #             best_location = p
    #
    #         # print(str(num_visible), end='')
    #     # print()
    #
    # print(best_num_visible)
    # print(best_location)
    # print('{} total asteroids'.format(len(asteroids)))
    #
    # asteroids_sorted = sorted(
    #     sorted(asteroids, key=lambda a: distance(best_location, a)),
    #     key=lambda a: vector_from_90(best_location, a))
    #
    # print(asteroids_sorted)
