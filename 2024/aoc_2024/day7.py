from typing import List
from operator import mul, add


def bits(n):
    if n == 0:
        yield 0
        return

    bitmask = 1
    while n >= bitmask:
        yield 1 if n & bitmask else 0
        bit <<= 1


def part_1_calibration_passes(result: int, vals: List[int]) -> bool:
    num_ops = len(vals) - 1
    print(f"{num_ops} ops")

    for attempt in range(2**num_ops):
        print(f"attempt: {attempt}")
        cal_sum = vals[0]

        for op_pos in range(1, num_ops + 1):
            print(f"op_pos = {op_pos}")
            op = add if attempt & 2**op_pos else mul
            print(f"{cal_sum} {op} {vals[op_pos]} ")
            cal_sum += op(cal_sum, vals[op_pos])

        print(f"total sum: {cal_sum}")

        if cal_sum == result:
            print(f"attempt {attempt} succeeds")
            return True

    return False


if __name__ == "__main__":
    example = """3267: 81 40 27"""

    example_input = example.split("\n")

    with open("input/day7.txt") as input:
        problem_input = [i.strip() for i in input.readlines()]

    good_calibration_sum = 0

    for l in example_input:
        result, operands = l.split(":")
        result = int(result)

        if part_1_calibration_passes(
            int(result), [int(o) for o in operands.strip().split()]
        ):
            good_calibration_sum += result

    print(f"part 1 sum: {good_calibration_sum}")
