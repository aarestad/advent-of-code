from scipy.sparse import lil_matrix
from scipy.sparse.csgraph import dijkstra
import numpy as np

if __name__ == "__main__":
    example = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""

    example_input = example.split("\n")

    with open("input/day15.txt") as input:
        problem_input = [i.strip() for i in input.readlines()]

    map = problem_input

    num_rows = len(map)
    num_cols = len(map[0])
    array_size = num_rows * num_cols

    map_matrix = lil_matrix((array_size, array_size), dtype=np.int8)

    for r in range(num_rows):
        for c in range(num_cols):
            row = int(r)
            col = int(c)
            map_matrix_row_idx = row * num_rows + col

            if row > 0:
                map_matrix[map_matrix_row_idx, (row - 1) * num_rows + col] = int(
                    map[row - 1][col]
                )
            if row < num_rows - 1:
                map_matrix[map_matrix_row_idx, (row + 1) * num_rows + col] = int(
                    map[row + 1][col]
                )
            if col > 0:
                map_matrix[map_matrix_row_idx, row * num_rows + col - 1] = int(
                    map[row][col - 1]
                )
            if col < num_cols - 1:
                map_matrix[map_matrix_row_idx, row * num_rows + col + 1] = int(
                    map[row][col + 1]
                )

    result = dijkstra(map_matrix, directed=True, indices=0, min_only=True)
    print(result[-1])
