import math


def binary_list_to_int(binary_list: list[int]) -> int:
    result = 0

    for idx, d in enumerate(binary_list):
        result |= d << (len(binary_list) - 1 - idx)

    return result


def get_subpackets(binary_list: list[int]) -> list[list[int]]:
    length_type = binary_list[6]

    if length_type:
        num_subpackets = binary_list_to_int(binary_list[1:12])
        rest_of_packet = binary_list[13:]
    else:
        subpacket_length = binary_list_to_int(binary_list[1:16])
        rest_of_packet = binary_list[16:]

    return []


def parse_packet(binary_list: list[int]) -> int:
    match packet_type := binary_list_to_int(binary_list[3:6]):
        case 0:
            print("sum packet")
            value = sum(parse_packet(packet) for packet in get_subpackets(binary_list))
        case 1:
            print("product packet")
            value = math.prod(
                parse_packet(packet) for packet in get_subpackets(binary_list)
            )
        case 2:
            print("min packet")
            value = min(parse_packet(packet) for packet in get_subpackets(binary_list))
        case 3:
            print("max packet")
            value = max(parse_packet(packet) for packet in get_subpackets(binary_list))
        case 4:
            print("literal packet")
            literal_value_binary_list = []
            current_start = 6
            not_last_group = 1

            while not_last_group:
                chunk = binary_list[current_start : current_start + 5]
                not_last_group = chunk[0]
                literal_value_binary_list.extend(chunk[1:])
                current_start += 5

            literal_value = binary_list_to_int(literal_value_binary_list)
            print(f"literal value: {literal_value}")
            value = literal_value
        case 5:
            print("gt packet")
            subpackets = get_subpackets(binary_list[6:])

            if len(subpackets) != 2:
                raise ValueError("gt packet has != 2 subpackets")

            left_value = parse_packet(subpackets[0])
            right_value = parse_packet(subpackets[1])
            value = 1 if left_value > right_value else 0
        case 6:
            print("lt packet")
            subpackets = get_subpackets(binary_list[6:])

            if len(subpackets) != 2:
                raise ValueError("lt packet has != 2 subpackets")

            left_value = parse_packet(subpackets[0])
            right_value = parse_packet(subpackets[1])
            value = 1 if left_value < right_value else 0
        case 7:
            print("eq packet")
            subpackets = get_subpackets(binary_list[6:])

            if len(subpackets) != 2:
                raise ValueError("eq packet has != 2 subpackets")

            left_value = parse_packet(subpackets[0])
            right_value = parse_packet(subpackets[1])
            value = 1 if left_value == right_value else 0
        case _:
            raise ValueError(f"bad packet type: {packet_type}")

    return value


if __name__ == "__main__":
    example = """C200B40A82"""

    example_input = example.split("\n")

    with open("input/day16.txt") as input:
        problem_input = [i.strip() for i in input.readlines()]

    decoded_input = [int(c, 16) for c in example_input[0]]

    decoded_bits = []

    for d in decoded_input:
        for n in range(3, -1, -1):
            decoded_bits.append(1 if (1 << n) & d else 0)

    print(parse_packet(decoded_bits))
