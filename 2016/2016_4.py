import re

number_finder = re.compile(r'\d+')
encrypted_name_finder = re.compile(r'\D+')

def check_room_checksum(encrypted_name_with_checksum):
    char_counter = {}

    checksum_chars = sorted(encrypted_name[-6:-1])
    encrypted_name = encrypted_name_finder.search(encrypted_name_with_checksum).group(0)

    for c in encrypted_name.replace('-', ''):
        if c in char_counter:
            char_counter[c] += 1
        else:
            char_counter[c] = 1
