import re
import collections

if __name__ == "__main__":
    example = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""

    example_input = example.split("\n")

    with open("input/day14.txt") as input:
        problem_input = [i.strip() for i in input.readlines()]

    template = problem_input[0]

    insertion_rules: dict[str, str] = {}

    for insertion_rule in problem_input[2:]:
        rule_match = re.match(r"(\w\w) -> (\w)", insertion_rule)
        insertion_rules[rule_match[1]] = rule_match[2]

    current_polymer: dict[str, int] = collections.defaultdict(int)

    for i in range(len(template) - 1):
        current_polymer[template[i : i + 2]] += 1

    for step in range(40):
        new_polymer: dict[str, int] = collections.defaultdict(int)

        # for i in range(len(current_polymer) - 1):
        for atom_pair, count in current_polymer.items():
            if atom_pair in insertion_rules:
                new_atom = insertion_rules[atom_pair]
                new_polymer[atom_pair[0] + new_atom] += count
                new_polymer[new_atom + atom_pair[1]] += count
            else:
                new_polymer[atom_pair] += count

        current_polymer = new_polymer

    char_counts: dict[str, int] = collections.defaultdict(int)

    for atom_pair, count in current_polymer.items():
        char_counts[atom_pair[0]] += count
        char_counts[atom_pair[1]] += count

    # Correct for double-counting
    # First, ensure the first and last character are "correctly" double-counted
    char_counts[template[0]] += 1
    char_counts[template[-1]] += 1

    # Then halve the counts for each char
    for atom in char_counts:
        char_counts[atom] //= 2

    char_count_items: list[(str, int)] = list(char_counts.items())
    char_count_items.sort(key=lambda i: i[1])
    print(char_count_items[-1][1] - char_count_items[0][1])
