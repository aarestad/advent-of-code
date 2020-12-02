import re

password_parser = re.compile(r'(\d+)-(\d+) (\w): (\w+)')


if __name__ == '__main__':
    num_good_passwords = 0

    with open('input/day2.txt') as password_file:
        for line in password_file:
            pw_match = password_parser.match(line)

            char = pw_match[3]
            char_one = int(pw_match[1])
            char_two = int(pw_match[2])
            password = pw_match[4]

            # day 1:
            # char_count = sum(1 for c in password if c == char)
            #
            # if min_chars <= char_count <= max_chars:
            #     num_good_passwords += 1
            if (password[char_one-1] == char) ^ (password[char_two-1] == char):
                num_good_passwords += 1

    print(num_good_passwords)
