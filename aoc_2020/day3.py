def count_trees(rows, delta_x, delta_y):
    row_length = len(rows[0])

    return sum(1 for idx, row in enumerate(rows[::delta_y])
               if row[((idx * delta_x) % row_length)] == '#')


if __name__ == '__main__':
    with open('input/day3.txt') as input_rows:
        mountain_rows = [row.strip() for row in input_rows.readlines()]

    print(count_trees(mountain_rows, 1, 1) *
          count_trees(mountain_rows, 3, 1) *
          count_trees(mountain_rows, 5, 1) *
          count_trees(mountain_rows, 7, 1) *
          count_trees(mountain_rows, 1, 2))
