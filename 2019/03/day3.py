from typing import Tuple, Optional


if __name__ == "__main__":
    with open("03_input.txt") as wires:
        wire_1_dirs = wires.readline().strip().split(",")
        wire_2_dirs = wires.readline().strip().split(",")

    wire_1_points_in_order = [(0, 0)]
    wire_1_points = set(wire_1_points_in_order)
    x = 0
    y = 0

    for dir_and_distance in wire_1_dirs:
        (direc, distance) = (dir_and_distance[0], int(dir_and_distance[1:]))

        for step in range(distance):
            if direc == "U":
                y += 1
            elif direc == "D":
                y -= 1
            elif direc == "R":
                x += 1
            elif direc == "L":
                x -= 1
            else:
                raise ValueError("unknown direction: {}".format(direc))

            wire_1_points.add((x, y))
            wire_1_points_in_order.append((x, y))

    smallest_intersection: Optional[Tuple] = None
    x = 0
    y = 0
    steps = 0

    for dir_and_distance in wire_2_dirs:
        (direc, distance) = (dir_and_distance[0], int(dir_and_distance[1:]))

        for step in range(distance):
            if direc == "U":
                y += 1
            elif direc == "D":
                y -= 1
            elif direc == "R":
                x += 1
            elif direc == "L":
                x -= 1
            else:
                raise ValueError("unknown direction: {}".format(direc))

            steps += 1

            if (x, y) in wire_1_points:
                wire_1_point_steps = wire_1_points_in_order.index((x, y))

                if (
                    smallest_intersection is None
                    or steps + wire_1_point_steps < smallest_intersection[2]
                ):
                    smallest_intersection = (x, y, steps + wire_1_point_steps)

    print(smallest_intersection)
