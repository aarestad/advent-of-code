import re

example = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""

example_input = example.split("\n")

with open("input/day5.txt") as input:
    problem_input = [i.strip() for i in input.readlines()]


def point_in_line(line: ((int, int), (int, int)), point: (int, int)) -> bool:
    vertical = line[0][0] == line[1][0]

    if vertical:
        return point[0] == line[0][0] and (
            line[0][1] <= point[1] <= line[1][1] or line[0][1] >= point[1] >= line[1][1]
        )
    else:
        return point[1] == line[0][1] and (
            line[0][0] <= point[0] <= line[1][0] or line[0][0] >= point[0] >= line[1][0]
        )


if __name__ == "__main__":
    cloud_lines = []

    for line in problem_input:
        line_parsed = re.match(r"(\d+),(\d+) -> (\d+),(\d+)", line)
        line_start = (int(line_parsed.group(1)), int(line_parsed.group(2)))
        line_end = (int(line_parsed.group(3)), int(line_parsed.group(4)))
        cloud_lines.append((line_start, line_end))

    xes = []
    ys = []

    for line in cloud_lines:
        xes.append(line[0][0])
        xes.append(line[1][0])
        ys.append(line[0][1])
        ys.append(line[1][1])

    min_x = min(xes)
    max_x = max(xes)

    min_y = min(ys)
    max_y = max(ys)

    field: list[list[int]] = []

    for y in range(max_y + 1):
        field.append([0] * (max_x + 1))

    for line in cloud_lines:
        (start, end) = line

        if start[0] > end[0] or start[1] > end[1]:
            (start, end) = (end, start)

        if start[0] == end[0]:
            for y in range(start[1], end[1] + 1):
                field[y][start[0]] += 1
        elif start[1] == end[1]:
            for x in range(start[0], end[0] + 1):
                field[start[1]][x] += 1
        elif start[0] < end[0] and start[1] < end[1]:  # NW-SE diagonal
            if start[0] > end[0]:
                (start, end) = (end, start)
            for i in range(end[0] - start[0] + 1):
                field[start[1] + i][start[0] + i] += 1
        else:  # NE-SW diagonal
            if start[0] > end[0]:
                (start, end) = (end, start)
            for i in range(end[0] - start[0] + 1):
                field[start[1] - i][start[0] + i] += 1

    intersections = 0

    for line in field:
        for cell in line:
            if cell > 1:
                intersections += 1

    print(intersections)
