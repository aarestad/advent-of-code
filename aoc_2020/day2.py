import re

password_parser = re.compile(r'(\d+)-(\d+) (\w): (\w+)')

if __name__ == '__main__':
    num_good_passwords = 0

    with open('input/day2.txt') as password_file:
        for line in password_file:
            pw_match = password_parser.match(line)
            (char_one, char_two, char, password) = pw_match.groups()

            # day 1:
            # char_count = sum(1 for c in password if c == char)
            #
            # if char_one <= char_count <= char_two:
            #     num_good_passwords += 1
            if (password[int(char_one) - 1] == char) ^ (password[int(char_two) - 1] == char):
                num_good_passwords += 1

    print(num_good_passwords)
