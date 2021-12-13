import re

if __name__ == "__main__":
    example = """London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141"""

    example_input = example.split("\n")

    with open("input_9.txt") as input:
        problem_input = [i.strip() for i in input.readlines()]

    distances: dict[str, dict[str, int]] = {}
    cities = set()

    for distance_description in example_input:
        dist_match = re.match(r"(\w+) to (\w+) = (\d+)", distance_description)

        start = dist_match[1]
        end = dist_match[2]
        distance = int(dist_match[3])

        cities.add(start)
        cities.add(end)

        if start not in distances:
            distances[start] = {}

        distances[start][end] = distance

    routes: list[(list[str], int)] = []

    for city in cities:
        other_cities = cities.copy()
        other_cities.remove(city)
