def decompress_string(compressed):
    result = []

    in_marker = False
    in_repeat_num = False
    active_marker = None

    repeated_str = ""

    for c in compressed:
        if c == "(" and not active_marker:
            in_marker = True
            in_repeat_num = True
            active_marker = ["", ""]
        elif in_marker and in_repeat_num and c != "x":
            active_marker[0] += c  # digit
        elif in_marker and c == "x":
            in_repeat_num = False
        elif in_marker and c != ")":
            active_marker[1] += c
        elif in_marker and c == ")":
            in_marker = False
            active_marker = [int(active_marker[0]), int(active_marker[1])]
        elif active_marker:
            repeated_str += c
            active_marker[0] -= 1

            if active_marker[0] == 0:
                for _ in range(active_marker[1]):
                    result += repeated_str
                active_marker = None
                repeated_str = ""
        else:
            result += c

    return "".join(result)


class RepeatedUnit:
    def __init__(self, times, string):
        self.times = times
        self.string = string

    def __repr__(self):
        return "('%s' x %s)" % (self.string, self.times)

    def __str__(self):
        return self.__repr__()

    def unit_length(self):
        return len(self.string) * self.times


def decompressed_len_v2(unit):
    sub_units = []

    in_marker = False
    in_repeat_num = False
    active_marker = None

    i = 0

    if "(" not in unit.string:
        return unit.unit_length()

    while i < len(unit.string):
        c = unit.string[i]

        if c == "(" and not active_marker:
            in_marker = True
            in_repeat_num = True
            active_marker = ["", ""]  # len, num_repeats
            i += 1
        elif in_marker and in_repeat_num and c != "x":
            active_marker[0] += c  # digit
            i += 1
        elif in_marker and c == "x":
            in_repeat_num = False
            i += 1
        elif in_marker and c != ")":
            active_marker[1] += c
            i += 1
        elif in_marker and c == ")":
            in_marker = False
            active_marker = [int(active_marker[0]), int(active_marker[1])]
            i += 1
        elif active_marker:
            sub_units.append(
                RepeatedUnit(active_marker[1], unit.string[i : i + active_marker[0]])
            )
            i += active_marker[0]
            active_marker = None
        else:
            # no active marker, and not processing marker - singleton string
            singleton_end = i + 1

            while (
                singleton_end < len(unit.string) and unit.string[singleton_end] != "("
            ):
                singleton_end += 1

            sub_units.append(RepeatedUnit(1, unit.string[i:singleton_end]))
            i = singleton_end

    result = 0

    for u in sub_units:
        result += decompressed_len_v2(u)

    return result * unit.times


with open("input_9.txt") as compressed_input:
    compressed_line = compressed_input.readline().strip()


# print(len(decompress_string(compressed_line)))

print(decompressed_len_v2(RepeatedUnit(1, "(3x3)XYZ")))
print(decompressed_len_v2(RepeatedUnit(1, "X(8x2)(3x3)ABCY")))
print(decompressed_len_v2(RepeatedUnit(1, "(27x12)(20x12)(13x14)(7x10)(1x12)A")))
print(
    decompressed_len_v2(
        RepeatedUnit(1, "(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN")
    )
)
print(decompressed_len_v2(RepeatedUnit(1, compressed_line)))

# part 2:
# - (3x3)XYZ still becomes XYZXYZXYZ, as the decompressed section contains no markers.
# - X(8x2)(3x3)ABCY becomes XABCABCABCABCABCABCY, because the decompressed data from the (8x2) marker
#   is then further decompressed, thus triggering the (3x3) marker twice for a total of six ABC sequences.
# - (27x12)(20x12)(13x14)(7x10)(1x12)A decompresses into a string of A repeated 241920 times.
# - (25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN becomes 445 characters long.
