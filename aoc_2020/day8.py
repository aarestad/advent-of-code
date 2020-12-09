from enum import Enum


class Oper(Enum):
    NOP = "nop"
    ACC = "acc"
    JMP = "jmp"


if __name__ == "__main__":
    program = []

    with open("input/day8.txt") as code_list:
        for oper in code_list:
            split_oper = oper.strip().split()
            program.append([Oper(split_oper[0]), int(split_oper[1])])

    mutator_index = 0

    for mutator_index in range(len(program)):
        if program[mutator_index][0] == Oper.ACC:
            continue

        # deep copy of program
        program_copy = [oper[:] for oper in program]

        program_copy[mutator_index][0] = (
            Oper.NOP if program_copy[mutator_index][0] == Oper.JMP else Oper.JMP
        )

        accumulator = 0
        pc = 0

        executed_instructions = set()

        while pc not in executed_instructions:
            if pc == len(program):
                print(accumulator)
                exit()

            executed_instructions.add(pc)
            oper = program_copy[pc]

            if oper[0] == Oper.ACC:
                accumulator += oper[1]
                pc += 1
            elif oper[0] == Oper.JMP:
                pc += oper[1]
            elif oper[0] == Oper.NOP:
                pc += 1
