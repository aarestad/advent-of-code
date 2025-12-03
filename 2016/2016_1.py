import sys


def solve_part_1(directions):
    curr_x = 0
    curr_y = 0

    currently_facing = 1  # 0 = E, 1, N, 2 = W, 3 = S (mod 4)

    for direction in directions:
        # turn right or left
        if direction[0] == "R":
            currently_facing -= 1
        elif direction[0] == "L":
            currently_facing += 1
        else:
            raise RuntimeError("unknown direction: " + direction[0])

        travel_distance = int(direction[1:])

        if currently_facing % 4 == 0:  # E
            curr_x += travel_distance
        elif currently_facing % 4 == 1:  # N
            curr_y += travel_distance
        elif currently_facing % 4 == 2:  # W
            curr_x -= travel_distance
        elif currently_facing % 4 == 3:  # S
            curr_y -= travel_distance

    print(
        "part 1: hq is %s blocks away at (%s, %s)"
        % (abs(curr_x) + abs(curr_y), curr_x, curr_y)
    )


def solve_part_2(directions):
    curr_x = 0
    curr_y = 0

    currently_facing = 1  # 0 = E, 1, N, 2 = W, 3 = S (mod 4)

    currently_visited = set((0, 0))

    for direction in directions:
        # turn right or left
        if direction[0] == "R":
            currently_facing -= 1
        elif direction[0] == "L":
            currently_facing += 1
        else:
            raise RuntimeError("unknown direction: " + direction[0])

        travel_distance = int(direction[1:])

        while travel_distance > 0:
            if currently_facing % 4 == 0:  # E
                curr_x += 1
            elif currently_facing % 4 == 1:  # N
                curr_y += 1
            elif currently_facing % 4 == 2:  # W
                curr_x -= 1
            elif currently_facing % 4 == 3:  # S
                curr_y -= 1

            if (curr_x, curr_y) in currently_visited:
                print(
                    "part 2: hq is %s blocks away at (%s, %s)"
                    % (abs(curr_x) + abs(curr_y), curr_x, curr_y)
                )
                return

            currently_visited.add((curr_x, curr_y))
            travel_distance -= 1


for line in open("input_1.txt"):
    directions = line.strip().split(", ")

solve_part_1(directions)
solve_part_2(directions)
