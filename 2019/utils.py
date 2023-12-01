from typing import NamedTuple


class Point(NamedTuple):
    x: int
    y: int


def lcm(first_num: int, second_num: int) -> int:
    max_num = first_num if first_num >= second_num else second_num
    common_mult = max_num

    while (common_mult % first_num > 0) or (common_mult % second_num > 0):
        common_mult += max_num

    return common_mult
