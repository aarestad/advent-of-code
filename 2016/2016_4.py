import re
from operator import itemgetter

number_finder = re.compile(r'\d+')
encrypted_name_finder = re.compile(r'^\D+')
checksum_finder = re.compile(r'\[(\w+)\]')

def sort_char_counts(a, b):
    if a[1] != b[1]:
        return (a[1] > b[1]) - (a[1] < b[1])


def check_room_checksum(encrypted_name_with_checksum):
    char_counter = {}

    checksum_chars = list(checksum_finder.search(encrypted_name_with_checksum).group(1))
    encrypted_name = encrypted_name_finder.search(encrypted_name_with_checksum).group(0)
    room_number = number_finder.search(encrypted_name_with_checksum).group(0)

    for c in encrypted_name.replace('-', ''):
        if c in char_counter:
            char_counter[c] += 1
        else:
            char_counter[c] = 1

    top_5 = sorted(sorted(char_counter.items(), key=itemgetter(0)), key=itemgetter(1), reverse=True)[:5]

    for count in top_5:
        if count[0] not in checksum_chars:
            return ''
        checksum_chars.remove(count[0])

    key = int(room_number) % 26

    decrypted_name = []

    for c in encrypted_name:
        if c == '-':
            decrypted_name.append(' ')
        else:
            decrypted = ord(c) + key

            if (decrypted > ord('z')):
                decrypted -= 26

            decrypted_name.append(chr(decrypted))

    return "%s %s" % (room_number, ''.join(decrypted_name))

with open('input_4.txt') as rooms:
    for room in rooms:
        room_name = check_room_checksum(room.strip())
        if room_name != '': print(room_name)
