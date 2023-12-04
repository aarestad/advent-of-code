"""advent of code 2023
https://adventofcode.com/2023
day 04
"""

from dataclasses import dataclass
from functools import cached_property
import re


@dataclass
class ScratchCard:
    """A scratch card instance"""

    id: int
    num_copies: int
    winning_numbers: [int]
    my_numbers: [int]

    @cached_property
    def num_winners(self):
        """Number of winning numbers on this card"""
        return len(list(n for n in self.my_numbers if n in self.winning_numbers))

    def point_value(self):
        """The point value of this card per Part 1"""
        return 2 ** (self.num_winners - 1) if self.num_winners > 0 else 0


def parse_input(lines):
    """Parse the input and return it to the test runner"""

    card_regex = re.compile(r"Card\s+(\d+):(.+)\|(.+)")

    cards = []

    for l in lines:
        card_match = card_regex.match(l)
        card_id = int(card_match[1])
        winning_numbers = [int(n) for n in card_match[2].strip().split()]
        my_numbers = [int(n) for n in card_match[3].strip().split()]
        cards.append(ScratchCard(card_id, 1, winning_numbers, my_numbers))

    return cards


def part1(cards):
    """Compute part 1 solution"""
    return sum(c.point_value() for c in cards)


def part2(cards):
    """Compute part 1 solution"""
    total_cards = 0

    for c in cards:
        for prev_card in cards[: c.id - 1]:
            if prev_card.num_winners + prev_card.id >= c.id:
                c.num_copies += prev_card.num_copies

        total_cards += c.num_copies

    return total_cards
