import re

has_two_same_adjacent_digits_re = re.compile(r"(\d)\1")
has_a_discrete_pair_of_digits_re = re.compile(
    "|".join("((?<!{}){}{}(?!{}))".format(n, n, n, n) for n in range(10))
)


def has_two_same_adjacent_digits(n):
    return has_two_same_adjacent_digits_re.search(str(n))


def has_a_discrete_pair_of_digits(n):
    return has_a_discrete_pair_of_digits_re.search(str(n))


def digits_do_not_decrease(n):
    prev_digit = 10

    while n > 0:
        next_digit = n % 10

        if next_digit > prev_digit:
            return False

        prev_digit = next_digit
        n //= 10

    return True


def is_good_password(pw):
    return has_a_discrete_pair_of_digits(pw) and digits_do_not_decrease(pw)


if __name__ == "__main__":
    print(len([pw for pw in range(240920, 789858) if is_good_password(pw)]))
