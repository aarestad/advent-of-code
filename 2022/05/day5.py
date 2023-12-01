import re

if __name__ == "__main__":
    example = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

    example_input = example.split("\n")

    with open("input/day5.txt") as input:
        problem_input = [i.rstrip() for i in input.readlines()]

    actual_input = problem_input

    num_stacks = (len(actual_input[0]) + 1) // 4

    stacks = []

    for _ in range(num_stacks):
        stacks.append([])

    highest_stack = 8  # barf :)

    stack_lines = actual_input[0:highest_stack]

    for line in stack_lines:
        for s in range(len(stacks)):
            crate = line[s * 4 + 1]
            if crate != " ":
                stacks[s].append(crate)

    # deep copy for part 2
    part_2_stacks = []
    for s in stacks:
        part_2_stacks.append(s[:])

    instructions = actual_input[highest_stack + 2 :]
    instruction_matcher = re.compile(r"move (\d+) from (\d) to (\d)")

    for line in instructions:
        instruction_match = instruction_matcher.search(line)

        (num_to_move, target_stack, dest_stack) = (
            int(g) for g in instruction_match.groups()
        )

        for _ in range(num_to_move):
            crate = stacks[target_stack - 1].pop(0)
            stacks[dest_stack - 1].insert(0, crate)

        chunk_to_move = part_2_stacks[target_stack - 1][0:num_to_move]
        del part_2_stacks[target_stack - 1][0:num_to_move]
        part_2_stacks[dest_stack - 1] = chunk_to_move + part_2_stacks[dest_stack - 1]

    print("part 1:", "".join(s[0] for s in stacks))
    print("part 2:", "".join(s[0] for s in part_2_stacks))
