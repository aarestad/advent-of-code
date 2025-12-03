from itertools import combinations


def part1(input):
    joltage = 0

    for line in input:
        joltage += best_joltage_4(line, 2)

    return joltage


def part2(input):
    joltage = 0

    for line in input:
        print(f"calculating for line {line}")
        joltage += best_joltage_4(line, 12)

    return joltage


# part 2: lolno, 100c12 = 1,050,421,051,106,700
def best_joltage_for(line, num_batteries):
    best = 0

    for j in combinations(line, num_batteries):
        joltage = int("".join(j))

        if joltage > best:
            best = joltage

    return best


def best_joltage_4(line, num_batteries):
    indices = []

    start_at = 0

    for i in range(num_batteries):
        next_best = (
            best_battery_remaining(line[start_at:], num_batteries - i - 1) + start_at
        )
        indices.append(next_best)
        start_at = next_best + 1

    return int("".join(line[ix] for ix in indices))


def best_battery_remaining(line, num_batteries_remaining):
    best_idx = -1
    best_val = 0
    substr = line[: len(line) - num_batteries_remaining]

    for idx, b in enumerate(substr):
        val = int(b)

        if val == 9:
            return idx

        if val > best_val:
            best_val = val
            best_idx = idx

    return best_idx


if __name__ == "__main__":
    example = """987654321111111
811111111111119
234234234234278
818181911112111"""

    example_input = example.split("\n")

    print(f"example part 1: {part1(example_input)}")
    print(f"example part 2: {part2(example_input)}")

    with open("input/day3.txt") as input:
        problem_input = [i.strip() for i in input.readlines()]

        print(f"part 1: {part1(problem_input)}")
        print(f"part 2: {part2(problem_input)}")
