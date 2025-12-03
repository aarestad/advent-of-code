from itertools import combinations

def part1(input):
    joltage = 0

    for line in input:
        joltage += best_joltage_for(line, 2)

    return joltage

def part2(input):
    joltage = 0

    for line in input:
        print(f"calculating for line {line}")
        # lol no - for 100-battery lines, this is 1,050,421,051,106,700 iterations
        joltage += best_joltage_for(line, 12)

    return joltage

def best_joltage_for(line, num_batteries):
    best = 0

    for j in combinations(line, num_batteries):
        joltage = int(''.join(j))

        if joltage > best:
            best = joltage

    return best

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
