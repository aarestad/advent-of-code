def decompress_string(compressed):
    result = []

    in_marker = False
    in_repeat_num = False
    active_marker = None

    repeated_str = ''

    for c in compressed:
        if c == '(' and not active_marker:
            in_marker = True
            in_repeat_num = True
            active_marker = ['', '']
        elif in_marker and in_repeat_num and c != 'x':
            active_marker[0] += c  # digit
        elif in_marker and c == 'x':
            in_repeat_num = False
        elif in_marker and c != ')':
            active_marker[1] += c
        elif in_marker and c == ')':
            in_marker = False
            active_marker = [int(active_marker[0]), int(active_marker[1])]
        elif active_marker:
            repeated_str += c
            active_marker[0] -= 1

            if active_marker[0] == 0:
                for i in range(active_marker[1]):
                    result += repeated_str
                active_marker = None
                repeated_str = ''
        else:
            result += c

    return ''.join(result)


with open('input_9.txt') as compressed_input:
    compressed_lines = [s.strip() for s in compressed_input.readlines()]

total_len = 0

for line in compressed_lines:
    total_len += len(decompress_string(line))

print(total_len)
