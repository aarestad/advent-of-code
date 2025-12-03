import re

replacement_map = {}

replacement_pattern = re.compile(r"(\w+) => (\w+)")

with open("input_19.txt") as replacements:
    for r in replacements:
        r = r.strip()

        if "=>" in r:
            match = replacement_pattern.match(r)
            target = match.group(1)
            replacement = match.group(2)

            if target in replacement_map:
                replacement_map[target].append(replacement)
            else:
                replacement_map[target] = [replacement]

        elif len(r) > 0:
            target_string = r

print(replacement_map)

starting_molecule = "e"
