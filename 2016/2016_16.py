def calculate_checksum(s):
    if len(s) % 2 != 0:
        raise ValueError("can't take the checksum of an odd-length bitstring")

    i = 0

    checksum = ''

    while i < len(s):
        if s[i:i+2] == '00' or s[i:i+2] == '11':
            checksum += '1'
        else:
            checksum += '0'
        i += 2

    if len(checksum) % 2 != 0:
        return checksum

    return calculate_checksum(checksum)


def dragon_curve(s):
    a = s
    a_rev = a[::-1]

    b = ''

    for c in a_rev:
        if c == '1':
            b += '0'
        else:
            b += '1'

    return a + '0' + b

#required_len = 272
required_len = 35651584

overwrite_str = '01111010110010011'

while len(overwrite_str) < required_len:
    overwrite_str = dragon_curve(overwrite_str)

overwrite_str = overwrite_str[:required_len]

print(calculate_checksum(overwrite_str))
