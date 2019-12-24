from itertools import count


def biodiversity_rating(board):
    board = ''.join([''.join(line) for line in board])

    return sum(2 ** i for i in range(len(board)) if board[i] == '#')


def next_board(board):
    new_board = [[] for _ in range(5)]

    for y in range(5):
        for x in range(5):
            neighbors = []

            if x > 0:
                # left
                neighbors.append(board[y][x - 1])
            if x < 4:
                # right
                neighbors.append(board[y][x + 1])
            if y > 0:
                # up
                neighbors.append(board[y - 1][x])
            if y < 4:
                # down
                neighbors.append(board[y + 1][x])

            live_neighbors = sum(1 for n in neighbors if n == '#')

            current_space = board[y][x]

            if current_space == '#':
                new_board[y].append('#' if live_neighbors == 1 else '.')
            else:
                new_board[y].append('#' if live_neighbors in (1, 2) else '.')

    return new_board


if __name__ == '__main__':
    board = []

    with open('24_input.txt') as gol_input:
        for board_line in gol_input:
            board.append(list(board_line.strip()))

    seen_biodiversity_ratings = {biodiversity_rating(board)}

    for x in count(start=1):
        board = next_board(board)
        rating = biodiversity_rating(board)

        if rating in seen_biodiversity_ratings:
            print(rating)
            exit()

        seen_biodiversity_ratings.add(rating)
