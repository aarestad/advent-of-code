import re

def part1(input):
    ranges = []
    ingredients = []

    for line in input:
        if "-" in line:
            start, end = line.split("-")
            ranges.append(range(int(start), int(end) + 1))
        elif re.match("[0-9]", line):
            ingredients.append(int(line))

    fresh = []

    for i in ingredients:
        for r in ranges:
            if i in r:
                fresh.append(r)
                break

    return fresh

def part2(input):
    ranges = []

    for line in input:
        if "-" in line:
            start, end = line.split("-")
            ranges.append(range(int(start), int(end) + 1))
        else:
            break

    new_ranges = []
    unprocessed = []

    for i, r in enumerate(unprocessed):
        for o in  ranges[i+1:]:

        for other_range in rest_of_ranges:
            if not(r.end < other_range.start or other_range.end < r.start):

    num_ingredients = 0

    for r in consolidated_ranges(ranges):
        num_ingredients += r.stop - r.start

    return num_ingredients


if __name__ == "__main__":
    example = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""

    example_input = example.split("\n")
    print(f"part 1 example: {len(part1(example_input))}")
    print(f"part 1 example: {len(part2(example_input))}")

    with open("input/day5.txt") as input:
        problem_input = [i.strip() for i in input.readlines()]
        print(f"part 1: {len(part1(problem_input))}")

