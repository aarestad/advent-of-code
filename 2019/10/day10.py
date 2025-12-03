from itertools import chain
from typing import List, NamedTuple
from fractions import Fraction
from math import copysign, atan2, pi as π


class Point(NamedTuple):
    row: int
    col: int


def angle_rotated_90_deg_clockwise(origination: Point, dest: Point) -> float:
    # up is down, black is white...
    origination = Point(-origination.row, origination.col)
    dest = Point(-dest.row, dest.col)
    translated_dest = Point(dest.row - origination.row, dest.col - origination.col)
    angle = atan2(translated_dest.row, translated_dest.col)

    adjusted_angle = angle - π / 2
    return adjusted_angle if adjusted_angle > 0 else adjusted_angle + 2 * π


def compute_blocked_spots(source: Point, blocker: Point, maxima: Point) -> List[Point]:
    if source == blocker:
        raise ValueError(
            "source {} and blocker {} are on top of each other!".format(source, blocker)
        )

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


def visible_asteroids_from(
    asteroid: Point, maxima: Point, other_asteroids: List[Point]
) -> List[Point]:
    blocked_spots = set(
        chain.from_iterable(
            compute_blocked_spots(asteroid, other, maxima) for other in other_asteroids
        )
    )

    return [other for other in other_asteroids if other not in blocked_spots]


if __name__ == "__main__":
    with open("10_input.txt") as map_input:
        map = [line.strip() for line in map_input.readlines()]

    asteroids = set(
        Point(row, col)
        for row in range(len(map))
        for col in range(len(map[row]))
        if map[row][col] == "#"
    )

    maxima = Point(len(map), len(map[0]))

    best_num_visible = 0
    base_location = None

    for row in range(maxima.row):
        for col in range(maxima.col):
            p = Point(row, col)

            if p not in asteroids:
                continue

            num_visible = len(
                visible_asteroids_from(p, maxima, [a for a in asteroids if a != p])
            )

            if num_visible > best_num_visible:
                best_num_visible = num_visible
                base_location = p

    removed = set()
    most_recent_angle = None

    while True:
        other_asteroids = [
            a for a in asteroids if a != base_location and a not in removed
        ]
        visible_asteroids = visible_asteroids_from(
            base_location, maxima, other_asteroids
        )

        for a in sorted(
            visible_asteroids,
            key=lambda a: angle_rotated_90_deg_clockwise(base_location, a),
            reverse=True,
        ):
            print("vaporizing {}".format(a))
            removed.add(a)
            most_recent_angle = angle_rotated_90_deg_clockwise(base_location, a)

            if len(removed) == 200:
                exit()
