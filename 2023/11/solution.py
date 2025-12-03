## advent of code 2023
## https://adventofcode.com/2023
## day 11


def parse_input(lines):
    star_map = []

    for l in lines:
        if not l:
            continue

        split_line = [c for c in l]
        star_map.append(split_line)

    return star_map


def manhattan_distance(p1, p2) -> int:
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def star_distances_with_expansion(star_map, expansion):
    empty_rows = []
    empty_cols = []

    for r, row in enumerate(star_map):
        if all(c == "." for c in row):
            empty_rows.append(r)

    for col in range(len(star_map[0])):
        column = "".join(row[col] for row in star_map)

        if all(c == "." for c in column):
            empty_cols.append(col)

    star_locs = []

    for orig_r, row in enumerate(star_map):
        for orig_c, col in enumerate(row):
            if col == "#":
                empty_rows_above = sum(1 for er in empty_rows if er < orig_r)
                empty_cols_left = sum(1 for ec in empty_cols if ec < orig_c)

                star_locs.append(
                    (
                        orig_r + expansion * empty_rows_above,
                        orig_c + expansion * empty_cols_left,
                    )
                )

    total_distance = 0

    while star_locs:
        star1 = star_locs.pop()

        for star2 in star_locs:
            total_distance += manhattan_distance(star1, star2)

    return total_distance


def part1(star_map):
    return star_distances_with_expansion(star_map, 1)


def part2(star_map):
    return star_distances_with_expansion(star_map, 999_999)
