import re

if __name__ == "__main__":
    example = """123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i
"""

    example_input = example.split("\n")

    with open("input_7.txt") as input:
        problem_input = [i.strip() for i in input.readlines()]

    wires = problem_input[:]
    values = {'b': 3176}

    while len(wires):
        skipped_wires = []

        for wire in wires:
            if not wire:
                continue

            if m := re.match(r"(\w+) -> (\w+)", wire):
                arg1 = m[1]
                dest = m[2]
                operation = "PASS"
            elif m := re.match(r"NOT (\w+) -> (\w+)", wire):
                arg1 = m[1]
                dest = m[2]
                operation = "NOT"
            elif m := re.match(r"(\w+) (\w+) (\w+) -> (\w+)", wire):
                arg1 = m[1]
                arg2 = m[3]
                dest = m[4]
                operation = m[2]
            else:
                raise ValueError(f"unrecognized connection: {wire}")

            if dest == 'b':  # b is hard-wired for part 2
                continue

            match operation:
                case "PASS":
                    if arg1.isdigit():
                        values[dest] = int(arg1)
                    elif arg1 in values:
                        values[dest] = values[arg1]
                    else:
                        skipped_wires.append(wire)
                case "AND":
                    if arg1.isdigit() and arg2 in values:
                        values[dest] = int(arg1) & values[arg2]
                    elif arg1 in values and arg2 in values:
                        values[dest] = values[arg1] & values[arg2]
                    else:
                        skipped_wires.append(wire)
                case "OR":
                    if arg1 in values and arg2 in values:
                        values[dest] = values[arg1] | values[arg2]
                    else:
                        skipped_wires.append(wire)
                case "NOT":
                    if arg1 in values:
                        values[dest] = 65535 & ~values[arg1]
                    else:
                        skipped_wires.append(wire)
                case "LSHIFT":
                    if arg1 in values:
                        values[dest] = 65535 & (values[arg1] << int(arg2))
                    else:
                        skipped_wires.append(wire)
                case "RSHIFT":
                    if arg1 in values:
                        values[dest] = 65535 & (values[arg1] >> int(arg2))
                    else:
                        skipped_wires.append(wire)
                case _:
                    raise ValueError(f"unrecognized operation: {operation}")

        wires = skipped_wires

    print(values)
    print(values.get("a"))
