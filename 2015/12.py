import json


def parse_as_dict(d):
    for v in d.values():
        # reject dict if it has a 'red' value
        if v == "red":
            return
    for v in d.values():
        parse_object(v)


total_sum = 0


def parse_object(o):
    global total_sum

    if isinstance(o, dict):
        parse_as_dict(o)
    elif isinstance(o, list):
        for e in o:
            parse_object(e)
    elif isinstance(o, int):
        total_sum += o


parse_object(json.load(open("input_12.json")))

print(total_sum)

# with open('input_12.json') as input_file:
# 	json_in = input_file.readline()
#
# import re
# int_strings = re.finditer(r'-?[0-9]+', json_in)
#
# total_sum = 0
#
# for s in int_strings:
# 	total_sum += int(s.group(0))
#
# print total_sum
