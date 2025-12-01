import re

LEFT = re.compile(r"L(\d+)")
RIGHT = re.compile(r"R(\d+)")

def part_1_and_2(rotations):
    pos = 50
    num_zeros = 0
    num_clicks = 0

    for r in rotations:
        print(r)
        if m := LEFT.search(r):
            distance = int(m.group(1))
            new_pos = (pos - distance) % 100
            clicks = distance // 100

            if pos != 0 and (new_pos > pos or new_pos == 0):
                clicks += 1

            print(f"{clicks} clicks")
            num_clicks += clicks
        elif m := RIGHT.search(r):
            distance = int(m.group(1))
            new_pos = (pos + distance) % 100
            clicks = distance // 100

            if pos != 0 and (new_pos < pos or new_pos == 0):
                clicks += 1

            print(f"{clicks} clicks")
            num_clicks += clicks
        else:
            raise RuntimeError(f"bad rotation: {r}")
        print(f"old->new:{pos}->{new_pos}")

        if new_pos == 0:
            num_zeros += 1

        pos = new_pos

    return num_zeros, num_clicks

if __name__ == "__main__":
    example = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""

    example_input = example.split("\n")

    print(f"example: zeroes and clicks={part_1_and_2(example_input)}")


    with open("input/day1.txt") as input:
        problem_input = [i.strip() for i in input.readlines()]

        print(f"input: zeroes and clicks={part_1_and_2(problem_input)}")


