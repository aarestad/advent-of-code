def char_score(c):
    return ord(c) - 96 if c.islower() else ord(c) - 38


if __name__ == "__main__":
    example = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

    example_input = example.split("\n")

    with open("input/day3.txt") as input:
        problem_input = [i.strip() for i in input.readlines()]

    total_score_part_1 = 0

    for line in problem_input:
        (b1, b2) = (line[0 : len(line) // 2], line[len(line) // 2 :])

        for c in b1:
            if c in b2:
                total_score_part_1 += char_score(c)
                break

    rucksacks = problem_input
    num_groups = len(rucksacks) // 3

    total_score_part_2 = 0

    for g in range(num_groups):
        first_group = rucksacks[g * 3]
        for c in first_group:
            if c in rucksacks[g * 3 + 1] and c in rucksacks[g * 3 + 2]:
                total_score_part_2 += char_score(c)
                break

    print(total_score_part_1)
    print(total_score_part_2)
