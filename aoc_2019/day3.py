from operator import add
from typing import Tuple, Optional

if __name__ == '__main__':
    with open('03_input.txt') as wires:
        wire_1_dirs = wires.readline().strip().split(',')
        wire_2_dirs = wires.readline().strip().split(',')

    wire_1_points = set()
    x = 0
    y = 0

    for dir_and_distance in wire_1_dirs:
        (direc, distance) = (dir_and_distance[0], int(dir_and_distance[1:]))

        for step in range(distance):
            if direc == 'U':
                y += 1
            elif direc == 'D':
                y -= 1
            elif direc == 'R':
                x += 1
            elif direc == 'L':
                x -= 1
            else:
                raise ValueError('unknown direction: {}'.format(direc))

            wire_1_points.add((x, y))

    smallest_intersection: Optional[Tuple] = None
    x = 0
    y = 0

    for dir_and_distance in wire_2_dirs:
        (direc, distance) = (dir_and_distance[0], int(dir_and_distance[1:]))

        for step in range(distance):
            if direc == 'U':
                y += 1
            elif direc == 'D':
                y -= 1
            elif direc == 'R':
                x += 1
            elif direc == 'L':
                x -= 1
            else:
                raise ValueError('unknown direction: {}'.format(direc))

            if (x, y) in wire_1_points:
                if smallest_intersection is None or abs(x) + abs(y) < add(*[abs(c) for c in smallest_intersection]):
                    smallest_intersection = (x, y)

    print(smallest_intersection)