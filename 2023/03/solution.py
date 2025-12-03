## advent of code 2023
## https://adventofcode.com/2023
## day 03

from operator import mul


def parse_input(lines):
    parsed_lines = []

    for l in lines:
        parsed_lines.append([c for c in l])

    return parsed_lines


def part1(lines):
    part_number_sum = 0

    for line_num, l in enumerate(lines):
        current_num = ""
        current_num_start = -1

        for i, c in enumerate(l):
            if c.isdigit():
                if current_num == "":
                    current_num_start = i
                current_num += c
                continue

            if len(current_num):
                # not a digit, and we have a nonzero-length current_num - check for a "symbol"
                num_len = len(current_num)

                check_start = max(current_num_start - 1, 0)
                check_end = min(current_num_start + num_len + 1, len(l))

                chars_above = (
                    lines[line_num - 1][check_start:check_end] if line_num > 0 else ""
                )
                symbol_above = any(not c.isdigit() and c != "." for c in chars_above)

                left_idx = current_num_start - 1
                left = l[left_idx] if left_idx > 0 else "."
                symbol_left = not left.isdigit() and left != "."

                right_idx = current_num_start + num_len
                right = l[right_idx] if right_idx < len(l) else "."
                symbol_right = not right.isdigit() and right != "."

                chars_below = (
                    lines[line_num + 1][check_start:check_end]
                    if line_num < len(lines) - 1
                    else ""
                )
                symbol_below = any(not c.isdigit() and c != "." for c in chars_below)

                if symbol_above or symbol_left or symbol_right or symbol_below:
                    part_number_sum += int(current_num)

                current_num = ""

        if len(current_num):
            # number at the end of the line
            num_len = len(current_num)

            check_start = max(current_num_start - 1, 0)
            check_end = min(current_num_start + num_len + 1, len(l))

            chars_above = (
                lines[line_num - 1][check_start:check_end] if line_num > 0 else ""
            )
            symbol_above = any(not c.isdigit() and c != "." for c in chars_above)

            left_idx = current_num_start - 1
            left = l[left_idx] if left_idx > 0 else "."
            symbol_left = not left.isdigit() and left != "."

            right_idx = current_num_start + num_len
            right = l[right_idx] if right_idx < len(l) else "."
            symbol_right = not right.isdigit() and right != "."

            chars_below = (
                lines[line_num + 1][check_start:check_end]
                if line_num < len(lines) - 1
                else ""
            )
            symbol_below = any(not c.isdigit() and c != "." for c in chars_below)

            if symbol_above or symbol_left or symbol_right or symbol_below:
                part_number_sum += int(current_num)

    return part_number_sum


def part2(lines):
    numbers_near_gears = dict()

    for r in range(len(lines)):
        for c in range(len(lines[r])):
            if lines[r][c] == "*":
                numbers_near_gears[(r, c)] = []

    for line_num, l in enumerate(lines):
        current_num = ""
        current_num_start = -1

        for i, c in enumerate(l):
            if c.isdigit():
                if current_num == "":
                    current_num_start = i
                current_num += c
                continue

            if len(current_num):
                # not a digit, and we have a nonzero-length current_num - check for a "symbol"
                num_len = len(current_num)

                possible_gear_locs = []

                check_start = max(current_num_start - 1, 0)
                check_end = min(current_num_start + num_len + 1, len(l))

                for col in range(check_start, check_end):
                    possible_gear_locs.append((line_num - 1, col))

                possible_gear_locs.append((line_num, current_num_start - 1))

                possible_gear_locs.append((line_num, current_num_start + num_len))

                for col in range(check_start, check_end):
                    possible_gear_locs.append((line_num + 1, col))

                for gear in numbers_near_gears:
                    if gear in possible_gear_locs:
                        numbers_near_gears[gear].append(int(current_num))

                current_num = ""

        if len(current_num):
            # number at the end of the line
            num_len = len(current_num)

            possible_gear_locs = []

            check_start = max(current_num_start - 1, 0)
            check_end = min(current_num_start + num_len + 1, len(l))

            for col in range(check_start, check_end):
                possible_gear_locs.append((line_num - 1, col))

            possible_gear_locs.append((line_num, current_num_start - 1))

            possible_gear_locs.append((line_num, current_num_start + num_len))

            for col in range(check_start, check_end):
                possible_gear_locs.append((line_num + 1, col))

            for gear in numbers_near_gears:
                if gear in possible_gear_locs:
                    numbers_near_gears[gear].append(int(current_num))

    gear_ratio_sum = 0

    for gear, nums in numbers_near_gears.items():
        if len(nums) == 2:
            gear_ratio_sum += mul(*nums)

    return gear_ratio_sum
