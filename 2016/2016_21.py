import re

swap_pos = re.compile(r'swap position (\d+) with position (\d+)')
swap_letters = re.compile(r'swap letter (\w) with letter (\w)')
rotate_steps = re.compile(r'rotate (left|right) (\d+) steps')
rotate_pos = re.compile(r'rotate based on position of letter (\w)')
reverse_range = re.compile(r'reverse positions (\d) through (\d)')
move_letter = re.compile(r'move position (\d) to position (\d)')

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

with open('input_21.txt') as command_file:
    commands = [c.strip() for c in command_file.readlines()]

for command in commands:
    m = swap_pos.match(command)

    if m:
        tmp = letters[int(m.group(1))]
        letters[int(m.group(1))] = letters[int(m.group(2))]
        letters[int(m.group(2))] = tmp
        continue

    m = swap_letters.match(command)

    if m:
        l1 = m.group(1)
        l2 = m.group(2)