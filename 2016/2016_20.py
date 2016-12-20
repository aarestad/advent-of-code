with open('input_20.txt') as range_file:
    ranges = [l.strip() for l in range_file.readlines()]

def merge_range(new_range, ranges):
    for r in ranges:
        if r[1]
