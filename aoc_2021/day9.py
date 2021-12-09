if __name__ == "__main__":
    example = """2199943210
3987894921
9856789892
8767896789
9899965678"""

    example_input = example.split("\n")

    with open("input/day9.txt") as input:
        problem_input = [i.strip() for i in input.readlines()]

    map = []

    for line in example_input:
        map.append([int(d) for d in line])

    risk_level = 0

    for row_num, line in enumerate(map):
        for col_num, height in enumerate(line):
            candidates = []

            if row_num > 0:
                candidates.append(map[row_num - 1][col_num])
            if row_num < len(map) - 1:
                candidates.append(map[row_num + 1][col_num])
            if col_num > 0:
                candidates.append(map[row_num][col_num - 1])
            if col_num < len(line) - 1:
                candidates.append(map[row_num][col_num + 1])

            if all(c > height for c in candidates):
                risk_level += height + 1

    print(risk_level)

    seen_points = {}
    largest_basins = []

    for row_num, line in enumerate(map):
        for col_num, height in enumerate(line):
            if height == 9:
                continue

            # get lower points up, down, left, right
            # recurse on up to up/left/right
            # recurse on down to down/left/right
            # recurse on left to left/up/down
            # recurse on right to right/up/down
