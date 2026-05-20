import re
from dataclasses import dataclass
from typing import Optional, List


@dataclass
class Disc:
    name: str
    weight: int
    parent: Optional[str]
    children: List[str]

    PARSER = re.compile(r"^(?P<name>\w+)\s+\((?P<weight>\d+)\)(?:\s+->\s+(?P<children>.*))?$")

    @classmethod
    def from_str(cls, s: str) -> 'Disc':
        m = cls.PARSER.match(s)
        if not m:
            raise ValueError(f"Invalid disc format: {s}")

        children = m.group("children")

        return cls(
            name=m.group("name"),
            weight=int(m.group("weight")),
            children=children.split(r', ') if children else [],
            parent=None
        )

    def __str__(self):
        return f"Disc({self.name} weight={self.weight} children={','.join(self.children)})"

DISCS_BY_NAME: dict[str, Disc] = {}

def weight_of_subtree(d: Disc):
    if len(d.children) == 0:
        return d.weight

    return d.weight + sum(weight_of_subtree(DISCS_BY_NAME[child]) for child in d.children)

if __name__ == "__main__":
    example = """pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)"""

    example_input = example.split("\n")

    with open("input/day7.txt") as input:
        problem_input = [i.strip() for i in input.readlines()]

        discs = [Disc.from_str(s) for s in problem_input]

        for i, d in enumerate(discs):
            DISCS_BY_NAME[d.name] = d

            for od in discs:
                if od.name in d.children:
                    od.parent = d.name

        root: Disc = None

        for d in discs:
            if d.parent is None:
                print(f"root is {d.name}")
                root = d
                break

        for d in DISCS_BY_NAME['apjxafk'].children:
            print(f"weight of apjxafk: {DISCS_BY_NAME['apjxafk'].weight} total subtree: subtree {d}: {weight_of_subtree(DISCS_BY_NAME[d])}")



