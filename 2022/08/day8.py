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

    # precompute the columns
    tree_cols = [[tree_map[r][c] for r in range(num_rows)] for c in range(num_cols)]

    visible_trees = 2 * num_rows + 2 * num_cols - 4  # de-double-count the corners
    best_scenic_score = 0

    for row in range(1, num_rows - 1):
        tree_row = tree_map[row]

        for col in range(1, num_cols - 1):
            tree_col = tree_cols[col]
            tree = tree_map[row][col]

            # Part 1
            visible_from_left = all(t < tree for t in tree_row[0:col])
            visible_from_right = all(t < tree for t in tree_row[col + 1 :])
            visible_from_top = all(t < tree for t in tree_col[0:row])
            visible_from_bottom = all(t < tree for t in tree_col[row + 1 :])

            if any(
                (
                    visible_from_left,
                    visible_from_right,
                    visible_from_top,
                    visible_from_bottom,
                )
            ):
                visible_trees += 1

            # Part 2
            left_score = 0

            for t in tree_row[col - 1 :: -1]:
                left_score += 1
                if t >= tree:
                    break

            right_score = 0

            for t in tree_row[col + 1 :]:
                right_score += 1
                if t >= tree:
                    break

            up_score = 0

            for t in tree_col[row - 1 :: -1]:
                up_score += 1
                if t >= tree:
                    break

            down_score = 0

            for t in tree_col[row + 1 :]:
                down_score += 1
                if t >= tree:
                    break

            scenic_score = left_score * right_score * up_score * down_score

            if scenic_score > best_scenic_score:
                best_scenic_score = scenic_score

    print(f"part 1: visible trees: {visible_trees}")
    print(f"part 2: best scenic score: {best_scenic_score}")
