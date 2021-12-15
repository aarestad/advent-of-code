from scipy.sparse import lil_matrix
from scipy.sparse.csgraph import dijkstra
import numpy as np


class ExtendedMap:
    def __init__(self, map_corner):
        self.map_corner = map_corner

    def __getitem__(self, coord):
        corner_row = coord[0] % len(self.map_corner)
        corner_col = coord[1] % len(self.map_corner[0])
        tile_row = coord[0] // len(self.map_corner)
        tile_col = coord[1] // len(self.map_corner[0])

        corner_val = int(self.map_corner[corner_row][corner_col])
        corner_val += tile_row
        corner_val += tile_col

        if corner_val > 9:
            corner_val -= 9

        return corner_val


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

    map = ExtendedMap(problem_input)

    tile_array_size = 5

    num_rows = len(problem_input) * tile_array_size
    num_cols = len(problem_input[0]) * tile_array_size
    array_size = num_rows * num_cols

    map_matrix = lil_matrix((array_size, array_size), dtype=np.int8)

    for r in range(num_rows):
        for c in range(num_cols):
            row = int(r)
            col = int(c)
            map_matrix_row_idx = row * num_rows + col

            if row > 0:
                map_matrix[map_matrix_row_idx, (row - 1) * num_rows + col] = int(
                    map[row - 1, col]
                )
            if row < num_rows - 1:
                map_matrix[map_matrix_row_idx, (row + 1) * num_rows + col] = int(
                    map[row + 1, col]
                )
            if col > 0:
                map_matrix[map_matrix_row_idx, row * num_rows + col - 1] = int(
                    map[row, col - 1]
                )
            if col < num_cols - 1:
                map_matrix[map_matrix_row_idx, row * num_rows + col + 1] = int(
                    map[row, col + 1]
                )

    result = dijkstra(map_matrix, directed=True, indices=0, min_only=True)
    print(result[-1])
