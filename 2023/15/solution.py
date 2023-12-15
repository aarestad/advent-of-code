## advent of code 2023
## https://adventofcode.com/2023
## day 15

from dataclasses import dataclass
from typing import List


@dataclass
class Lens:
    label: str
    focal_length: int


@dataclass
class LensBox:
    lenses: List[Lens]
    box_num: int

    def insert_lens(self, lens):
        for i, l in enumerate(self.lenses):
            if l.label == lens.label:
                self.lenses[i] = lens
                break
        else:
            self.lenses.append(lens)

    def remove_lens(self, lens_label):
        for i, l in enumerate(self.lenses):
            if l.label == lens_label:
                del self.lenses[i]

    def focusing_power(self) -> int:
        return sum(
            self.box_num * (slot + 1) * l.focal_length
            for slot, l in enumerate(self.lenses)
        )


def parse_input(lines):
    return lines[0].split(",")


def hash_string(s) -> int:
    hash = 0

    for c in s:
        hash += ord(c)
        hash *= 17
        hash %= 256

    return hash


def part1(init_steps):
    return sum(hash_string(s) for s in init_steps)


def part2(init_steps):
    boxes: [LensBox] = []

    for i in range(256):
        boxes.append(LensBox(lenses=[], box_num=i + 1))

    for step in init_steps:
        if "=" in step:
            label, length = step.split("=")
            lens = Lens(label=label, focal_length=int(length))
        else:
            (label, _) = step.split("-")
            lens = None

        box_num = hash_string(label)

        if lens:
            boxes[box_num].insert_lens(lens)
        else:
            boxes[box_num].remove_lens(label)

    return sum(box.focusing_power() for box in boxes)
