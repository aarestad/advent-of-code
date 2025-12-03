class Instruction(object):
    def __init__(self, name, arg1, arg2=None):
        self.name = name
        self.arg1 = arg1
        self.arg2 = arg2


instructions = []

with open("input_23.txt") as instlist:
    for inst in instlist:
        instructions.append(Instruction(*inst.strip().split()))

regs = {"a": 1, "b": 0}
pc = 0

while pc < len(instructions):
    curr_inst = instructions[pc]

    if curr_inst.name == "hlf":
        regs[curr_inst.arg1] /= 2
        pc += 1
    elif curr_inst.name == "tpl":
        regs[curr_inst.arg1] *= 3
        pc += 1
    elif curr_inst.name == "inc":
        regs[curr_inst.arg1] += 1
        pc += 1
    elif curr_inst.name == "jmp":
        pc += int(curr_inst.arg1)
    elif curr_inst.name == "jie":
        if regs[curr_inst.arg1[0]] % 2 == 0:
            pc += int(curr_inst.arg2)
        else:
            pc += 1
    elif curr_inst.name == "jio":
        if regs[curr_inst.arg1[0]] == 1:
            pc += int(curr_inst.arg2)
        else:
            pc += 1

print(regs)
