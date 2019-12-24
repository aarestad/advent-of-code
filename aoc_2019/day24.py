def biodiversity_rating(board):
    board = ''.join([''.join(line) for line in board])

    return sum(2 ** i for i in range(len(board)) if board[i] == '#')


def next_boards(boards):
    new_boards = [[[] for _ in range(5)] for __ in range(len(boards) + 2)]

    for idx, new_board in enumerate(new_boards):
        outer_board = boards[idx - 2] if (0 <= idx - 2 < len(boards)) else [['.' for _ in range(5)] for __ in range(5)]
        current_board = boards[idx - 1] if (0 <= idx - 1 < len(boards)) else [['.' for _ in range(5)] for __ in range(5)]
        inner_board = boards[idx] if idx < len(boards) else [['.' for _ in range(5)] for __ in range(5)]

        for y in range(5):
            for x in range(5):
                neighbors = []

                if y == 0:
                    if x == 0:
                        neighbors.append(outer_board[1][2])  # U
                        neighbors.append(current_board[1][0])  # D
                        neighbors.append(outer_board[2][1])  # L
                        neighbors.append(current_board[0][1])  # R
                    if x == 1:
                        neighbors.append(outer_board[1][2])  # U
                        neighbors.append(current_board[1][1])  # D
                        neighbors.append(current_board[0][0])  # L
                        neighbors.append(current_board[0][2])  # R
                    if x == 2:
                        neighbors.append(outer_board[1][2])  # U
                        neighbors.append(current_board[1][2])  # D
                        neighbors.append(current_board[0][1])  # L
                        neighbors.append(current_board[0][3])  # R
                    if x == 3:
                        neighbors.append(outer_board[1][2])  # U
                        neighbors.append(current_board[1][3])  # D
                        neighbors.append(current_board[0][2])  # L
                        neighbors.append(current_board[0][4])  # R
                    if x == 4:
                        neighbors.append(outer_board[1][2])  # U
                        neighbors.append(current_board[1][4])  # D
                        neighbors.append(current_board[0][3])  # L
                        neighbors.append(outer_board[2][3])  # R
                if y == 1:
                    if x == 0:
                        neighbors.append(current_board[0][0])  # U
                        neighbors.append(current_board[2][0])  # D
                        neighbors.append(outer_board[2][1])  # L
                        neighbors.append(current_board[1][1])  # R
                    if x == 1:
                        neighbors.append(current_board[0][1])  # U
                        neighbors.append(current_board[2][1])  # D
                        neighbors.append(current_board[1][0])  # L
                        neighbors.append(current_board[1][2])  # R
                    if x == 2:
                        neighbors.append(current_board[0][2])  # U
                        neighbors.append(inner_board[0][0])  # D
                        neighbors.append(inner_board[0][1])  # D
                        neighbors.append(inner_board[0][2])  # D
                        neighbors.append(inner_board[0][3])  # D
                        neighbors.append(inner_board[0][4])  # D
                        neighbors.append(current_board[1][1])  # L
                        neighbors.append(current_board[1][3])  # R
                    if x == 3:
                        neighbors.append(current_board[0][1])  # U
                        neighbors.append(current_board[2][1])  # D
                        neighbors.append(current_board[1][0])  # L
                        neighbors.append(current_board[1][2])  # R
                    if x == 4:
                        neighbors.append(outer_board[1][2])  # U
                        neighbors.append(current_board[1][4])  # D
                        neighbors.append(current_board[0][3])  # L
                        neighbors.append(outer_board[2][3])  # R

                if y == 2:
                    if x == 0:
                        neighbors.append(current_board[1][0])  # U
                        neighbors.append(current_board[3][0])  # D
                        neighbors.append(outer_board[2][1])  # L
                        neighbors.append(current_board[2][1])  # R
                    if x == 1:
                        neighbors.append(current_board[1][1])  # U
                        neighbors.append(current_board[3][1])  # D
                        neighbors.append(current_board[2][0])  # L
                        neighbors.append(inner_board[0][0])  # R
                        neighbors.append(inner_board[1][0])  # R
                        neighbors.append(inner_board[2][0])  # R
                        neighbors.append(inner_board[3][0])  # R
                        neighbors.append(inner_board[4][0])  # R
                    if x == 3:
                        neighbors.append(current_board[1][3])  # U
                        neighbors.append(current_board[3][3])  # D
                        neighbors.append(inner_board[0][4])  # L
                        neighbors.append(inner_board[1][4])  # L
                        neighbors.append(inner_board[2][4])  # L
                        neighbors.append(inner_board[3][4])  # L
                        neighbors.append(inner_board[4][4])  # L
                        neighbors.append(current_board[2][4])  # R
                    if x == 4:
                        neighbors.append(current_board[1][4])  # U
                        neighbors.append(current_board[3][4])  # D
                        neighbors.append(current_board[2][3])  # L
                        neighbors.append(outer_board[2][3])  # R

                if y == 3:
                    if x == 0:
                        neighbors.append(current_board[2][0])  # U
                        neighbors.append(current_board[4][0])  # D
                        neighbors.append(outer_board[2][1])  # L
                        neighbors.append(current_board[3][1])  # R
                    if x == 1:
                        neighbors.append(current_board[2][1])  # U
                        neighbors.append(current_board[4][1])  # D
                        neighbors.append(current_board[3][0])  # L
                        neighbors.append(current_board[3][2])  # R
                    if x == 2:
                        neighbors.append(inner_board[4][0])  # U
                        neighbors.append(inner_board[4][1])  # U
                        neighbors.append(inner_board[4][2])  # U
                        neighbors.append(inner_board[4][3])  # U
                        neighbors.append(inner_board[4][4])  # U
                        neighbors.append(current_board[4][2])  # D
                        neighbors.append(current_board[3][1])  # L
                        neighbors.append(current_board[3][3])  # R
                    if x == 3:
                        neighbors.append(current_board[2][3])  # U
                        neighbors.append(current_board[4][3])  # D
                        neighbors.append(current_board[3][2])  # L
                        neighbors.append(current_board[3][4])  # R
                    if x == 4:
                        neighbors.append(current_board[2][4])  # U
                        neighbors.append(current_board[4][4])  # D
                        neighbors.append(current_board[3][3])  # L
                        neighbors.append(outer_board[2][3])  # R

                if y == 4:
                    if x == 0:
                        neighbors.append(current_board[3][0])  # U
                        neighbors.append(outer_board[3][2])  # D
                        neighbors.append(outer_board[2][1])  # L
                        neighbors.append(current_board[4][1])  # R
                    if x == 1:
                        neighbors.append(current_board[3][1])  # U
                        neighbors.append(outer_board[3][2])  # D
                        neighbors.append(current_board[4][0])  # L
                        neighbors.append(current_board[4][2])  # R
                    if x == 2:
                        neighbors.append(current_board[3][2])  # U
                        neighbors.append(outer_board[3][2])  # D
                        neighbors.append(current_board[4][1])  # L
                        neighbors.append(current_board[4][3])  # R
                    if x == 3:
                        neighbors.append(current_board[3][3])  # U
                        neighbors.append(outer_board[3][2])  # D
                        neighbors.append(current_board[4][2])  # L
                        neighbors.append(current_board[4][4])  # R
                    if x == 4:
                        neighbors.append(current_board[3][4])  # U
                        neighbors.append(outer_board[3][2])  # D
                        neighbors.append(current_board[4][3])  # L
                        neighbors.append(outer_board[2][3])  # R

                live_neighbors = sum(1 for n in neighbors if n == '#')

                current_space = board[y][x]

                if current_space == '#':
                    new_board[y].append('#' if live_neighbors == 1 else '.')
                else:
                    new_board[y].append('#' if live_neighbors in (1, 2) else '.')

    return new_boards


if __name__ == '__main__':
    boards = []

    with open('24_input.txt') as gol_input:
        board = []

        for board_line in gol_input:
            board.append(list(board_line.strip()))

        boards.append(board)

    for _ in range(200):
        print(f'iteration {_}')
        boards = next_boards(boards)

    total_bugs = 0

    for board in boards:
        board_in_line = ''.join(''.join(l) for l in board)
        total_bugs += sum(1 for c in board_in_line if c == '#')

    print(total_bugs)
