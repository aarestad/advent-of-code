from typing import List


def part_1_safe(r: List[int]) -> bool:
    decreasing = None

    for l in range(len(r) - 1):
        diff = r[l] - r[l + 1]

        if abs(diff) not in range(1, 4):
            return False

        if decreasing is not None:
            if diff > 0 and not decreasing or diff < 0 and decreasing:
                return False
        else:
            decreasing = diff > 0

    return True


def part_2_safe(r: List[int]) -> bool:
    return part_1_safe(r) or any(
        part_1_safe(r[0:l] + r[l + 1 :]) for l in range(len(r))
    )


if __name__ == "__main__":
    example = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

    example_input = example.split("\n")

    with open("input/day2.txt") as input:
        problem_input = [i.strip() for i in input.readlines()]

    reports = [[int(l) for l in r.split()] for r in problem_input]

    for r in reports:
        print(f"{r}: {part_1_safe(r)}")

    print(sum(1 for r in reports if part_1_safe(r)))
    print(sum(1 for r in reports if part_2_safe(r)))
