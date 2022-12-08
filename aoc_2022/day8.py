if __name__ == "__main__":
    example = """30373
25512
65332
33549
35390"""

    example_input = example.split("\n")

    with open("input/day8.txt") as input:
        problem_input = [i.strip() for i in input.readlines()]

    tree_map = [[int(t) for t in line] for line in problem_input]

    num_rows = len(tree_map)
    num_cols = len(tree_map[0])

    visible_trees = 2 * num_rows + 2 * num_cols - 4  # de-double-count the corners

    for row in range(1, num_rows - 1):
        for col in range(1, num_cols - 1):
            tree_row = tree_map[row]
            tree_col = [tree_map[r][col] for r in range(num_rows)]
            tree = tree_map[row][col]

            visible_from_left = all(t < tree for t in tree_row[0:col])
            visible_from_right = all(t < tree for t in tree_row[col + 1 :])
            visible_from_top = all(t < tree for t in tree_col[0:row])
            visible_from_bottom = all(t < tree for t in tree_col[row + 1 :])

            tree_visible = any(
                (
                    visible_from_left,
                    visible_from_right,
                    visible_from_top,
                    visible_from_bottom,
                )
            )

            if tree_visible:
                visible_trees += 1

    print(f"visible trees: {visible_trees}")
