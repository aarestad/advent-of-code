from typing import NamedTuple, Callable, Dict, List


class IntcodeOp(NamedTuple):
    params: int
    op: Callable[[int, int], int]


class IntcodeMachine:
    def __init__(self, program: str):
        self.memory: List[int] = [int(x) for x in program.split(',')]
        self.pc: int = 0

        self.ops: Dict[int, IntcodeOp] = {
            1: IntcodeOp(3, lambda a, b: self.memory[a] + self.memory[b]),  # ADD a, b, dest
            2: IntcodeOp(3, lambda a, b: self.memory[a] * self.memory[b]),  # MUL a, b, dest
            99: None  # HLT
        }

    def run(self) -> None:
        while True:
            opcode = self.memory[self.pc]

            try:
                op = self.ops[opcode]
            except KeyError:
                raise ValueError('invalid opcode: {}'.format(opcode))

            if op:
                params = self.memory[self.pc + 1:self.pc + op.params + 1]
                result = op.op(*params[0:2])
                self.memory[params[2]] = result
                self.pc += 1 + len(params)
            else:
                break


if __name__ == '__main__':
    with open('02_input.txt') as program:
        program_text = program.readline().strip()

    for noun in range(100):
        for verb in range(100):
            intcode_machine = IntcodeMachine(program_text)

            intcode_machine.memory[1] = noun
            intcode_machine.memory[2] = verb
            intcode_machine.run()

            result = intcode_machine.memory[0]

            if result == 19690720:
                print(100 * noun + verb)
                break
        else:
            continue

        break
