import time
from enum import Enum


class Space(Enum):
    FLOOR = '.'
    EMPTY = 'L'
    FILLED = '#'

    def __repr__(self):
        return self.value


def valid_coords(deck, y, x):
    return 0 <= y < len(deck) and 0 <= x < len(deck[y])


def count_occupied_neighbors(x, y, deck):
    nw = [y-1, x-1]
    n = [y-1, x]
    ne = [y-1, x+1]
    w = [y, x-1]
    e = [y, x+1]
    sw = [y+1, x-1]
    s = [y+1, x]
    se = [y+1, x+1]

    neighbors = []

    while valid_coords(deck, *nw):
        contents = deck[nw[0]][nw[1]]

        if contents == Space.FLOOR:
            nw = [nw[0] - 1, nw[1] - 1]
        else:
            neighbors.append(contents)
            break

    while valid_coords(deck, *n):
        contents = deck[n[0]][n[1]]

        if contents == Space.FLOOR:
            n = [n[0] - 1, n[1]]
        else:
            neighbors.append(contents)
            break

    while valid_coords(deck, *ne):
        contents = deck[ne[0]][ne[1]]

        if contents == Space.FLOOR:
            ne = [ne[0] - 1, ne[1] + 1]
        else:
            neighbors.append(contents)
            break

    while valid_coords(deck, *w):
        contents = deck[w[0]][w[1]]

        if contents == Space.FLOOR:
            w = [w[0], w[1] - 1]
        else:
            neighbors.append(contents)
            break

    while valid_coords(deck, *e):
        contents = deck[e[0]][e[1]]

        if contents == Space.FLOOR:
            e = [e[0], e[1] + 1]
        else:
            neighbors.append(contents)
            break

    while valid_coords(deck, *sw):
        contents = deck[nw[0]][nw[1]]

        if contents == Space.FLOOR:
            sw = [sw[0] + 1, sw[1] - 1]
        else:
            neighbors.append(contents)
            break

    while valid_coords(deck, *s):
        contents = deck[n[0]][n[1]]

        if contents == Space.FLOOR:
            s = [s[0] + 1, s[1]]
        else:
            neighbors.append(contents)
            break

    while valid_coords(deck, *se):
        contents = deck[se[0]][se[1]]

        if contents == Space.FLOOR:
            se = [se[0] + 1, se[1] + 1]
        else:
            neighbors.append(contents)
            break

    return sum(1 for n in neighbors if n == Space.FILLED)


example = '''L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL'''

if __name__ == "__main__":
    deck = []

    with open('input/day11.txt') as input:
        # for line in input:
        for line in example.split('\n'):
            deck.append([Space(c) for c in line.strip()])

    while True:
        for row in deck:
            print(row)

        print()

        new_deck = []

        for y, row in enumerate(deck):
            new_row = []
            new_deck.append(new_row)

            for x, seat in enumerate(row):
                if seat == Space.EMPTY:
                    if count_occupied_neighbors(x, y, deck) == 0:
                        new_row.append(Space.FILLED)
                    else:
                        new_row.append(Space.EMPTY)
                elif seat == Space.FILLED:
                    if count_occupied_neighbors(x, y, deck) >= 5:
                        new_row.append(Space.EMPTY)
                    else:
                        new_row.append(Space.FILLED)
                else:
                    new_row.append(Space.FLOOR)

        if all(new_deck[i][j] == deck[i][j] for i in range(len(new_deck)) for j in range(len(new_deck[i]))):
            break

        deck = new_deck

    for row in deck:
        print(row)

    print(sum(1 for i in range(len(deck)) for j in range(len(deck[i])) if deck[i][j] == Space.FILLED))
