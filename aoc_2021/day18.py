from dataclasses import dataclass
import re
from typing import Union, ForwardRef


@dataclass
class NumberPair:
    left: Union[int, "NumberPair"]
    right: Union[int, "NumberPair"]
    nesting_level: int


def parse_number_pair(num_pair_str: str, level: int = -1) -> NumberPair:
    left = None
    right = None

    for i, c in enumerate(num_pair_str):
        match c:
            case "[":
                level += 1
                return parse_number_pair(num_pair_str[i + 1 :], level)
        case c.isdigit():
            if not left:
                left = int(c)
            else:
                right = int(c)
        if c == "]":
            return NumberPair(left, right, level)

        raise ValueError(f"Invalid character {c}")


if __name__ == "__main__":
    example = """[1,1]
[2,2]
[3,3]
[4,4]"""

    example_input = example.split("\n")

    with open("input/day18.txt") as input:
        problem_input = [i.strip() for i in input.readlines()]

    for line in example:
        print(parse_number_pair(line))
