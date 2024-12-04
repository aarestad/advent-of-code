import re

PART_1_MUL = re.compile(
    r"mul\((\d{1,3}),(\d{1,3})\)",
)

if __name__ == "__main__":
    example = (
        """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""
    )

    with open("input/day3.txt") as input:
        problem_input = "".join(i.strip() for i in input.readlines())

    print(sum(int(m[1]) * int(m[2]) for m in PART_1_MUL.finditer(problem_input)))
