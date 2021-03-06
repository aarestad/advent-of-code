from typing import Callable, Dict, List
from enum import Enum


class ParamMode(Enum):
    INDIRECT = 0
    IMMEDIATE = 1


# noinspection PyUnusedLocal
class IntcodeMachine:
    def __init__(self, program: str):
        self.memory: List[int] = [int(x) for x in program.split(',')]
        self.pc: int = 0

        def op_add(a_mode: ParamMode, b_mode: ParamMode, c_mode: ParamMode, a: int, b: int, c: int):
            addend_a = a if a_mode == ParamMode.IMMEDIATE else self.memory[a]
            addend_b = b if b_mode == ParamMode.IMMEDIATE else self.memory[b]
            self.memory[c] = addend_a + addend_b
            self.pc += 4

        def op_mul(a_mode: ParamMode, b_mode: ParamMode, c_mode: ParamMode, a: int, b: int, c: int):
            addend_a = a if a_mode == ParamMode.IMMEDIATE else self.memory[a]
            addend_b = b if b_mode == ParamMode.IMMEDIATE else self.memory[b]
            self.memory[c] = addend_a * addend_b
            self.pc += 4

        def op_input(a_mode: ParamMode, b_mode: ParamMode, c_mode: ParamMode, a: int):
            self.memory[a] = int(input('enter a number: '))
            self.pc += 2

        def op_output(a_mode: ParamMode, b_mode: ParamMode, c_mode: ParamMode, a: int):
            print(a if a_mode == ParamMode.IMMEDIATE else self.memory[a])
            self.pc += 2

        def op_jit(a_mode: ParamMode, b_mode: ParamMode, c_mode: ParamMode, a: int, b: int):
            target = a if a_mode == ParamMode.IMMEDIATE else self.memory[a]
            dest_addr = b if b_mode == ParamMode.IMMEDIATE else self.memory[b]
            self.pc = dest_addr if target != 0 else self.pc + 3

        def op_jif(a_mode: ParamMode, b_mode: ParamMode, c_mode: ParamMode, a: int, b: int):
            target = a if a_mode == ParamMode.IMMEDIATE else self.memory[a]
            dest_addr = b if b_mode == ParamMode.IMMEDIATE else self.memory[b]
            self.pc = dest_addr if target == 0 else self.pc + 3

        def op_lt(a_mode: ParamMode, b_mode: ParamMode, c_mode: ParamMode, a: int, b: int, c: int):
            a_cmp = a if a_mode == ParamMode.IMMEDIATE else self.memory[a]
            b_cmp = b if b_mode == ParamMode.IMMEDIATE else self.memory[b]
            self.memory[c] = 1 if a_cmp < b_cmp else 0
            self.pc += 4

        def op_eq(a_mode: ParamMode, b_mode: ParamMode, c_mode: ParamMode, a: int, b: int, c: int):
            a_cmp = a if a_mode == ParamMode.IMMEDIATE else self.memory[a]
            b_cmp = b if b_mode == ParamMode.IMMEDIATE else self.memory[b]
            self.memory[c] = 1 if a_cmp == b_cmp else 0
            self.pc += 4

        self.ops: Dict[int, Callable] = {
            1: op_add,
            2: op_mul,
            3: op_input,
            4: op_output,
            5: op_jit,
            6: op_jif,
            7: op_lt,
            8: op_eq,
            99: None
        }

    def run(self) -> None:
        while True:
            opcode_and_modes = self.memory[self.pc]

            opcode = opcode_and_modes % 100
            a_mode = (opcode_and_modes // 100) % 10
            b_mode = (opcode_and_modes // 1000) % 10
            c_mode = (opcode_and_modes // 10000) % 10

            try:
                op = self.ops[opcode]
            except KeyError:
                raise ValueError('invalid opcode: {}'.format(opcode))

            if op:
                # noinspection PyUnresolvedReferences
                num_params = op.__code__.co_argcount - 3
                params = self.memory[self.pc + 1:self.pc + num_params + 1]
                op(ParamMode(a_mode), ParamMode(b_mode), ParamMode(c_mode), *params)
            else:
                break


if __name__ == '__main__':
    with open('05_input.txt') as program:
        machine = IntcodeMachine(program.readline().strip())
        machine.run()
