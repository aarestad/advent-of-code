import collections

if __name__ == "__main__":
    example = """bvwbjplbgvbhsrlpgdmjqwftvncz"""

    example_input = example.split("\n")

    with open("input/day6.txt") as input:
        problem_input = [i.strip() for i in input.readlines()]

    message = problem_input[0]

    for i in range(0, len(message) - 4):
        packet = message[i : i + 4]
        char_counts = collections.Counter(packet)
        if len(char_counts) == 4:  # four unique chars
            print(i + 4)
            break

    for i in range(0, len(message) - 14):
        packet = message[i : i + 14]
        char_counts = collections.Counter(packet)
        if len(char_counts) == 14:  # 14 unique chars
            print(i + 14)
            break
    else:
        print("no message?")
