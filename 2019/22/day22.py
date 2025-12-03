import re
from typing import List

INCREMENT_RE = re.compile(r"^deal with increment (\d+)$")
NEW_STACK_RE = re.compile(r"^deal into new stack$")
CUT_RE = re.compile(r"^cut (-?\d+)$")


def increment_shuffle(deck, inc) -> List[int]:
    new_deck = [0] * len(deck)

    for i in range(len(deck)):
        new_deck[(i * inc) % len(deck)] = deck[i]

    return new_deck


if __name__ == "__main__":
    deck: List[int] = list(range(119_315_717_514_047))

    with open("22_input.txt") as command_file:
        commands = list(command_file)

    for i in range(101_741_582_076_661):
        for command in commands:
            if NEW_STACK_RE.search(command):
                deck.reverse()
            elif cut_match := CUT_RE.search(command):
                cut_point = int(cut_match.group(1))
                deck = deck[cut_point:] + deck[:cut_point]
            elif increment_match := INCREMENT_RE.search(command):
                deck = increment_shuffle(deck, int(increment_match.group(1)))
            else:
                raise RuntimeError("no match?!")

    print(deck.index(2020))
