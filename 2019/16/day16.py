def calculated_pattern(pos: int):
    base_pattern = [0, 1, 0, -1]

    current_idx = 0
    count = 0

    while True:
        count += 1

        if count >= pos:
            count = 0
            current_idx += 1
            current_idx %= 4

        yield base_pattern[current_idx]


if __name__ == '__main__':
    input_signal = '69317163492948606335995924319873' * 10_000
    # with open('16_input.txt') as input_16:
    #     input_signal = input_16.readline().strip() * 10_000

    offset = int(input_signal[:7])

    for _ in range(100):
        next_signal = ''

        for pos in range(1, len(input_signal) + 1):
            print(pos)

            next_digit = 0

            pattern = calculated_pattern(pos)
            mulitiplicands = []

            for digit in input_signal:
                next_multiplicand = next(pattern)
                mulitiplicands.append(next_multiplicand)
                next_digit += int(digit) * next_multiplicand

            next_signal += str(next_digit)[-1]
            # print(mulitiplicands)

        print(f'iteration {_} complete')
        input_signal = next_signal

    print(input_signal[offset:offset+8])
