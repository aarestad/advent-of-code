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

o2_diags = diags[:]

for i in range(bits):
    if len(o2_diags) == 1:
        break

    digits = [diag[i] for diag in o2_diags]
    num_ones = sum(1 for d in digits if d == "1")

    if num_ones >= len(digits) / 2:
        o2_diags = [d for d in o2_diags if d[i] == "1"]
    else:
        o2_diags = [d for d in o2_diags if d[i] == "0"]

o2_gen = int(o2_diags[0], 2)

co2_diags = diags[:]

for i in range(bits):
    if len(co2_diags) == 1:
        break

    digits = [diag[i] for diag in co2_diags]
    num_ones = sum(1 for d in digits if d == "1")

    if num_ones < len(digits) / 2:
        co2_diags = [d for d in co2_diags if d[i] == "1"]
    else:
        co2_diags = [d for d in co2_diags if d[i] == "0"]

co2_scrub = int(co2_diags[0], 2)

print(o2_gen * co2_scrub)
