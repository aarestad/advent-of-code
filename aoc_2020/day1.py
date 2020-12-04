from itertools import combinations
from operator import mul
from functools import reduce

if __name__ == "__main__":
    entries = []

    with open("input/day1.txt") as entry_file:
        for entry in entry_file:
            entries.append(int(entry.strip()))

    for combo in combinations(entries, 3):
        if sum(combo) == 2020:
            print(reduce(mul, combo))
