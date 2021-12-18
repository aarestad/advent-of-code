import math


def binary_list_to_int(binary_list: list[int]) -> int:
    result = 0

    for idx, d in enumerate(binary_list):
        result |= d << (len(binary_list) - 1 - idx)

    return result


def parse_packet(binary_list: list[int]) -> (int, int, list[int]):
    packet_version = binary_list_to_int(binary_list[0:3])
    packet_type = binary_list_to_int(binary_list[3:6])

    if packet_type == 4:
        literal_value_binary_list = []
        current_start = 6
        not_last_group = 1

        while not_last_group:
            chunk = binary_list[current_start : current_start + 5]
            not_last_group = chunk[0]
            literal_value_binary_list.extend(chunk[1:])
            current_start += 5

        packet_value = binary_list_to_int(literal_value_binary_list)
        rest_of_packet = binary_list[current_start:]
    else:
        subpacket_values = []

        length_type = binary_list[6]

        if length_type:
            num_subpackets = binary_list_to_int(binary_list[7:18])
            rest_of_packet = binary_list[18:]

            for _ in range(num_subpackets):
                pver, pval, rest_of_packet = parse_packet(rest_of_packet)
                packet_version += pver
                subpacket_values.append(pval)
        else:
            subpacket_length = binary_list_to_int(binary_list[7:22])
            rest_of_packet = binary_list[22:]
            original_length = len(rest_of_packet)

            while original_length - len(rest_of_packet) < subpacket_length:
                pver, pval, rest_of_packet = parse_packet(rest_of_packet)
                packet_version += pver
                subpacket_values.append(pval)

        match packet_type:
            case 0:
                packet_value = sum(subpacket_values)
            case 1:
                packet_value = math.prod(subpacket_values)
            case 2:
                packet_value = min(subpacket_values)
            case 3:
                packet_value = max(subpacket_values)
            case 5:
                packet_value = subpacket_values[0] > subpacket_values[1]
            case 6:
                packet_value = subpacket_values[0] < subpacket_values[1]
            case 7:
                packet_value = subpacket_values[0] == subpacket_values[1]
            case _:
                raise ValueError(f"bad packet type: {packet_type}")

    return packet_version, packet_value, rest_of_packet


if __name__ == "__main__":
    example = """A0016C880162017C3686B18A3D4780"""

    example_input = example.split("\n")

    with open("input/day16.txt") as input:
        problem_input = [i.strip() for i in input.readlines()]

    decoded_input = [int(c, 16) for c in problem_input[0]]

    decoded_bits = []

    for d in decoded_input:
        for n in range(3, -1, -1):
            decoded_bits.append(1 if (1 << n) & d else 0)

    packet_version, packet_value, _ = parse_packet(decoded_bits)
    print(f"packet version = {packet_version}")
    print(f"packet value = {packet_value}")
