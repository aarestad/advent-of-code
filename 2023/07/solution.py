## advent of code 2023
## https://adventofcode.com/2023
## day 07

from dataclasses import dataclass
from functools import total_ordering, cached_property, reduce
from collections import Counter
from operator import mul
import enum


@total_ordering
class HandType(enum.Enum):
    UNKNOWN = 0
    HIGH_CARD = enum.auto()
    ONE_PAIR = enum.auto()
    TWO_PAIR = enum.auto()
    THREE_OF_KIND = enum.auto()
    FULL_HOUSE = enum.auto()
    FOUR_OF_KIND = enum.auto()
    FIVE_OF_KIND = enum.auto()

    def __lt__(self, other: "HandType") -> bool:
        return self.value < other.value


@total_ordering
class Card(enum.Enum):
    JOKER = (-1, "J")  # part 2
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
    # JACK = (10, "J") # part 1
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

    def __hash__(self):
        return hash(self.rank) * hash(self.label)

    def __lt__(self, other: "Card") -> bool:
        return self.rank < other.rank

    def __eq__(self, other: "Card") -> bool:
        return self.rank == other.rank


@dataclass
@total_ordering
class Hand:
    cards: [Card]
    bid: int

    @property
    def cards_str(self) -> str:
        return "".join(c.label for c in self.cards)

    @cached_property
    def hand_type(self) -> HandType:
        card_counts = Counter(self.cards)

        if len(card_counts) == 1:
            return HandType.FIVE_OF_KIND

        if len(card_counts) == 2:
            if 4 in card_counts.values():
                return HandType.FOUR_OF_KIND

            return HandType.FULL_HOUSE

        if len(card_counts) == 3:
            if 3 in card_counts.values():
                return HandType.THREE_OF_KIND

            return HandType.TWO_PAIR

        if len(card_counts) == 4:
            return HandType.ONE_PAIR

        # high card
        return HandType.HIGH_CARD

    @cached_property
    def hand_type_part_2(self) -> HandType:
        card_counts = Counter(self.cards)

        if Card.JOKER in card_counts:
            del card_counts[Card.JOKER]

        if len(card_counts) == 0 or len(card_counts) == 1:
            # 0 (5), 1 (4), 2 (3), 3 (2), 4 (1), 5 (0)
            return HandType.FIVE_OF_KIND

        non_joker_counts = sorted(card_counts.values())

        if len(card_counts) == 2:
            larger_non_joker_amt = non_joker_counts[-1]

            if larger_non_joker_amt == 4:
                # 4/1 (1)
                return HandType.FOUR_OF_KIND

            smaller_non_joker_amt = non_joker_counts[0]

            if larger_non_joker_amt == 3:
                if smaller_non_joker_amt == 1:
                    # 3/1 (1)
                    return HandType.FOUR_OF_KIND

                # 3/2 (0)
                return HandType.FULL_HOUSE

            if larger_non_joker_amt == 2:
                if smaller_non_joker_amt == 2:
                    # 2/2 (1)
                    return HandType.FULL_HOUSE

                # 2/1 (2)
                return HandType.FOUR_OF_KIND

            # 1/1 (3)
            return HandType.FOUR_OF_KIND

        if len(card_counts) == 3:
            larger_non_joker_amt = non_joker_counts[-1]

            if larger_non_joker_amt == 3:
                # 3/1/1 (0)
                return HandType.THREE_OF_KIND

            if larger_non_joker_amt == 2:
                next_smallest_non_j_amt = non_joker_counts[-2]

                if next_smallest_non_j_amt == 2:
                    # 2/2/1 (0)
                    return HandType.TWO_PAIR

                # 2/1/1 (1)
                return HandType.THREE_OF_KIND

            # 1/1/1 (2)
            return HandType.THREE_OF_KIND

        if len(card_counts) == 4:
            # 2/1/1/1 (0), 1/1/1/1 (1)
            return HandType.ONE_PAIR

        # 1/1/1/1/1 (0)
        return HandType.HIGH_CARD

    def __lt__(self, other: "Hand") -> bool:
        # part 1
        if self.hand_type_part_2 != other.hand_type_part_2:
            return self.hand_type_part_2 < other.hand_type_part_2

        # compare card _places_!
        for sc, oc in zip(self.cards, other.cards):
            if sc != oc:
                return sc < oc

        # they are equal
        return False

    def __eq__(self, other: "Hand") -> bool:
        return all(sc == oc for sc, oc in zip(self.cards, other.cards))

    def __hash__(self) -> int:
        return reduce(mul, (hash(c) for c in self.cards)) * hash(self.bid)


def parse_input(lines) -> [Hand]:
    hands = []

    for l in lines:
        hand, bid = l.split()
        hands.append(Hand([Card.card_for_label(c) for c in hand], int(bid)))

    return hands


def part1(hands):
    return sum((i + 1) * h.bid for i, h in enumerate(sorted(hands)))


def part2(hands):
    return sum((i + 1) * h.bid for i, h in enumerate(sorted(hands)))
