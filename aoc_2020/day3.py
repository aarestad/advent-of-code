example = '''..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#'''


def count_trees(rows, x_diff, y_diff=1):
    filtered_rows = rows[::y_diff]

    row_length = len(filtered_rows[0])

    trees = 0

    for idx, row in enumerate(filtered_rows):
        if row[((idx * x_diff) % row_length)] == '#':
            trees += 1

    return trees


if __name__ == '__main__':
    mountain_rows = [row.strip() for row in open('input/day3.txt').readlines()]
    # mountain_rows = example.split('\n')

    print(count_trees(mountain_rows, 1) *
          count_trees(mountain_rows, 3) *
          count_trees(mountain_rows, 5) *
          count_trees(mountain_rows, 7) *
          count_trees(mountain_rows, 1, 2))
