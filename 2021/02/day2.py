import re

vertical_pos = 0
horiz_pos = 0
aim_val = 0

with open("input/day2.txt") as instructions:
    for instruction in instructions:
        inst_match = re.match(r"(\w+)\s+(\d+)", instruction)

        inst = inst_match.group(1)
        amount = int(inst_match.group(2))

        if inst == "forward":
            horiz_pos += amount
            vertical_pos += aim_val * amount
        elif inst == "up":
            aim_val -= amount
        elif inst == "down":
            aim_val += amount

print(vertical_pos * horiz_pos)
