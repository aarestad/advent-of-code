import re

col_matcher = re.compile(r'x=(\d+) by (\d+)')
row_matcher = re.compile(r'y=(\d+) by (\d+)')

def print_screen(screen):
    for row in screen:
        for pixel in row:
            print('#' if pixel else '.', end='')
        print()
    print()

def process_cmd(cmd, screen):
    cmd_toks = cmd.split()

    if cmd_toks[0] == 'rect':
        (cols, rows) = [int(x) for x in cmd_toks[1].split('x')]

        for y in range(rows):
            for x in range(cols):
                screen[y][x] = True

    elif cmd_toks[0] == 'rotate':
        if cmd_toks[1] == 'column':
            col_results = col_matcher.match(' '.join(cmd_toks[2:]))
            col_number = int(col_results.group(1))
            col_shift = int(col_results.group(2))

            old_col = [row[col_number] for row in screen]
            new_col = [None] * len(old_col)

            i = 0

            for cell in old_col:
                if i + col_shift < len(new_col):
                    new_col[i + col_shift] = old_col[i]
                else:
                    new_col[i + col_shift - len(new_col)] = old_col[i]
                i += 1

            i = 0

            for cell in new_col:
                screen[i][col_number] = new_col[i]
                i += 1

        elif cmd_toks[1] == 'row':
            row_results = row_matcher.match(' '.join(cmd_toks[2:]))
            row_number = int(row_results.group(1))
            row_shift = int(row_results.group(2))

            old_row = screen[row_number]
            new_row = [None] * len(old_row)

            i = 0

            for cell in old_row:
                if i + row_shift < len(new_row):
                    new_row[i + row_shift] = old_row[i]
                else:
                    new_row[i + row_shift - len(new_row)] = old_row[i]
                i += 1

            i = 0

            for cell in new_row:
                screen[row_number][i] = new_row[i]
                i += 1

    print_screen(screen)

ROWS = 6
COLS = 50

screen = []

for i in range(ROWS):
    screen.append([False] * COLS)

print_screen(screen)

with open('input_8.txt') as commands:
    cmds = [c.strip() for c in commands.readlines()]

for cmd in cmds:
    process_cmd(cmd, screen)

pixel_count = 0

for row in screen:
    for c in row:
        if c: pixel_count += 1

print(pixel_count)
