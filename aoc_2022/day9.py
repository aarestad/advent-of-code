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

            for i in range(1, len(knots)):
                current_knot = knots[i]
                prev_knot = knots[i - 1]

                delta_r = prev_knot[0] - current_knot[0]
                delta_c = prev_knot[1] - current_knot[1]

                primary_move = (delta_r == 0 and abs(delta_c) > 1) or (
                    abs(delta_r) > 1 and delta_c == 0
                )
                secondary_move = not primary_move and (
                    abs(delta_r) > 1 or abs(delta_c) > 1
                )

                if primary_move:
                    if dir == "U":
                        knots[i] = (current_knot[0] + 1, current_knot[1])
                    elif dir == "D":
                        knots[i] = (current_knot[0] - 1, current_knot[1])
                    elif dir == "R":
                        knots[i] = (current_knot[0], current_knot[1] + 1)
                    elif dir == "L":
                        knots[i] = (current_knot[0], current_knot[1] - 1)
                elif secondary_move:
                    if dir == "U":
                        knots[i] = (
                            current_knot[0] + 1,
                            current_knot[1] + (1 if delta_c > 0 else -1),
                        )
                    elif dir == "D":
                        knots[i] = (
                            current_knot[0] - 1,
                            current_knot[1] + (1 if delta_c > 0 else -1),
                        )
                    elif dir == "R":
                        knots[i] = (
                            current_knot[0] + (1 if delta_r > 0 else -1),
                            current_knot[1] + 1,
                        )
                    elif dir == "L":
                        knots[i] = (
                            current_knot[0] + (1 if delta_r > 0 else -1),
                            current_knot[1] - 1,
                        )

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
