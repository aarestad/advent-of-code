class IntcodeMachine:
    def __init__(self, program):
        self.memory = [int(x) for x in program.split(',')]
        self.pc = 0
        self.ops = {
            1: {  # ADD a, b, dest
                'params': 3,
                'op': lambda x, y: self.memory[x] + self.memory[y]
            },
            2: {  # MUL a, b, dest
                'params': 3,
                'op': lambda x, y: self.memory[x] * self.memory[y]
            },
            99: None  # HLT
        }

    def run(self):
        while True:
            opcode = self.memory[self.pc]

            try:
                op = self.ops[opcode]
            except KeyError:
                raise ValueError('invalid opcode: {}'.format(opcode))

            if op:
                params = self.memory[self.pc + 1:self.pc + op['params'] + 1]
                result = op['op'](*params[0:2])
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
