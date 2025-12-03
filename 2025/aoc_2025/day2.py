from typing import List

def part_1(ranges: List[str]):
    invalid_ids = []

    for r in ranges:
        start, end = (int(n) for n in r.split("-"))

        for id in range(start, end+1):
            id_str = str(id)
            id_length = len(id_str)

            if id_length % 2 == 0 and has_repeated_substring_of_length(id_str, id_length//2):
                invalid_ids.append(id)

    return invalid_ids

def part_2(ranges: List[str]):
    invalid_ids = []

    for r in ranges:
        start, end = (int(n) for n in r.split("-"))

        for id in range(start, end+1):
            id_str = str(id)
            id_length = len(id_str)

            for lgth in range(1, id_length//2 + 1):
                if id_length % lgth == 0 and has_repeated_substring_of_length(id_str, lgth):
                    invalid_ids.append(id)
                    break

    return invalid_ids


def has_repeated_substring_of_length(str, lgth):
    start = 0
    while start < len(str):
        substr = str[start:start+lgth]

        needle = start + lgth

        while needle < len(str):
            if substr != str[needle:needle+lgth]:
                return False

            needle += lgth

        start += lgth

    return True

if __name__ == "__main__":
    example = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""

    example_repeats = part_1(example.split(","))
    print(f"example repeats: {example_repeats}")
    print(f"example sum: {sum(example_repeats)}")

    example_repeats_2 = part_2(example.split(","))
    print(f"part 2 example repeats: {example_repeats_2}")
    print(f"part 2 example sum: {sum(example_repeats_2)}")

    with open("input/day2.txt") as input:
        problem_input = [i.strip() for i in input.readlines()][0]

        part_1_repeats = part_1(problem_input.split(","))
        print(f"{part_1_repeats} ids in input")
        print(f"part 1 sum: {sum(part_1_repeats)}")

        part_2_repeats = part_2(problem_input.split(","))
        print(f"part 2 sum: {sum(part_2_repeats)}")

