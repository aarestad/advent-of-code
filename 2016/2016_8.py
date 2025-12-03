import re
import curses
import time

col_matcher = re.compile(r"x=(\d+) by (\d+)")
row_matcher = re.compile(r"y=(\d+) by (\d+)")


def rect(cols, rows, screen):
    for y in range(rows):
        for x in range(cols):
            screen[y][x] = True


def rotate_column(col_number, col_shift, screen):
    old_col = [row[col_number] for row in screen]
    new_col = [None] * len(old_col)

    i = 0
    for cell in old_col:
        new_col[(i + col_shift) % len(new_col)] = old_col[i]
        i += 1

    i = 0
    for cell in new_col:
        screen[i][col_number] = new_col[i]
        i += 1


def rotate_row(row_number, row_shift, screen):
    old_row = screen[row_number]
    new_row = [None] * len(old_row)

    i = 0
    for cell in old_row:
        new_row[(i + row_shift) % len(new_row)] = old_row[i]
        i += 1

    i = 0
    for cell in new_row:
        screen[row_number][i] = new_row[i]
        i += 1


def process_cmd(cmd, screen):
    cmd_toks = cmd.split()

    if cmd_toks[0] == "rect":
        (cols, rows) = [int(x) for x in cmd_toks[1].split("x")]
        rect(cols, rows, screen)
    elif cmd_toks[0] == "rotate":
        if cmd_toks[1] == "column":
            col_results = col_matcher.match(" ".join(cmd_toks[2:]))
            col_number = int(col_results.group(1))
            col_shift = int(col_results.group(2))
            rotate_column(col_number, col_shift, screen)
        elif cmd_toks[1] == "row":
            row_results = row_matcher.match(" ".join(cmd_toks[2:]))
            row_number = int(row_results.group(1))
            row_shift = int(row_results.group(2))
            rotate_row(row_number, row_shift, screen)


def print_screen(scr):
    for row in scr:
        for pixel in row:
            print("#" if pixel else ".", end="")
        print()
    print()


def print_screen_curses(stdscr, scr):
    for y in range(ROWS):
        for x in range(COLS):
            stdscr.addch(y, x, "#" if scr[y][x] else ".")

    stdscr.refresh()
    time.sleep(0.05)


if __name__ == "__main__":
    ROWS = 6
    COLS = 50

    screen = []

    for i in range(ROWS):
        screen.append([False] * COLS)

    with open("input_8.txt") as commands:
        cmds = [c.strip() for c in commands.readlines()]

    curses.wrapper(print_screen_curses, screen)

    for cmd in cmds:
        process_cmd(cmd, screen)
        curses.wrapper(print_screen_curses, screen)

    pixel_count = 0

    for row in screen:
        for c in row:
            if c:
                pixel_count += 1

    print("%d pixels lit up" % pixel_count)
