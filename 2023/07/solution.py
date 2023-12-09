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

    def __hash__(self):
        return hash(self.rank) * hash(self.label)

    def __lt__(self, other: "Card") -> bool:
        return self.rank < other.rank

    def __eq__(self, other: "Card") -> bool:
        return self.rank == other.rank


@dataclass
@total_ordering
class Hand:
    raw_hand: str
    cards: [Card]
    bid: int

    @property
    def cards_str(self) -> str:
        return "".join(c.label for c in self.cards)

    @cached_property
    def hand_type(self) -> (HandType, [Card]):
        card_counts = Counter(self.cards)

        if len(card_counts) == 1:
            return HandType.FIVE_OF_KIND, self.cards[0:1]

        if len(card_counts) == 2:
            # four of a kind or full house
            if 4 in card_counts.values():
                four_of_kind_card = [c for c, n in card_counts.items() if n == 4]
                single_card = [c for c, n in card_counts.items() if n == 1]
                return HandType.FOUR_OF_KIND, four_of_kind_card + single_card

            three_of_kind_card = [c for c, n in card_counts.items() if n == 3]
            pair_card = [c for c, n in card_counts.items() if n == 2]
            return HandType.FULL_HOUSE, three_of_kind_card + pair_card

        if len(card_counts) == 3:
            if 3 in card_counts.values():
                three_of_kind_card = [c for c, n in card_counts.items() if n == 3]
                single_cards = sorted(
                    [c for c, n in card_counts.items() if n == 1], reverse=True
                )
                return HandType.THREE_OF_KIND, three_of_kind_card + single_cards

            pair_cards = sorted(
                [c for c, n in card_counts.items() if n == 2], reverse=True
            )

            single_card = [c for c, n in card_counts.items() if n == 1]

            return HandType.TWO_PAIR, pair_cards + single_card

        if len(card_counts) == 4:
            pair_cards = sorted(
                [c for c, n in card_counts.items() if n == 2], reverse=True
            )

            single_cards = sorted(
                [c for c, n in card_counts.items() if n == 1], reverse=True
            )

            return HandType.ONE_PAIR, pair_cards + single_cards

        # high card
        return HandType.HIGH_CARD, sorted(self.cards, reverse=True)

    def __lt__(self, other: "Hand") -> bool:
        sht = self.hand_type
        oht = other.hand_type

        if sht[0] != oht[0]:
            return sht[0] < oht[0]

        # compare card _places_!
        for sc, oc in zip(self.cards, other.cards):
            if sc != oc:
                return sc < oc

        # for sc, oc in zip(sht[1], oht[1]):
        #     if sc != oc:
        #         return sc < oc

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
        hands.append(Hand(hand, [Card.card_for_label(c) for c in hand], int(bid)))

    return hands


def part1(hands):
    sorted_hands = sorted(hands)

    total_winnings = 0

    print("\t".join(["cards", "bid", "rank", "win", "total"]))
    for i, h in enumerate(sorted_hands):
        winnings = (i + 1) * h.bid
        total_winnings += winnings
        print(
            "\t".join(
                [
                    "".join(c.label for c in h.cards),
                    str(h.bid),
                    str(i + 1),
                    str(winnings),
                    str(total_winnings),
                ]
            )
        )
    return sum((i + 1) * h.bid for i, h in enumerate(sorted_hands))


def part2(hands):
    pass
