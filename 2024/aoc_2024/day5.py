from collections import defaultdict
from dataclasses import dataclass
from typing import List
from itertools import groupby


@dataclass(frozen=True)
class PageOrdering:
    page_before: int
    page_after: int

    @staticmethod
    def from_str(s: str) -> "PageOrdering":
        parts = s.split("|")
        before = int(parts[0])
        after = int(parts[1])
        return PageOrdering(before, after)


orderings_by_page_before: defaultdict[int, List[PageOrdering]] = defaultdict(list)
orderings_by_page_after: defaultdict[int, List[PageOrdering]] = defaultdict(list)


def any_prev_page_bad(print_order: List[int]) -> bool:
    return any(
        PageOrdering(prev_page, page) not in orderings_by_page_before[prev_page]
        for prev_page in print_order[:idx]
    )


def any_following_page_bad(print_order: List[int]) -> bool:
    return any(
        PageOrdering(prev_page, page) not in orderings_by_page_before[prev_page]
        for prev_page in print_order[:idx]
    )


def fixed_order(print_order: List[int]) -> List[int]:
    correct_order = [0] * len(print_order)

    for page in print_order:
        correct_order[
            len(
                [
                    o
                    for o in orderings_by_page_after[page]
                    if o.page_before in print_order
                ]
            )
        ] = page

    return correct_order


if __name__ == "__main__":
    with open("input/day5.txt") as input:
        problem_input = [i.strip() for i in input.readlines()]

    empty_line_idx = problem_input.index("")

    page_orderings = [PageOrdering.from_str(o) for o in problem_input[:empty_line_idx]]

    print_orders = [
        [int(p) for p in l.split(",")] for l in problem_input[empty_line_idx + 1 :]
    ]

    for p, orderings in groupby(
        sorted(page_orderings, key=lambda po: po.page_before), lambda po: po.page_before
    ):
        orderings_by_page_before[p] = list(orderings)

    for p, orderings in groupby(
        sorted(page_orderings, key=lambda po: po.page_after), lambda po: po.page_after
    ):
        orderings_by_page_after[p] = list(orderings)

    ok_middle_page_number_sum = 0
    fixed_middle_page_number_sum = 0

    for po in print_orders:
        for idx, page in enumerate(po):
            if any_prev_page_bad(po) or any_following_page_bad(po):
                fixed_middle_page_number_sum += fixed_order(po)[len(po) // 2]
                break
        else:
            ok_middle_page_number_sum += po[len(po) // 2]

    print(f"ok middle page number sum: {ok_middle_page_number_sum}")
    print(f"fixed middle page number sum: {fixed_middle_page_number_sum}")
