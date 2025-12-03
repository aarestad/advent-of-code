present_analysis = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}

import re

parser = re.compile(r"Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)")

with open("input_16.txt") as aunts:
    for aunt in aunts:
        matched_aunt = parser.match(aunt)
        aunt_number = matched_aunt.group(1)

    current_group = 2

    found_aunt = True

    # In particular, the cats and trees readings indicates that there are greater
    # than that many (due to the unpredictable nuclear decay of cat dander and tree pollen),
    # while the pomeranians and goldfish readings indicate that there are fewer than that
    # many (due to the modial interaction of magnetoreluctance).

    while found_aunt and current_group < len(matched_aunt.groups()):
        if matched_aunt.group(current_group):
            obj = matched_aunt.group(current_group)
            obj_num = matched_aunt.group(current_group + 1)
        else:
            break

print(obj, obj_num, present_analysis[obj])

if obj == "cats" or obj == "trees":
    print(
        "checking underread: %s should be greater than %s"
        % (obj_num, present_analysis[obj])
    )

if present_analysis[obj] >= int(obj_num):
    found_aunt = False
    break
elif obj == "pomeranians" or obj == "goldfish":
    print(
        "checking overread: %s should be fewer than %s"
        % (obj_num, present_analysis[obj])
    )

if present_analysis[obj] <= int(obj_num):
    found_aunt = False
    break
else:
    print("checking normal read")

if present_analysis[obj] != int(obj_num):
    found_aunt = False
    break

current_group += 2

if found_aunt:
    print(aunt_number)
break
