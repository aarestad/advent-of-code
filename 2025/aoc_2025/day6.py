import re
from functools import reduce
from operator import add, mul


def part1(input):
    total = 0

    for problem in zip(*(re.split(r'\s+', l.strip()) for l in input)):
        op = mul if problem[-1] == "*" else add
        base = 1 if op == mul else 0
        result = reduce(op, (int(i) for i in  problem[:-1]), base)
        print(problem, result)
        total += result

    return total

def part2(input):
    total = 0

    for problem in zip(*(re.split(r'\s+', l.strip()) for l in input)):
        op = mul if problem[-1] == "*" else add
        base = 1 if op == mul else 0
        result = reduce(op, parse_nums(problem[:-1]), base)
        print(problem, result)
        total += result

    return total

def parse_nums(num_strs):
    padded

if __name__ == "__main__":
    example = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """

    example_input = example.split("\n")
    print(part1(example_input))

    with open("input/day6.txt") as input:
        problem_input = [i.strip() for i in input.readlines()]
        print(part1(problem_input))
