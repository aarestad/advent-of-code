#/usr/bin/python

# A house n gets 10 times the sum of its divisors
# so house 1 gets 10 * 1 = 10, house 6 gets 10 * (1+2+3+6) = 120

def divisors(n):
	divs = [1, n]

	for x in range (2, n/2 + 1):
		if n % x == 0:
			divs.append(x)

	return divs

max_sum = 0

for n in xrange(458640, 20000000):
	divs = divisors(n)
	sum_divisors = sum(divs)

	if sum_divisors > max_sum:
		print n, divs, sum_divisors
		max_sum = sum_divisors

	if sum_divisors >= 3310000: break
