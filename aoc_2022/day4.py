import re

if __name__ == "__main__":
    example = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""

    example_input = example.split("\n")

    with open("input/day4.txt") as input:
        problem_input = [i.strip() for i in input.readlines()]

    pair_matcher = re.compile(r"(\d+)-(\d+)")

    num_contained = 0
    num_overlap = 0

    for line in problem_input:
        (pair_1_txt, pair_2_txt) = line.split(",")
        pair_1_match = pair_matcher.search(pair_1_txt)
        pair_1 = (int(pair_1_match.group(1)), int(pair_1_match.group(2)))
        pair_2_match = pair_matcher.search(pair_2_txt)
        pair_2 = (int(pair_2_match.group(1)), int(pair_2_match.group(2)))

        if (pair_1[0] >= pair_2[0] and pair_1[1] <= pair_2[1]) or (
            pair_2[0] >= pair_1[0] and pair_2[1] <= pair_1[1]
        ):
            num_contained += 1

        if pair_1[0] <= pair_2[1] and pair_2[0] <= pair_1[1]:
            print(f"{line} overlaps")
            num_overlap += 1

    print(num_contained)
    print(num_overlap)
