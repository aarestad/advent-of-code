from aoc_2019.intcode import IntcodeMachine
import sys

if __name__ == '__main__':
    with open(sys.argv[1]) as intcode_program:
        prog = intcode_program.readline().strip()

    affected_points = 0
    answer = 0

    for y in range(90, 120):
        print(f"{y}: ", end='')
        last_x_affected = None
        num_x_affected = 0

        for x in range(100, 150):
            machine = IntcodeMachine(prog)

            machine.send(0)
            machine.send(x)
            machine.send(y)

            response = machine.receive()
            print('#' if response else '.', end='')

            if response:
                num_x_affected += 1
                last_x_affected = x

        if num_x_affected >= 10:
            first_x_affected = last_x_affected - 9
            num_y_affected = 0

            for double_check_y in range(y, y + 10):
                machine = IntcodeMachine(prog)
                machine.send(0)
                machine.send(first_x_affected)
                machine.send(double_check_y)
                num_y_affected += machine.receive()

            if num_y_affected == 10:
                answer = first_x_affected * 10_000 + y
                print(answer)
                exit()
        print()

    print(answer)


