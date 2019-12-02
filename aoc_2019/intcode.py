class IntcodeMachine:
    def __init__(self, program):
        self.memory = [int(x) for x in program.split(',')]
        self.pc = 0

    def run(self):
        while True:
            opcode = self.memory[self.pc]

            if opcode == 1:  # ADD
                result = self.memory[self.memory[self.pc + 1]] + self.memory[self.memory[self.pc + 2]]
                self.memory[self.memory[self.pc + 3]] = result
                self.pc += 4
            elif opcode == 2:  # MUL
                result = self.memory[self.memory[self.pc + 1]] * self.memory[self.memory[self.pc + 2]]
                self.memory[self.memory[self.pc + 3]] = result
                self.pc += 4
            elif opcode == 99:  # HALT
                break
            else:
                raise ValueError('invalid opcode: {}'.format(opcode))


if __name__ == '__main__':
    with open('02_input.txt') as program:
        intcode_machine = IntcodeMachine(program.readline().strip())

    intcode_machine.memory[1] = 12
    intcode_machine.memory[2] = 2
    intcode_machine.run()
    print(intcode_machine.memory[0])
