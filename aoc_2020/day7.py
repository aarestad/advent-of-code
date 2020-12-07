import re

bag_rules = {}


def bag_can_contain_shiny_gold(bag):
    return any(
        c[1] == "shiny gold" or bag_can_contain_shiny_gold(c[1]) for c in bag_rules[bag]
    )


def format_bags(bag, indent=0):
    contains = bag_rules[bag]

    return (
        f'{"|" * (indent-1)} nothing\n'
        if len(contains) == 0
        else "".join(
            f'{"|" * indent}{c[0]} {c[1]}:\n' + format_bags(c[1], indent + 1)
            for c in contains
        )
    )


def count_containing_bags(bag):
    return sum(int(c[0]) * (1 + count_containing_bags(c[1])) for c in bag_rules[bag])


if __name__ == "__main__":
    with open("input/day7.txt") as bag_rule_file:
        for rule in bag_rule_file:
            (bag_name, bag_contents) = rule.strip().split(" bags contain ")
            elements = bag_contents.strip(".").split(", ")

            try:
                bag_content_elements = [
                    re.match(r"(\d+) ([\w\s]+) bag", c).groups() for c in elements
                ]
            except AttributeError:  # "no other bags"
                bag_content_elements = []

            bag_rules[bag_name] = bag_content_elements

    print(format_bags("shiny gold"))
    print(sum(1 for bag in bag_rules.keys() if bag_can_contain_shiny_gold(bag)))
    print(count_containing_bags("shiny gold"))
