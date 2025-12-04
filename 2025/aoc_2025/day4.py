def part1(input):
    num_accessible = 0

    for y, l in enumerate(input):
        for x, c in enumerate(l):
            if c == '@' and surrounding_roll_count(input, x, y) < 4:
                num_accessible += 1
                print("x", end='')
            else:
                print(c, end='')

        print()

    return num_accessible

def part2(input):
    editable_board = [list(l) for l in input]

    num_removed = 0

    while True:
        roll_removed = False

        for y, l in enumerate(editable_board):
            for x, c in enumerate(l):
                if c == '@' and surrounding_roll_count(editable_board, x, y) < 4:
                    editable_board[y][x] = "x"
                    num_removed += 1
                    roll_removed = True
                    print("x", end='')
                else:
                    print(c, end='')

            print()

        print()

        if not roll_removed:
            break

    return num_removed

def surrounding_roll_count(input, x, y):
    count = 0

    if y > 0:
        if x > 0:
            count += 1 if input[y-1][x-1] == '@' else 0

        count += 1 if input[y-1][x] == '@' else 0

        if x < len(input[y-1])-1:
            count += 1 if input[y-1][x+1] == '@' else 0

    if x > 0:
        count += 1 if input[y][x-1] == '@' else 0
    if x < len(input[y])-1:
        count += 1 if input[y][x+1] == '@' else 0

    if y < len(input)-1:
        if x > 0:
            count += 1 if input[y + 1][x - 1] == '@' else 0

        count += 1 if input[y + 1][x] == '@' else 0

        if x < len(input[y - 1]) - 1:
            count += 1 if input[y + 1][x + 1] == '@' else 0

    return count

if __name__ == "__main__":
    example = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""

    example_input = example.split("\n")
    print(f"part 1: {part1(example_input)}")
    print(f"part 2: {part2(example_input)}")

    with open("input/day4.txt") as input:
        problem_input = [i.strip() for i in input.readlines()]
        print(f"part 1: {part1(problem_input)}")
        print(f"part 2: {part2(problem_input)}")
