## advent of code 2023
## https://adventofcode.com/2023
## day 04

from dataclasses import dataclass
import re


@dataclass
class ScratchCard:
    id: int
    winning_numbers: [int]
    my_numbers: [int]

    def num_winners(self):
        return len(list(n for n in self.my_numbers if n in self.winning_numbers))

    def point_value(self):
        num_winners = self.num_winners()
        return 2 ** (num_winners - 1) if num_winners > 0 else 0


def parse_input(lines):
    # Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
    CARD_REGEX = re.compile(r"Card\s+(\d+):(.+)\|(.+)")

    cards = []

    for l in lines:
        card_match = CARD_REGEX.match(l)
        id = int(card_match[1])
        winning_numbers = [int(n) for n in card_match[2].strip().split()]
        my_numbers = [int(n) for n in card_match[3].strip().split()]
        cards.append(ScratchCard(id, winning_numbers, my_numbers))

    return cards


def part1(cards):
    return sum(c.point_value() for c in cards)


def part2(cards):
    won_card_ids = []
    cards = list(cards)

    total_cards = len(cards)

    for c in cards:
        num_winners = c.num_winners()
        won_card_ids.extend([n for n in range(c.id + 1, c.id + num_winners + 1)])

    # this is really stupid inefficient, but it completes in a few seconds at least :)
    while won_card_ids:
        total_cards += len(won_card_ids)
        new_won_card_ids = []

        for card_id in won_card_ids:
            c = cards[card_id - 1]
            num_winners = c.num_winners()

            new_won_card_ids.extend(
                [n for n in range(c.id + 1, c.id + num_winners + 1)]
            )

        won_card_ids = new_won_card_ids

    print(total_cards)
    return total_cards
