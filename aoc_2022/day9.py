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
    knots = [(0, 0)] * 10

    for line in example2_input:
        (dir, distance) = line.split()
        distance = int(distance)

        print(f"== {dir} {distance} ==")
        print()

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

            print(f"head moved from {current_head} to {knots[0]}")

            for i in range(1, len(knots)):
                current_knot = knots[i]
                prev_knot = knots[i - 1]
                print(f"{i}={current_knot} {i-1}={prev_knot}")

                delta_r = prev_knot[0] - current_knot[0]
                delta_c = prev_knot[1] - current_knot[1]
                print(f"delta_r={delta_r} delta_c={delta_c}")

                if abs(delta_r) > 1:
                    r_move = -1 if delta_r < 0 else 1
                else:
                    r_move = 0

                if abs(delta_c) > 1:
                    c_move = -1 if delta_c < 0 else 1
                else:
                    c_move = 0

                knots[i] = (current_knot[0] + r_move, current_knot[1] + c_move)
                if knots[i] == current_knot:
                    print(f"no move for {i}")
                else:
                    print(f"{i}: {current_knot} -> {knots[i]}")

            tail_locations.add(knots[-1])

        for r in range(24, -1, -1):
            for c in range(30):
                for i in range(len(knots)):
                    if (r - 5, c - 12) == knots[i]:
                        print("H" if i == 0 else i, end="")
                        break
                else:
                    if r == 5 and c == 12:
                        print("s", end="")
                    else:
                        print(".", end="")
            print()
        print()
    print(len(tail_locations))

    for r in range(24, -1, -1):
        for c in range(30):
            if r == 5 and c == 12:
                print("s", end="")
            elif (r - 5, c - 12) in tail_locations:
                print("#", end="")
            else:
                print(".", end="")
        print()
