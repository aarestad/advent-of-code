if __name__ == "__main__":
    example = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

    example2 = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""

    example_input = example.split("\n")
    example2_input = example2.split("\n")

    with open("input/day9.txt") as input:
        problem_input = [i.strip() for i in input.readlines()]

    tail_locations = set()
    tail_locations.add((0, 0))
    # part 1: knots = [(0, 0)] * 2
    knots = [(0, 0)] * 10

    for line in problem_input:
        (dir, distance) = line.split()
        distance = int(distance)

        while distance > 0:
            distance -= 1
            current_head = knots[0]

            if dir == "U":
                knots[0] = (current_head[0] + 1, current_head[1])
            elif dir == "D":
                knots[0] = (current_head[0] - 1, current_head[1])
            elif dir == "R":
                knots[0] = (current_head[0], current_head[1] + 1)
            elif dir == "L":
                knots[0] = (current_head[0], current_head[1] - 1)

            for i in range(1, len(knots)):
                current_knot = knots[i]
                prev_knot = knots[i - 1]

                delta_r = prev_knot[0] - current_knot[0]
                delta_c = prev_knot[1] - current_knot[1]

                if delta_r < -1 or (delta_r == -1 and abs(delta_c) > 1):
                    r_move = -1
                elif delta_r > 1 or (delta_r == 1 and abs(delta_c) > 1):
                    r_move = 1
                else:
                    r_move = 0

                if delta_c < -1 or (delta_c == -1 and abs(delta_r) > 1):
                    c_move = -1
                elif delta_c > 1 or (delta_c == 1 and abs(delta_r) > 1):
                    c_move = 1
                else:
                    c_move = 0

                knots[i] = (current_knot[0] + r_move, current_knot[1] + c_move)

            tail_locations.add(knots[-1])

    print(len(tail_locations))
