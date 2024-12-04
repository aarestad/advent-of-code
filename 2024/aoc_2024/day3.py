import re

MUL = re.compile(
    r"mul\((\d{1,3}),(\d{1,3})\)",
)

DO_OR_DONT_OR_MUL = re.compile(r"(don't\(\)|do\(\)|mul\((\d{1,3}),(\d{1,3})\))")

if __name__ == "__main__":
    example = (
        """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""
    )

    with open("input/day3.txt") as input:
        problem_input = "".join(i.strip() for i in input.readlines())

    print(f"part 1: {sum(int(m[1]) * int(m[2]) for m in MUL.finditer(problem_input))}")

    do_mult = True
    part_2_mul_sum = 0

    for m in DO_OR_DONT_OR_MUL.finditer(problem_input):
        match = m[1]

        if match == "don't()":
            do_mult = False
        elif match == "do()":
            do_mult = True
        elif do_mult:  # mul
            part_2_mul_sum += int(m[2]) * int(m[3])

    print(f"part 2: {part_2_mul_sum}")
