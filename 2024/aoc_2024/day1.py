from collections import Counter

if __name__ == "__main__":
    example = """3   4
4   3
2   5
1   3
3   9
3   3"""

    example_input = example.split("\n")

    with open("input/day1.txt") as input:
        problem_input = [i.strip() for i in input.readlines()]

    l1, l2 = [], []

    for l in problem_input:
        n1, n2 = l.split()
        l1.append(int(n1))
        l2.append(int(n2))

    zipped = zip(sorted(l1), sorted(l2))
    diffs = [abs(b - a) for a, b in zipped]

    print(f"part 1: {sum(diffs)}")

    l2_counter = Counter(l2)

    print(f"part 2: {sum([l * l2_counter[l] for l in l1])}")
