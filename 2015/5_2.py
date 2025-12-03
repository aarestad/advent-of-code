import re

with open("input_5.txt") as input:
    nice_string_count = 0
    for line in input:
        if re.search("(..).*\\1", line) and re.search("(.).\\1", line):
            nice_string_count += 1
        else:
            print("naughty line:", line)

    print(nice_string_count)
