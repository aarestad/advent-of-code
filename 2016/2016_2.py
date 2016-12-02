def solve_part_1(lines):
    code = []

    current_pos = 5

    for line in lines:
        for char in line:
            if char == 'U' and current_pos > 3:
                current_pos -= 3
            elif char == 'D' and current_pos < 7:
                current_pos += 3
            elif char == 'L' and current_pos not in {1, 4, 7}:
                current_pos -= 1
            elif char == 'R' and current_pos not in {3, 6, 9}:
                current_pos += 1

        code.append(current_pos)

    return code

def solve_part_2(lines):
    code = []

    current_pos = 5

    for line in lines:
        for char in line.strip():
            print("move %s, %s->" % (char, current_pos), end=" ")

            if char == 'U' and current_pos not in {1, 2, 4, 5, 9}:
                current_pos -= 2 if current_pos in {3, 13} else 4
            elif char == 'D' and current_pos not in {5, 9, 10, 12, 13}:
                current_pos += 2 if current_pos in {1, 11} else 4
            elif char == 'L' and current_pos not in {1, 2, 5, 10, 13}:
                current_pos -= 1
            elif char == 'R' and current_pos not in {1, 4, 9, 12, 13}:
                current_pos += 1

            print(current_pos)

        print("stopping at %s" % current_pos)
        code.append(current_pos)

    return code

sample = ["ULL", "RRDDD", "LURDL", "UUUUD"]

print(solve_part_1(sample))
print(solve_part_2(sample))

with open('input_2.txt') as problem_input:
    lines = problem_input.readlines()
    print(solve_part_1(lines))
    print(solve_part_2(lines))
