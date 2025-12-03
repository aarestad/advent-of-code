def toggle_instruction(instruction):
    if len(instruction) == 2:
        if instruction[0] == "inc":
            return ["dec", instruction[1]]
        else:
            return ["inc", instruction[1]]
    if len(instruction) == 3:
        if instruction[0] == "jnz":
            return ["cpy"] + instruction[1:]
        else:
            return ["jnz"] + instruction[1:]

    raise ValueError("tried to toggle something unknown: " + instruction)


instructions = []

with open("input_25.txt") as insts:
    for i in insts:
        instructions.append(i.strip().split())


def run_program(init_a):
    regs = {"a": init_a, "b": 0, "c": 0, "d": 0}
    pc = 0
    output = ""

    while pc < len(instructions):
        inst = instructions[pc]

        if inst[0] == "cpy":
            if inst[2] in regs:  # do nothing if an invalid cpy
                if inst[1] in regs:  # register name
                    regs[inst[2]] = regs[inst[1]]
                else:  # immediate
                    regs[inst[2]] = int(inst[1])
            pc += 1
        elif inst[0] == "inc":
            if inst[1] in regs:
                regs[inst[1]] += 1
            pc += 1
        elif inst[0] == "dec":
            if inst[1] in regs:
                regs[inst[1]] -= 1
            pc += 1
        elif inst[0] == "jnz":
            if inst[1] in regs:
                do_jump = regs[inst[1]] != 0
            else:
                do_jump = int(inst[1]) != 0

            if do_jump:
                if inst[2] in regs:
                    pc += regs[inst[2]]
                elif inst[2] != "0":
                    pc += int(inst[2])
                else:
                    pc += 1
            else:
                pc += 1
        elif inst[0] == "tgl":
            if inst[1] in regs:
                inst_to_toggle = pc + regs[inst[1]]
            else:
                inst_to_toggle = pc + int(inst[1])

            if inst_to_toggle < len(instructions):
                instructions[inst_to_toggle] = toggle_instruction(
                    instructions[inst_to_toggle]
                )

            pc += 1
        elif inst[0] == "out":
            output += str(regs[inst[1]])

            if len(output) == 12:
                return output == "010101010101"
            pc += 1
        else:
            raise ValueError("tried to execute something unknown: " + inst)


for a in range(2**12):
    if a % 1000 == 0:
        print(a)
    if run_program(a):
        print(a)
        break
