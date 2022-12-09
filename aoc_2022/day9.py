if __name__ == "__main__":
    example = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

    example_input = example.split("\n")

    with open("input/day9.txt") as input:
        problem_input = [i.strip() for i in input.readlines()]

    tail_locations = set()
    current_head = (0, 0)
    current_tail = (0, 0)
    tail_locations.add(current_tail)

    for line in problem_input:
        (dir, distance) = line.split()
        distance = int(distance)

        while distance > 0:
            print(f"moving {dir}")
            distance -= 1

            if dir == "U":
                current_head = (current_head[0] + 1, current_head[1])
            elif dir == "D":
                current_head = (current_head[0] - 1, current_head[1])
            elif dir == "R":
                current_head = (current_head[0], current_head[1] + 1)
            elif dir == "L":
                current_head = (current_head[0], current_head[1] - 1)

            delta_r = current_head[0] - current_tail[0]
            delta_c = current_head[1] - current_tail[1]

            primary_move = (delta_r == 0 and delta_c > 1) or (
                delta_r > 1 and delta_c == 0
            )
            secondary_move = abs(delta_r) > 1 or abs(delta_c) > 1

            if primary_move:
                if dir == "U":
                    current_tail = (current_tail[0] + 1, current_tail[1])
                elif dir == "D":
                    current_tail = (current_tail[0] - 1, current_tail[1])
                elif dir == "R":
                    current_tail = (current_tail[0], current_tail[1] + 1)
                elif dir == "L":
                    current_tail = (current_tail[0], current_tail[1] - 1)
            elif secondary_move:
                if dir == "U":
                    current_tail = (
                        current_tail[0] + 1,
                        current_tail[1] + (1 if delta_c > 0 else -1),
                    )
                elif dir == "D":
                    current_tail = (
                        current_tail[0] - 1,
                        current_tail[1] + (1 if delta_c > 0 else -1),
                    )
                elif dir == "R":
                    current_tail = (
                        current_tail[0] + (1 if delta_r > 0 else -1),
                        current_tail[1] + 1,
                    )
                elif dir == "L":
                    current_tail = (
                        current_tail[0] + (1 if delta_r > 0 else -1),
                        current_tail[1] - 1,
                    )

            print(f"head={current_head}, tail={current_tail}")

            tail_locations.add(current_tail)
    print(len(tail_locations))
