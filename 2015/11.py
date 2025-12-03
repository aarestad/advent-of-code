ord_of_a = ord("a")
ord_of_z = ord("z")


def increment_password(pw):
    pw_chars = list(map(ord, pw))

    i = len(pw_chars) - 1

    while True:
        pw_chars[i] += 1
        if pw_chars[i] > ord_of_z:
            pw_chars[i] = ord_of_a
            i -= 1

            if i < 0:  # we have a big ol' string of 'a's at this point
                return "a" + "".join(map(chr, pw_chars))
        else:
            return "".join(map(chr, pw_chars))


def password_valid(pw):
    return (
        contains_ascending_sequence(pw)
        and not contains_forbidden_letter(pw)
        and contains_two_repeating_pairs_of_letters(pw)
    )


def contains_ascending_sequence(pw):
    # - Passwords must include one increasing straight of at least
    # three letters, like abc, bcd, cde, and so on, up to xyz.
    # They cannot skip letters; abd doesn't count.
    for i in range(len(pw) - 2):
        if ord(pw[i]) + 1 == ord(pw[i + 1]) and ord(pw[i]) + 2 == ord(pw[i + 2]):
            return True
    return False


def contains_forbidden_letter(pw):
    # - Passwords may not contain the letters i, o, or l, as these letters can be
    # mistaken for other characters and are therefore confusing.
    import re

    return re.search("i|o|l", pw) is not None


def contains_two_repeating_pairs_of_letters(pw):
    # - Passwords must contain at least two different, non-overlapping pairs of
    # letters, like aa, bb, or zz.
    import re

    letter_pair_matcher = re.compile(r"(.)\1")

    first_pair_match = letter_pair_matcher.search(pw)

    if not first_pair_match:
        return False

    return letter_pair_matcher.search(pw, first_pair_match.end()) is not None


original_password = "hepxxzaa"

while not password_valid(original_password):
    original_password = increment_password(original_password)

print(original_password)
