def knot_hash(input: bytearray, lengths: list[int]) -> str:
    lengths += [17, 31, 73, 47, 23]

    current_pos = 0
    skip_size = 0

    for _ in range(64):
        current_pos, skip_size, input_bytes = knot_hash_round(current_pos, skip_size, lengths, input)

def knot_hash_round(current_pos: int, skip_size: int, lengths: list[int], input: bytearray) -> tuple[int, int, bytearray]:
    input_len = len(input)

    for l in lengths:
        print(f'current_pos: {current_pos}, skip_size: {skip_size}, l: {l}')
        print(f'reversed:{list(reversed((input * 2)[current_pos:current_pos + l]))}')
        input[current_pos:current_pos + l] = reversed((input * 2)[current_pos:current_pos + l])

        if current_pos + l > input_len:
            input[0:(len(input) - input_len)] = input[input_len:]
            input = input[:input_len]

        current_pos = (current_pos + l + skip_size) % len(input)
        skip_size += 1

        print(input)

    return current_pos, skip_size, input

if __name__ == "__main__":
    example_input = "3,4,1,5"

    with open("input/day10.txt") as input:
        problem_input = "34,88,2,222,254,93,150,0,199,255,39,32,137,136,1,167"

        _, _, num_list = knot_hash_round(0, 0, [int(l) for l in example_input.split(",")], bytearray(range(5)))

        print(f"part 1: {num_list[0] * num_list[1]}")
