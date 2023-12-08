## advent of code 2023
## https://adventofcode.com/2023
## day 07

from dataclasses import dataclass
from functools import total_ordering, cached_property
from collections import Counter
import enum


class HandTypeEnum(enum.Enum):
    UNKNOWN = 0
    HIGH_CARD = enum.auto()
    ONE_PAIR = enum.auto()
    TWO_PAIR = enum.auto()
    THREE_OF_KIND = enum.auto()
    FULL_HOUSE = enum.auto()
    FOUR_OF_KIND = enum.auto()
    FIVE_OF_KIND = enum.auto()


class Card(enum.Enum):
    UNKNOWN = (0, "?")
    TWO = (1, "2")
    THREE = (2, "3")
    FOUR = (3, "4")
    FIVE = (4, "5")
    SIX = (5, "6")
    SEVEN = (6, "7")
    EIGHT = (7, "8")
    NINE = (8, "9")
    TEN = (9, "T")
    JACK = (10, "J")
    QUEEN = (11, "Q")
    KING = (12, "K")
    ACE = (13, "A")

    def __init__(self, rank, label):
        self.rank = rank
        self.label = label

    @classmethod
    def card_for_label(cls, label) -> "Card":
        for e in cls:
            if e.label == label:
                return e

        return Card.UNKNOWN


@dataclass
@total_ordering
class Hand:
    cards: [Card]
    bid: int

    @cached_property
    def hand_type(self) -> HandTypeEnum:
        card_counts = Counter(self.cards)
        print(card_counts)
        return HandTypeEnum.UNKNOWN

    def __lt__(self, other: "Hand") -> bool:
        return self.hand_type < other.hand_type

    def __eq__(self, other: "Hand") -> bool:
        return self.hand_type == other.hand_type


def parse_input(lines) -> [Hand]:
    hands = []

    for l in lines:
        hand, bid = l.split()
        hands.append(Hand([Card.card_for_label(c) for c in hand], int(bid)))

    return hands


def part1(hands):
    print(hands[0].hand_type)


def part2(hands):
    pass
