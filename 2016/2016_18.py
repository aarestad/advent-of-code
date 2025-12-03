# a new tile is a trap only in one of the following situations:
#
# Its left and center tiles are traps, but its right tile is not.
# Its center and right tiles are traps, but its left tile is not.
# Only its left tile is a trap.
# Only its right tile is a trap.


def is_trap_tile(parent_tiles):
    l = parent_tiles[0]
    c = parent_tiles[1]
    r = parent_tiles[2]

    return (
        (l and c and not r)
        or (not l and c and r)
        or (l and not c and not r)
        or (not l and not c and r)
    )


def print_row(row):
    for t in row:
        print("^" if t else ".", end="")
    print()


first_row_txt = ".^^^.^.^^^^^..^^^..^..^..^^..^.^.^.^^.^^....^.^...^.^^.^^.^^..^^..^.^..^^^.^^...^...^^....^^.^^^^^^^"

prev_row = []

for t in first_row_txt:
    prev_row.append(t == "^")

safe_tiles = 0

for parent_idx in range(400000):
    for t in prev_row:
        if not t:
            safe_tiles += 1

    if parent_idx % 10000 == 0:
        print(parent_idx)
    new_row = []

    for i in range(len(prev_row)):
        if i == 0:
            parent_tiles = [False] + prev_row[:2]
        elif i == len(prev_row) - 1:
            parent_tiles = prev_row[len(prev_row) - 2 :] + [False]
        else:
            parent_tiles = prev_row[i - 1 : i + 2]
        new_row.append(is_trap_tile(parent_tiles))

    prev_row = new_row

print(safe_tiles)
