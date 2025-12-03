from aoc_2019.intcode import IntcodeMachine
import sys

if __name__ == '__main__':
    with open(sys.argv[1]) as intcode_program:
        machine = IntcodeMachine(intcode_program.readline().strip())

    # machine.memory[0] = 2

    map = []
    current_line = []

    while chr_code := machine.receive():
        if chr_code == 10:
            map.append(current_line)
            current_line = []
        else:
            current_line.append(chr_code)

    for line in map:
        print(''.join(chr(c) for c in line))
