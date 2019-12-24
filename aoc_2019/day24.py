def biodiversity_rating(board):
    board = ''.join([''.join(line) for line in board])

    return sum(2 ** i for i in range(len(board)) if board[i] == '#')


def next_boards(boards):
    # init new boards
    new_boards = [[[] for _ in range(5)] for __ in range(len(boards) + 2)]

    # add dummy blank outer and inner boards
    boards.insert(0, [['.' for _ in range(5)] for __ in range(5)])
    boards.append([['.' for _ in range(5)] for __ in range(5)])

    for idx, new_board in enumerate(new_boards):
        outer_board = boards[idx - 1] if idx - 1 >= 0 else [['.' for _ in range(5)] for __ in range(5)]
        current_board = boards[idx]
        inner_board = boards[idx + 1] if idx + 1 < len(boards) else [['.' for _ in range(5)] for __ in range(5)]

        for y in range(5):
            for x in range(5):
                if y == 2 and x == 2:
                    new_board[y].append('.')
                    continue

                neighbors = []

                # UP
                if y == 0:
                    neighbors.append(outer_board[1][2])
                elif y != 3 or x != 2:
                    neighbors.append(current_board[y - 1][x])
                else:
                    for inner_x in range(5):
                        neighbors.append(inner_board[4][inner_x])

                # DOWN
                if y == 4:
                    neighbors.append(outer_board[3][2])
                elif y != 1 or y != 2:
                    neighbors.append(current_board[y + 1][x])
                else:
                    for inner_x in range(5):
                        neighbors.append(inner_board[0][inner_x])

                # LEFT
                if x == 0:
                    neighbors.append(outer_board[2][1])

                elif y != 2 or x != 3:
                    neighbors.append(current_board[y][x - 1])
                else:
                    for inner_y in range(5):
                        neighbors.append(inner_board[inner_y][4])

                # RIGHT
                if x == 4:
                    neighbors.append(outer_board[2][3])
                elif y != 2 or x != 1:
                    neighbors.append(current_board[y][x + 1])
                else:
                    if x == 1:
                        for inner_y in range(5):
                            neighbors.append(inner_board[inner_y][0])

                live_neighbors = sum(1 for n in neighbors if n == '#')

                current_space = current_board[y][x]

                if current_space == '#':
                    new_board[y].append('#' if live_neighbors == 1 else '.')
                else:
                    new_board[y].append('#' if live_neighbors in (1, 2) else '.')

    return new_boards


if __name__ == '__main__':
    boards = []

    with open('24_input.txt') as gol_input:
        init_board = []

        for board_line in gol_input:
            init_board.append(list(board_line.strip()))

        boards.append(init_board)

    for _ in range(200):
        print(f'iteration {_}')
        boards = next_boards(boards)

    total_bugs = 0

    for b in boards:
        board_in_line = ''.join(''.join(line) for line in b)
        total_bugs += sum(1 for c in board_in_line if c == '#')

    print(total_bugs)
