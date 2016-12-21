import math

target_number = 3310000


def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n % 2 == 0: return False
    if n < 9: return True
    if n % 3 == 0: return False
    r = int(n ** 0.5)
    f = 5
    while f <= r:
        if n % f == 0: return False
        if n % (f + 2) == 0: return False
        f += 6
    return True


def primes():
    yield 2
    p = 3
    while True:
        yield p
        p += 2
        while not is_prime(p): p += 2


def prime_factors(n, primes=primes()):
    factors = []
    for p in primes:
        if p * p > n: break
        i = 0
        while n % p == 0:
            n //= p
            i += 1
        if i > 0:
            factors.append((p, i));
    if n > 1: factors.append((n, 1))
    return factors


def divisor_sum_prime_power(p, a):
    return (p ** (a + 1) - 1) / (p - 1)


def divisor_sum(n):
    if n % 1000 == 0: print
    n
    dsum = 1
    for f in prime_factors(n):
        dsum *= divisor_sum_prime_power(*f)
    return dsum


for n in range(1, 100):
    dsum = divisor_sum(n)
    print
    n, dsum

    if dsum >= target_number:
        break


# /usr/bin/python

# A house n gets 10 times the sum of its divisors
# so house 1 gets 10 * 1 = 10, house 6 gets 10 * (1+2+3+6) = 120

def divisors(n):
    divs = [1, n]

    for x in range(2, n / 2 + 1):
        if n % x == 0:
            divs.append(x)

    return divs


max_sum = 0

for n in xrange(458640, 20000000):
    divs = divisors(n)
    sum_divisors = sum(divs)

    if sum_divisors > max_sum:
        print
        n, divs, sum_divisors
        max_sum = sum_divisors

    if sum_divisors >= 3310000: break
