import re
from itertools import permutations
from typing import NamedTuple

HAPPINESS_REGEX = re.compile(
    r"^(?P<guest>\w+) would (?P<dir>gain|lose) (?P<amt>\d+) happiness units by sitting next to (?P<target>\w+).\n$"
)


class HappinessAmount(NamedTuple):
    amt: int
    target: str


if __name__ == "__main__":
    amounts_by_guest = {}

    with open("input_13.txt") as happiness_lines:
        for line in happiness_lines:
            result = HAPPINESS_REGEX.search(line)

            guest = result.group("guest")

            new_amt = HappinessAmount(
                int(result.group("amt")) * (-1 if result.group("dir") == "lose" else 1),
                result.group("target"),
            )

            if guest in amounts_by_guest:
                amounts_by_guest[guest].append(new_amt)
            else:
                amounts_by_guest[guest] = [new_amt]

    best_scores = None
    best_permutation = None

    for seating_order in permutations(
        ("Alice", "Bob", "Carol", "David", "Eric", "Frank", "George", "Mallory", "me")
    ):
        scores = []

        for idx, person in enumerate(seating_order):
            person_ = amounts_by_guest.get(person, None)

            if person_:
                person_to_right = seating_order[(idx + 1) % len(seating_order)]
                person_to_right_records = list(
                    filter(lambda ha: ha.target == person_to_right, person_)
                )

                if person_to_right_records:
                    scores.append(person_to_right_records[0].amt)

                person_to_left = seating_order[idx - 1]
                person_to_left_records = list(
                    filter(lambda ha: ha.target == person_to_left, person_)
                )

                if person_to_left_records:
                    scores.append(person_to_left_records[0].amt)

        if best_scores is None or sum(scores) > sum(best_scores):
            best_scores = scores
            best_permutation = seating_order

    print(best_permutation)
    print(best_scores)
    print(sum(best_scores))
