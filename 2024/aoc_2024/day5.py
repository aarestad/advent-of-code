from collections import defaultdict
from dataclasses import dataclass
from typing import List


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


def fixed_order(po: List[int]) -> List[int]:
    return po


orderings_by_page_before = defaultdict(list)
orderings_by_page_after = defaultdict(list)

if __name__ == "__main__":
    example = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

    example_input = example.split("\n")

    with open("input/day5.txt") as input:
        problem_input = [i.strip() for i in input.readlines()]

    data = problem_input
    empty_line_idx = data.index("")
    pages = data[empty_line_idx + 1 :]

    print_orders = [[int(p) for p in l.split(",")] for l in pages]

    for po in [PageOrdering.from_str(o) for o in data[:empty_line_idx]]:
        orderings_by_page_before[po.page_before].append(po)
        orderings_by_page_after[po.page_after].append(po)

    ok_middle_page_number_sum = 0
    fixed_middle_page_number_sum = 0

    for po in print_orders:
        for idx, page in enumerate(po):
            if any(
                PageOrdering(prev_page, page) not in orderings_by_page_before[prev_page]
                for prev_page in po[:idx]
            ) or any(
                PageOrdering(page, following_page)
                not in orderings_by_page_after[following_page]
                for following_page in po[idx + 1 :]
            ):
                fixed_middle_page_number_sum += fixed_order(po)[len(po) // 2]

                break
        else:
            ok_middle_page_number_sum += po[len(po) // 2]

    print(f"ok middle page number sum: {ok_middle_page_number_sum}")
    print(f"fixed middle page number sum: {fixed_middle_page_number_sum}")
