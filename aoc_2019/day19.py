from aoc_2019.intcode import IntcodeMachine
import sys

if __name__ == '__main__':
    with open(sys.argv[1]) as intcode_program:
        prog = intcode_program.readline().strip()

    affected_points = 0
    answer = 0

    for y in range(1000, 1100):
        print(f'{y}: ', end='')
        last_x_affected = None
        num_x_affected = 0

        for x in range(1100, 1500):
            machine = IntcodeMachine(prog)

            machine.send(0)
            machine.send(x)
            machine.send(y)

            response = machine.receive()

            if response:
                num_x_affected += 1
                last_x_affected = x

        if num_x_affected >= 199:
            first_x_affected = last_x_affected - 99
            num_y_affected = 0

            for double_check_y in range(y, y + 100):
                machine = IntcodeMachine(prog)
                machine.send(0)
                machine.send(first_x_affected)
                machine.send(double_check_y)
                num_y_affected += machine.receive()

            print(f'{num_y_affected} affected')

            if num_y_affected == 100:
                answer = first_x_affected * 10_000 + y
                print(answer)
                exit()
        print()


