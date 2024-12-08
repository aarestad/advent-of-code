from typing import List
from operator import mul, add


# returns the pos-th trit of n
def trit_at(n: int, pos: int) -> int:
    pass


def part_1_calibration_passes(result: int, vals: List[int]) -> bool:
    num_ops = len(vals) - 1

    for attempt in range(2**num_ops):
        cal_sum = vals[0]

        for op_pos in range(num_ops):
            op = add if attempt & 2**op_pos else mul
            cal_sum = op(cal_sum, vals[op_pos + 1])

        if cal_sum == result:
            print(f"attempt {attempt} for {result}: {vals} succeeds")
            return True

    print(f"{result}: {vals} fails")
    return False


def part_2_calibration_passes(result: int, vals: List[int]) -> bool:
    num_ops = len(vals) - 1

    for attempt in range(3**num_ops):
        cal_sum = vals[0]

        for op_pos in range(num_ops):
            op = add if attempt & 2**op_pos else mul
            cal_sum = op(cal_sum, vals[op_pos + 1])

        if cal_sum == result:
            print(f"attempt {attempt} for {result}: {vals} succeeds")
            return True

    print(f"{result}: {vals} fails")
    return False


if __name__ == "__main__":
    example = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""

    example_input = example.split("\n")

    with open("input/day7.txt") as input:
        problem_input = [i.strip() for i in input.readlines()]

    good_calibration_sum = 0

    for l in problem_input:
        result, operands = l.split(":")
        result = int(result)

        if part_1_calibration_passes(
            int(result), [int(o) for o in operands.strip().split()]
        ):
            good_calibration_sum += result

    print(f"part 1 sum: {good_calibration_sum}")
