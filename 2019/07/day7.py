from itertools import permutations, cycle
from typing import Callable, Dict, List
from enum import Enum
import functools


class ParamMode(Enum):
    INDIRECT = 0
    IMMEDIATE = 1


# noinspection PyUnusedLocal
class IntcodeMachine:
    def __init__(self, program: str, name='Intcode'):
        self.name = name
        self.memory: List[int] = [int(x) for x in program.split(',')]
        self.pc: int = 0
        self.trace = True
        self.input = None
        self.output = None
        self.generator = self.run()
        next(self.generator)

        def debug_input(func):
            @functools.wraps(func)
            def debug_wrapper(*args, **kwargs):
                if self.trace:
                    print()
                    # print('pc: {}'.format(self.pc))
                    # print('mem: {}'.format(self.memory))
                    # print('{}: {}'.format(func.__name__, args))

                func(*args, **kwargs)

            return debug_wrapper

        def fetch(arg: int, mode: ParamMode):
            if mode == ParamMode.IMMEDIATE:
                return arg

            try:
                return self.memory[arg]
            except IndexError:
                return 0

        def store(val: int, address: int, mode: ParamMode):
            try:
                self.memory[address] = val
            except IndexError:
                self.memory.extend([0] * (address - len(self.memory) + 1))
                self.memory[address] = val

        @debug_input
        def op_add(a_mode: ParamMode, b_mode: ParamMode, c_mode: ParamMode, a: int, b: int, c: int):
            addend_a = fetch(a, a_mode)
            addend_b = fetch(b, b_mode)
            store(addend_a + addend_b, c, c_mode)

            self.pc += 4

        @debug_input
        def op_mul(a_mode: ParamMode, b_mode: ParamMode, c_mode: ParamMode, a: int, b: int, c: int):
            mul_a = fetch(a, a_mode)
            mul_b = fetch(b, b_mode)
            store(mul_a * mul_b, c, c_mode)

            self.pc += 4

        @debug_input
        def op_input(a_mode: ParamMode, b_mode: ParamMode, c_mode: ParamMode, a: int):
            store(int(self.input), a, a_mode)
            self.input = None
            self.pc += 2

        @debug_input
        def op_output(a_mode: ParamMode, b_mode: ParamMode, c_mode: ParamMode, a: int):
            self.output = fetch(a, a_mode)
            self.pc += 2

        @debug_input
        def op_jit(a_mode: ParamMode, b_mode: ParamMode, c_mode: ParamMode, a: int, b: int):
            target = fetch(a, a_mode)
            dest_addr = fetch(b, b_mode)
            self.pc = dest_addr if target != 0 else self.pc + 3

        @debug_input
        def op_jif(a_mode: ParamMode, b_mode: ParamMode, c_mode: ParamMode, a: int, b: int):
            target = fetch(a, a_mode)
            dest_addr = fetch(b, b_mode)
            self.pc = dest_addr if target == 0 else self.pc + 3

        @debug_input
        def op_lt(a_mode: ParamMode, b_mode: ParamMode, c_mode: ParamMode, a: int, b: int, c: int):
            a_cmp = fetch(a, a_mode)
            b_cmp = fetch(b, b_mode)
            store(1 if a_cmp < b_cmp else 0, c, c_mode)

            self.pc += 4

        @debug_input
        def op_eq(a_mode: ParamMode, b_mode: ParamMode, c_mode: ParamMode, a: int, b: int, c: int):
            a_cmp = fetch(a, a_mode)
            b_cmp = fetch(b, b_mode)
            store(1 if a_cmp == b_cmp else 0, c, c_mode)

            self.pc += 4

        self.ops: Dict[int, (Callable, int)] = {
            1: (op_add, 3),
            2: (op_mul, 3),
            3: (op_input, 1),
            4: (op_output, 1),
            5: (op_jit, 2),
            6: (op_jif, 2),
            7: (op_lt, 3),
            8: (op_eq, 3),
            99: None
        }

    def send(self, value):
        try:
            self.generator.send(value)
        except StopIteration:
            if self.trace:
                print(f"{self.name}: 'send' hit StopIteration")

    def receive(self):
        try:
            for output in self.generator:
                if output is not None:
                    next(self.generator)
                    return output
        except StopIteration:
            if self.trace:
                print(f"{self.name}: 'receive' hit StopIteration")
            # noinspection PyUnboundLocalVariable
            return output

    def run(self):
        while True:
            input = yield

            if input is not None:
                if self.trace:
                    print(f"{self.name}: received {input}")
                self.input = input

            opcode_and_modes = self.memory[self.pc]

            opcode = opcode_and_modes % 100
            a_mode = ParamMode((opcode_and_modes // 100) % 10)
            b_mode = ParamMode((opcode_and_modes // 1000) % 10)
            c_mode = ParamMode((opcode_and_modes // 10000) % 10)

            try:
                op = self.ops[opcode]
            except KeyError:
                raise ValueError('invalid opcode: {}'.format(opcode))

            if opcode == 3 and self.input is None:
                if self.trace:
                    print("Waiting for input")
                continue

            if op:
                num_params = op[1]
                params = self.memory[self.pc + 1:self.pc + num_params + 1]
                # print('pc={}, original_op={}, args={}'.format(self.pc, opcode_and_modes, params))

                op[0](a_mode, b_mode, c_mode, *params)

                if self.output is not None:
                    if self.trace:
                        print(f"{self.name}: sent {self.output}")
                    yield self.output
                    self.output = None
            else:
                break


if __name__ == '__main__':
    names = 'ABCDE'

    def generate_amps(phases, program):
        amps = {}

        # Create and initialize five amplifiers
        for amp in range(len(names)):
            # Create amplifier
            amplifier = IntcodeMachine(program, names[amp])

            # Send amplifier phase
            amplifier.send(phases[amp])

            # Store the amplifier
            amps[names[amp]] = amplifier

        return amps

    with open('07_input.txt') as f:
        program = f.readline()

        max_signal = 0
        for phases in permutations(range(5, 10)):

            amps = generate_amps(phases, program)

            signal = 0

            for amp in cycle(names):
                amps[amp].send(signal)

                signal = amps[amp].receive()
                if signal is None:
                    break

                if signal > max_signal:
                    max_signal = signal

        print(max_signal)
