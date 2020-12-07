import re

bag_rules = {}


def bag_can_contain_shiny_gold(bag):
    contains = bag_rules[bag]

    if len(contains) == 0:
        return False

    return any(c[1] == 'shiny gold' or bag_can_contain_shiny_gold(c[1]) for c in contains)


def format_bags(bag, indent=0):
    contains = bag_rules[bag]

    if len(contains) == 0:
        return f'{" " * (indent + 1)}nothing\n'

    return ''.join(f'{" " * indent}{c[0]} {c[1]}:\n' + format_bags(c[1], indent+1) for c in contains)


def count_containing_bags(bag):
    contains = bag_rules[bag]

    if len(contains) == 0:
        return 0

    return sum(int(c[0]) * (1 + count_containing_bags(c[1])) for c in contains)


if __name__ == "__main__":
    with open('input/day7.txt') as bag_rule_file:
        for rule in bag_rule_file:
            (bag_name, bag_contents) = rule.strip().split(' bags contain ')
            elements = bag_contents.strip('.').split(', ')

            try:
                bag_content_elements = [re.match(r'(\d+) ([\w\s]+) bag', c).groups() for c in elements]
            except AttributeError:  # "no other bags"
                bag_content_elements = []

            if bag_name in bag_rules:
                raise ValueError(f'duplicate rule for {bag_name}')

            bag_rules[bag_name] = bag_content_elements

    good_bags = 0

    for bag in bag_rules.keys():
        if bag_can_contain_shiny_gold(bag):
            good_bags += 1

    print(format_bags('shiny gold'))
    print(good_bags)
    print(count_containing_bags('shiny gold'))
