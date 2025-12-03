from operator import itemgetter

def solve(lines, reverse):
    letter_counts = [None] * 8

    for line in lines:
        idx = 0

        for c in line.strip():
            if letter_counts[idx] is None:
                letter_counts[idx] = {c: 1}
            elif c in letter_counts[idx]:
                letter_counts[idx][c] += 1
            else:
                letter_counts[idx][c] = 1
            idx += 1

    message = []

    for counter in letter_counts:
        message.append(sorted(counter.items(), key=itemgetter(1), reverse=reverse)[0][0])

    return ''.join(message)

with open('input_6.txt') as lines:
    message_lines = lines.readlines()

print(solve(message_lines, True)) # part 1
print(solve(message_lines, False)) # part 2
