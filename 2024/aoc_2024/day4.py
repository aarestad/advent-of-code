def xmas_up(input, row, col):
    if row < 3:
        return False

    return (
        input[row][col]
        + input[row - 1][col]
        + input[row - 2][col]
        + input[row - 3][col]
        == "XMAS"
    )


def xmas_down(input, row, col):
    if row > len(input) - 4:
        return False

    return (
        input[row][col]
        + input[row + 1][col]
        + input[row + 2][col]
        + input[row + 3][col]
        == "XMAS"
    )


def xmas_left(input, row, col):
    if col < 3:
        return False

    return (input[row][col - 3 : col + 1][::-1]) == "XMAS"


def xmas_right(input, row, col):
    if col > len(input[row]) - 4:
        return False

    return input[row][col : col + 4] == "XMAS"


def xmas_nw(input, row, col):
    if row < 3 or col < 3:
        return False

    return (
        input[row][col]
        + input[row - 1][col - 1]
        + input[row - 2][col - 2]
        + input[row - 3][col - 3]
        == "XMAS"
    )


def xmas_ne(input, row, col):
    if row < 3 or col > len(input[row]) - 4:
        return False

    return (
        input[row][col]
        + input[row - 1][col + 1]
        + input[row - 2][col + 2]
        + input[row - 3][col + 3]
        == "XMAS"
    )


def xmas_sw(input, row, col):
    if row > len(input) - 4 or col < 3:
        return False

    return (
        input[row][col]
        + input[row + 1][col - 1]
        + input[row + 2][col - 2]
        + input[row + 3][col - 3]
        == "XMAS"
    )


def xmas_se(input, row, col):
    if row > len(input) - 4 or col > len(input[row]) - 4:
        return False

    return (
        input[row][col]
        + input[row + 1][col + 1]
        + input[row + 2][col + 2]
        + input[row + 3][col + 3]
        == "XMAS"
    )


def x_mas(input, row, col):
    if row < 1 or row > len(input) - 2 or col < 1 or col > len(input[row]) - 2:
        return False

    nw = input[row + 1][col + 1] + input[row][col] + input[row - 1][col - 1]
    ne = input[row + 1][col - 1] + input[row][col] + input[row - 1][col + 1]

    return nw in ["MAS", "SAM"] and ne in ["MAS", "SAM"]


if __name__ == "__main__":
    example = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

    example_input = example.split("\n")

    with open("input/day4.txt") as input:
        problem_input = [i.strip() for i in input.readlines()]

    word_search = problem_input

    xmases = 0

    for row in range(len(word_search)):
        for col in range(len(word_search[row])):
            if word_search[row][col] == "X":
                xmases += sum(
                    1
                    for dir in (
                        xmas_up,
                        xmas_down,
                        xmas_left,
                        xmas_right,
                        xmas_ne,
                        xmas_nw,
                        xmas_se,
                        xmas_sw,
                    )
                    if dir(word_search, row, col)
                )

    print(f"{xmases} XMASes")

    x_mases = 0

    for row in range(len(word_search)):
        for col in range(len(word_search[row])):
            if x_mas(word_search, row, col):
                x_mases += 1

    print(f"{x_mases} X-MASes")
