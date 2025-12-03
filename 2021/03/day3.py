example = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""


gamma_rate = ""
epsilon_rate = ""

# diags = example.split("\n")

diags = []

with open("input/day3.txt") as input:
    for diag in input:
        diags.append(diag.strip())

bits = len(diags[0])

for i in range(bits):
    digits = [diag[i] for diag in diags]
    num_ones = sum(1 for d in digits if d == "1")

    if num_ones > len(digits) / 2:
        gamma_rate += "1"
        epsilon_rate += "0"
    else:
        gamma_rate += "0"
        epsilon_rate += "1"

print(int(gamma_rate, 2) * int(epsilon_rate, 2))

o2_prefix = ""

for i in range(bits):
    o2_diags = [diag for diag in diags if diag.startswith(o2_prefix)]
    num_diags = len(o2_diags)

    if num_diags == 1:
        o2_prefix = o2_diags[0]
        break

    num_ones = sum(1 for d in (diag[i] for diag in o2_diags) if d == "1")

    if num_ones >= num_diags / 2:
        o2_prefix += "1"
    else:
        o2_prefix += "0"

o2_gen = int(o2_prefix, 2)

co2_prefix = ""

for i in range(bits):
    co2_diags = [diag for diag in diags if diag.startswith(co2_prefix)]
    num_diags = len(co2_diags)

    if num_diags == 1:
        co2_prefix = co2_diags[0]
        break

    num_ones = sum(1 for d in (diag[i] for diag in co2_diags) if d == "1")

    if num_ones < num_diags / 2:
        co2_prefix += "1"
    else:
        co2_prefix += "0"

co2_scrub = int(co2_prefix, 2)

print(o2_gen * co2_scrub)
