from aoc_2019.intcode import IntcodeMachine
import sys

if __name__ == '__main__':
    with open(sys.argv[1]) as intcode_program:
        machine = IntcodeMachine(intcode_program.readline().strip())

    map = []
    current_line = []

    while chr_code := machine.receive():
        if chr_code == 10:
            map.append(current_line)
            current_line = []
        else:
            current_line.append(chr_code)

    alignment_param_sum = 0

    for y, line in enumerate(map):
        if y == 0 or y == len(map) - 1:
            continue
        for x, c in enumerate(line):
            if x == 0 or x == len(line) - 1:
                continue
            pound = ord('#')
            if c == pound and \
                    line[x - 1] == pound and \
                    line[x + 1] == pound and \
                    map[y - 1][x] == pound and \
                    map[y + 1][x] == pound:
                alignment_param_sum += y * x

    print(alignment_param_sum)
