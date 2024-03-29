import re
import itertools


def find_paths_part_1(
    connections: list[(str, str)], path: list[str]
) -> list[list[str]]:
    new_paths = []

    possible_connections = [c for c in connections if path[-1] in c]

    for connection in possible_connections:
        next_node = connection[0] if connection[1] == path[-1] else connection[1]

        if next_node == "start":
            continue
        elif next_node == "end":
            new_paths.append(path + ["end"])
        elif not next_node.islower() or next_node not in path:
            new_paths.extend(find_paths_part_1(connections, path + [next_node]))

    return new_paths


def find_paths_part_2(
    connections: list[(str, str)], path: list[str]
) -> list[list[str]]:
    new_paths = []

    possible_connections = [c for c in connections if path[-1] in c]

    for connection in possible_connections:
        next_node = connection[0] if connection[1] == path[-1] else connection[1]

        if next_node == "start":
            continue
        elif next_node == "end":
            new_paths.append(path + ["end"])
        else:
            new_path = path + [next_node]
            sorted_path = sorted(new_path)

            small_cave_visited_twice = False

            for node, occurrences in itertools.groupby(sorted_path):
                if node.islower():
                    o_count = sum(1 for _ in occurrences)

                    if o_count == 2 and not small_cave_visited_twice:
                        small_cave_visited_twice = True
                    elif o_count > 1:
                        break
            else:
                new_paths.extend(find_paths_part_2(connections, new_path))

    return new_paths


if __name__ == "__main__":
    ex1 = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""

    ex1_input = ex1.split("\n")

    with open("input/day12.txt") as input:
        problem_input = [i.strip() for i in input.readlines()]

    connections = []

    for line in problem_input:
        connection = re.match(r"(\w+)-(\w+)", line)
        connections.append((connection[1], connection[2]))

    print(len(find_paths_part_1(connections, ["start"])))
    print(len(find_paths_part_2(connections, ["start"])))
