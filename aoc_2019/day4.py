def has_two_same_adjacent_digits(n):
    prev_digit = -1

    while n > 0:
        next_digit = n % 10

        if next_digit == prev_digit:
            return True

        prev_digit = next_digit
        n //= 10

    return False


def has_a_discrete_pair_of_digits(n):
    prev_digit = -1
    num_seen = 0

    while n > 0:
        next_digit = n % 10

        if next_digit == prev_digit:
            num_seen += 1
        else:
            if num_seen == 2:
                return True
            num_seen = 1

        prev_digit = next_digit
        n //= 10

    return num_seen == 2


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


if __name__ == '__main__':
    print(len([pw for pw in range(240920, 789858) if is_good_password(pw)]))
