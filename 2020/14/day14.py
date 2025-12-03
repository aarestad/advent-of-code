import re
from typing import List, Optional


def mask_value(raw_value: int, mask: List[Optional[str]]):
    value = 0

    for idx, mask_bit in enumerate(mask[::-1]):
        if (mask_bit == "X" and raw_value & 2**idx) or mask_bit == "1":
            value += 2**idx

    return value


def compute_floating_addresses(raw_addr: int, mask: List[Optional[str]]):
    addresses = []
    num_anys = sum(1 for bit in mask if bit is "X")

    for addr in range(2**num_anys):
        mask_copy = mask[:]
        binary_addr = "{0:b}".format(addr)


example = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0"""


if __name__ == "__main__":
    part_one_memory = {}
    part_two_memory = {}

    mask_re = re.compile(r"mask = (\w+)")
    write_re = re.compile(r"mem\[(\d+)] = (\d+)")

    with open("input/day14.txt") as program:
        # for line in program:
        for line in example.split("\n"):
            if result := mask_re.match(line):
                mask = result[1]
            elif result := write_re.match(line):
                (addr, raw_value) = result.groups()
                part_one_memory[addr] = mask_value(int(raw_value), mask)

    print(sum(part_one_memory.values()))
