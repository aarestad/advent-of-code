with open("input/day4.txt") as input:
    problem_input = input.readlines()

example = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""

MARKED = -999


def mark_board(board: list[list[int]], drawn_num: int):
    for row in board:
        for i, val in enumerate(row):
            if val == drawn_num:
                row[i] = MARKED


def board_is_winner(board: list[list[int]]) -> bool:
    for row in board:
        if all(True if space == MARKED else False for space in row):
            return True
    for col in range(5):
        if all(
            True if space == MARKED else False for space in [row[col] for row in board]
        ):
            return True

    return False


def score_board(board: list[list[int]]) -> int:
    score = 0

    for row in board:
        for space in row:
            if space != MARKED:
                score += space

    return score


if __name__ == "__main__":
    calls = None
    boards = []
    in_progress_board = []

    for line in problem_input:
        # for line in example.split("\n"):
        line = line.strip()
        if calls is None:
            calls = [int(num) for num in line.split(",")]
            continue

        if not line and len(in_progress_board) > 0:
            boards.append(in_progress_board)
            in_progress_board = []
        elif line:
            in_progress_board.append([int(num) for num in line.split()])

    boards.append(in_progress_board)  # don't forget the last one

    for call in calls:
        for board in boards:
            mark_board(board, call)

            if board_is_winner(board):
                print(score_board(board) * call)
                boards = [b for b in boards if b != board]
