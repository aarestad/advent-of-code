def binary_list_to_int(binary_list: list[int]) -> int:
    result = 0

    for idx, d in enumerate(binary_list):
        result |= d << (len(binary_list) - 1 - idx)

    return result


def parse_packet(binary_list: list[int]) -> int:
    version_number_sum = 0

    packet_version = binary_list_to_int(binary_list[0:3])
    packet_type = binary_list_to_int(binary_list[3:6])

    version_number_sum += packet_version

    match packet_type:
        case 4:
            literal_value_binary_list = []
            current_start = 6
            not_last_group = 1

            while not_last_group:
                chunk = binary_list[current_start:current_start+5]
                not_last_group = chunk[0]
                literal_value_binary_list.extend(chunk[1:])
                current_start += 5

            print(f"literal value: {binary_list_to_int(literal_value_binary_list)}")

            rest_of_packet = binary_list[current_start:]

            if len(rest_of_packet) >= 8 or not all(d == 0 for d in rest_of_packet):
                version_number_sum += parse_packet(rest_of_packet)
        case _:
            length_type = binary_list[6]

            if length_type:
                num_subpackets = binary_list_to_int(binary_list[7:18])
                version_number_sum += parse_packet(binary_list[18:])
            else:
                total_length = binary_list_to_int(binary_list[7:22])
                version_number_sum += parse_packet(binary_list[22:])

    return version_number_sum


if __name__ == "__main__":
    example = """C200B40A82"""

    example_input = example.split("\n")

    with open("input/day16.txt") as input:
        problem_input = [i.strip() for i in input.readlines()]

    decoded_input = [int(c, 16) for c in problem_input[0]]

    decoded_bits = []

    for d in decoded_input:
        for n in range(3, -1, -1):
            decoded_bits.append(1 if (1 << n) & d else 0)

    print(parse_packet(decoded_bits))
