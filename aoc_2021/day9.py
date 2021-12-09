import math


def find_basin(
    map: list[list[int]], row: int, col: int, seen_points: set[int]
) -> list[int, int]:
    low_points = []

    # Bail if:
    # - we are "off the map"
    # - we've seen this point already
    # - we're on a ridge (height of 9)
    if (
        row < 0
        or row >= len(map)
        or col < 0
        or col >= len(map[0])
        or (row, col) in seen_points
        or map[row][col] == 9
    ):
        return low_points

    low_points.append((row, col))
    seen_points.add((row, col))

    # look left
    if col > 0:
        low_points.extend(find_basin(map, row, col - 1, seen_points))
    # look right
    if col < len(map[row]) - 1:
        low_points.extend(find_basin(map, row, col + 1, seen_points))
    # look up
    if row > 0:
        low_points.extend(find_basin(map, row - 1, col, seen_points))
    # look down
    if row < len(map) - 1:
        low_points.extend(find_basin(map, row + 1, col, seen_points))

    return low_points


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

    for line in problem_input:
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

    seen_points = set()
    basin_sizes = []

    for row, line in enumerate(map):
        for col, height in enumerate(line):
            points_in_basin = find_basin(map, row, col, seen_points)
            basin_sizes.append(len(points_in_basin))

    basin_sizes.sort(reverse=True)

    print(math.prod(basin_sizes[:3]))
