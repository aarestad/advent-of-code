## advent of code 2023
## https://adventofcode.com/2023
## day 08

from dataclasses import dataclass
import re
from typing import Optional
from functools import reduce
from math import gcd


@dataclass
class MapNode:
    name: str
    left_name: str
    right_name: str
    left: Optional["MapNode"]
    right: Optional["MapNode"]


def lcm(a, b):
    return abs(a * b) // gcd(a, b)


def parse_input(lines):
    instructions = lines[0]
    node_re = re.compile(r"(\w+) = \((\w+), (\w+)\)")

    nodes = {}

    for line in lines[1:]:
        if not line:
            continue

        node_match = node_re.search(line)

        nodes[node_match[1]] = MapNode(
            name=node_match[1],
            left_name=node_match[2],
            right_name=node_match[3],
            left=None,
            right=None,
        )

    for node in nodes.values():
        if node.left_name != node.name:
            node.left = nodes[node.left_name]

        if node.right_name != node.name:
            node.right = nodes[node.right_name]

    return instructions, nodes


def part1(instructions, nodes):
    current_node = nodes["AAA"]
    step_count = 0

    while current_node.name != "ZZZ":
        for inst in instructions:
            if current_node.name != "ZZZ":
                if inst == "L":
                    current_node = current_node.left
                else:
                    current_node = current_node.right

                step_count += 1

    return step_count


def part2(instructions, nodes):
    current_nodes = [n for n in nodes.values() if n.name.endswith("A")]
    loop_counts = [(0, False)] * len(current_nodes)

    while not all(c[1] for c in loop_counts):
        for inst in instructions:
            for idx, node in enumerate(current_nodes):
                if inst == "L":
                    new_node = node.left
                else:
                    new_node = node.right

                loop_count, loop_end = loop_counts[idx]

                if not loop_end:
                    loop_count += 1

                if new_node.name.endswith("Z"):
                    loop_end = True

                current_nodes[idx] = new_node
                loop_counts[idx] = (loop_count, loop_end)

    return reduce(lcm, (c[0] for c in loop_counts))
