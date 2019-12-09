from typing import Callable, Dict, List
from enum import Enum
import functools


class ParamMode(Enum):
    INDIRECT = 0
    IMMEDIATE = 1
    RELATIVE = 2


# noinspection PyUnusedLocal
class IntcodeMachine:
    def __init__(self, program: str):
        self.memory: List[int] = [int(x) for x in program.split(',')]
        self.memory += [0] * 100
        self.pc: int = 0
        self.relative_base = 0

        me = self

        def debug_input(func):
            @functools.wraps(func)
            def debug_wrapper(*args, **kwargs):
                # print()
                # print('pc: {}'.format(me.pc))
                # print('mem: {}'.format(me.memory))
                # print('relative base: {}'.format(me.relative_base))
                # print('{}: {}'.format(func.__name__, args))
                func(*args, **kwargs)

            return debug_wrapper

        def adjust_address(address: int, mode: ParamMode):
            adjusted = address

            if mode == ParamMode.INDIRECT:
                pass
            elif mode == ParamMode.RELATIVE:
                adjusted += self.relative_base
            else:
                raise ValueError('bad ParamMode: {}'.format(mode))

            if adjusted < 0:
                raise ValueError(
                    'negative memory address: {} (orig={}, relative_base={})'.format(adjusted, address,
                                                                                     self.relative_base))

            return adjusted

        def fetch(arg: int, mode: ParamMode):
            if mode == ParamMode.IMMEDIATE:
                return arg

            address = adjust_address(arg, mode)
            return self.memory[address]

        @debug_input
        def op_add(a_mode: ParamMode, b_mode: ParamMode, c_mode: ParamMode, a: int, b: int, c: int):
            addend_a = fetch(a, a_mode)
            addend_b = fetch(b, b_mode)
            c_addr = adjust_address(c, c_mode)
            # print('ADD {} {} {}'.format(addend_a, addend_b, c_addr))

            self.memory[c_addr] = addend_a + addend_b

            self.pc += 4

        @debug_input
        def op_mul(a_mode: ParamMode, b_mode: ParamMode, c_mode: ParamMode, a: int, b: int, c: int):
            mul_a = fetch(a, a_mode)
            mul_b = fetch(b, b_mode)
            c_addr = adjust_address(c, c_mode)
            # print('MUL {} {} {}'.format(mul_a, mul_b, c_addr))

            self.memory[c_addr] = mul_a * mul_b

            self.pc += 4

        @debug_input
        def op_input(a_mode: ParamMode, b_mode: ParamMode, c_mode: ParamMode, a: int):
            a_addr = adjust_address(a, a_mode)
            # print('INP {}'.format(a_addr))
            self.memory[adjust_address(a, a_mode)] = int(input('enter a number: '))
            self.pc += 2

        @debug_input
        def op_output(a_mode: ParamMode, b_mode: ParamMode, c_mode: ParamMode, a: int):
            a_val = fetch(a, a_mode)
            # print('OUT {}'.format(a_val))
            print(a_val)
            self.pc += 2

        @debug_input
        def op_jit(a_mode: ParamMode, b_mode: ParamMode, c_mode: ParamMode, a: int, b: int):
            target = fetch(a, a_mode)
            dest_addr = fetch(b, b_mode)
            # print('JIT {} {}'.format(target, dest_addr))
            self.pc = dest_addr if target != 0 else self.pc + 3

        @debug_input
        def op_jif(a_mode: ParamMode, b_mode: ParamMode, c_mode: ParamMode, a: int, b: int):
            target = fetch(a, a_mode)
            dest_addr = fetch(b, b_mode)
            # print('JIF {} {}'.format(target, dest_addr))
            self.pc = dest_addr if target == 0 else self.pc + 3

        @debug_input
        def op_lt(a_mode: ParamMode, b_mode: ParamMode, c_mode: ParamMode, a: int, b: int, c: int):
            a_cmp = fetch(a, a_mode)
            b_cmp = fetch(b, b_mode)
            c_addr = adjust_address(c, c_mode)
            # print('LT {} {} {}'.format(a_cmp, b_cmp, c_addr))

            self.memory[c_addr] = 1 if a_cmp < b_cmp else 0

            self.pc += 4

        @debug_input
        def op_eq(a_mode: ParamMode, b_mode: ParamMode, c_mode: ParamMode, a: int, b: int, c: int):
            a_cmp = fetch(a, a_mode)
            b_cmp = fetch(b, b_mode)
            c_addr = adjust_address(c, c_mode)
            # print('EQ {} {} {}'.format(a_cmp, b_cmp, c_addr))

            self.memory[c_addr] = 1 if a_cmp == b_cmp else 0

            self.pc += 4

        @debug_input
        def op_arb(a_mode: ParamMode, b_mode: ParamMode, c_mode: ParamMode, a: int):
            a_new_base = fetch(a, a_mode)
            # print('ARB {}'.format(a_new_base))
            self.relative_base += a_new_base
            self.pc += 2

        self.ops: Dict[int, (Callable, int)] = {
            1: (op_add, 3),
            2: (op_mul, 3),
            3: (op_input, 1),
            4: (op_output, 1),
            5: (op_jit, 2),
            6: (op_jif, 2),
            7: (op_lt, 3),
            8: (op_eq, 3),
            9: (op_arb, 1),
            99: None
        }

    def run(self) -> None:
        while True:
            opcode_and_modes = self.memory[self.pc]

            opcode = opcode_and_modes % 100
            a_mode = ParamMode((opcode_and_modes // 100) % 10)
            b_mode = ParamMode((opcode_and_modes // 1000) % 10)
            c_mode = ParamMode((opcode_and_modes // 10000) % 10)

            try:
                op = self.ops[opcode]
            except KeyError:
                raise ValueError('invalid opcode: {}'.format(opcode))

            if op:
                num_params = op[1]
                params = self.memory[self.pc + 1:self.pc + num_params + 1]
                # print('pc={}, original_op={}, args={}'.format(self.pc, opcode_and_modes, params))

                op[0](a_mode, b_mode, c_mode, *params)
            else:
                break


if __name__ == '__main__':
    with open('09_input.txt') as program:
        machine = IntcodeMachine(program.readline().strip())
    # machine = IntcodeMachine('109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99')
    machine.run()
