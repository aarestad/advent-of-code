import re

with open("input_5.txt") as nice_or_naughty_strings:
    nice_string_count = 0
    for line in nice_or_naughty_strings:
        line = line.strip()
        if (
            re.search("[aeiou].*[aeiou].*[aeiou]", line)
            and re.search("(.)\\1", line)
            and not (
                re.search("ab", line)
                or re.search("cd", line)
                or re.search("pq", line)
                or re.search("xy", line)
            )
        ):
            nice_string_count += 1
        else:
            print("naughty line:", line)

    print(nice_string_count)
