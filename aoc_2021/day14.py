import re

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

    current_polymer = template

    for step in range(10):
        print(f"step {step}")
        new_str_pairs = [
            current_polymer[i : i + 2] for i in range(len(current_polymer) - 1)
        ]

        for i in range(len(current_polymer) - 1):
            atom_pair = current_polymer[i : i + 2]

            if atom_pair in insertion_rules:
                new_str_pairs[i] = (
                    atom_pair[0] + insertion_rules[atom_pair] + atom_pair[1]
                )

        current_polymer = "".join(
            [new_str_pairs[0]] + [pair[1:] for pair in new_str_pairs[1:]]
        )

    char_counts: dict[str, int] = {}

    for c in current_polymer:
        if c not in char_counts:
            char_counts[c] = 1
        else:
            char_counts[c] += 1

    char_count_items = list(char_counts.items())
    char_count_items.sort(key=lambda i: i[1])
    print(char_count_items[-1][1] - char_count_items[0][1])
