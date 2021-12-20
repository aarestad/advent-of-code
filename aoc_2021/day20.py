def print_map(map: list[int], cols: int):
    for row in map:
        for col in range(cols):
            print('.' if row & (1 << col) == 0 else '#', end='')
        print()
    print()


def bit_count(n):
    count = 0

    while n > 0:
        count += 1
        n &= n-1

    return count


if __name__ == "__main__":
    example = """..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###"""

    example_input = example.split("\n")

    with open("input/day20.txt") as input:
        problem_input = [i.strip() for i in input.readlines()]

    input = problem_input

    algo_on_indexes = set(i for i, c in enumerate(input[0]) if c == "#")

    input_map = input[2:]

    map = [0]
    num_cols = len(input_map[0]) + 2

    for line in input_map:
        map.append(sum(1 << i + 1 for i, c in enumerate(line) if c == "#"))

    map.append(0)

    for iteration in range(2):
        new_map = [int('1' * (num_cols + 2))] if iteration % 2 == 0 and 0 in algo_on_indexes else [0]

        for i, row in enumerate(map):
            row_above = i - 1
            row_below = i + 1

            new_row = 1 if iteration % 2 == 0 and 0 in algo_on_indexes else 0

            for col in range(num_cols):
                index = ["0"] * 9

                col_left = col - 1
                col_right = col + 1

                if row_above >= 0:
                    if col_left >= 0 and map[row_above] & (1 << col_left):
                        index[0] = "1"

                    if map[row_above] & (1 << col):
                        index[1] = "1"

                    if col_right < num_cols and map[row_above] & (1 << col_right):
                        index[2] = "1"

                if col_left >= 0 and map[i] & (1 << col_left):
                    index[3] = "1"

                if map[i] & (1 << col):
                    index[4] = "1"

                if col_right < num_cols and map[i] & (1 << col_right):
                    index[5] = "1"

                if row_below < len(map) - 1:
                    if col_left >= 0 and map[row_below] & (1 << col_left):
                        index[6] = "1"

                    if map[row_below] & (1 << col):
                        index[7] = "1"

                    if col_right < num_cols and map[row_below] & (1 << col_right):
                        index[8] = "1"

                if int("".join(index), 2) in algo_on_indexes:
                    new_row |= 1 << (col+1)

            if iteration % 2 == 0 and 0 in algo_on_indexes:
                new_row |= 1 << (num_cols + 1)

            new_map.append(new_row)

        new_map.append(int('1' * (num_cols + 2)) if iteration % 2 == 0 and 0 in algo_on_indexes else 0)
        map = new_map
        num_cols += 2
        print_map(map, num_cols)

        print(sum(bit_count(r) for r in map))
