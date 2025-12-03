regs = {"a": 0, "b": 0, "c": 1, "d": 0}

pc = 0

instructions = []

with open("input_12.txt") as insts:
    for i in insts:
        instructions.append(i.strip().split())

while pc < len(instructions):
    inst = instructions[pc]

    if inst[0] == "cpy":
        if inst[1] in regs:  # register name
            regs[inst[2]] = regs[inst[1]]
        else:  # immediate
            regs[inst[2]] = int(inst[1])
        pc += 1
    elif inst[0] == "inc":
        regs[inst[1]] += 1
        pc += 1
    elif inst[0] == "dec":
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
            else:
                pc += int(inst[2])
        else:
            pc += 1
    else:
        raise Error("unknown: " + inst)

print(regs)
