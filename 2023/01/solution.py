## advent of code 2023
## https://adventofcode.com/2023
## day 01

words_to_numbers = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def parse_input(lines):
    calibration_values = []

    for line in lines:
        print(line + ":")
        first_digit = None
        most_recent_digit = None

        i = 0
        while i < len(line):
            num = None

            for w in words_to_numbers:
                if line[i:].startswith(w):
                    num = words_to_numbers[w]
                    break
            else:
                if line[i].isdigit():
                    num = line[i]

            i += 1

            if num is None:
                continue

            if first_digit is None:
                first_digit = num

            most_recent_digit = num
            print(f"i={i-1}, num={num}", end=None)

        val = int(first_digit + most_recent_digit)
        print(val)
        print()
        calibration_values.append(val)

    return calibration_values


def part1(data):
    return sum(data)


def part2(data):
    return sum(data)
