from aoc_2019.intcode import IntcodeMachine

if __name__ == '__main__':
    with open('25_input.txt') as droid_program:
        machine = IntcodeMachine(droid_program.readline().strip())

    while True:
        buffer = []

        while len(buffer) < 8 or ''.join(buffer[-8:]) != 'Command?':
            buffer.append(chr(machine.receive()))

        print(''.join(buffer))
        command = input('# ')

        for c in command:
            machine.send(ord(c))

        machine.send(ord('\n'))
