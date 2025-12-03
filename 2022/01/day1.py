test_input = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""

with open("day1.txt") as inp:
    input = inp.read()

calorie_counts = [0]

current_elf = 0

for line in input.split("\n"):
    if line == "":
        calorie_counts.append(0)
        current_elf += 1
        continue
    calorie_counts[current_elf] += int(line.strip())

sorted_calories = sorted(calorie_counts, reverse=True)
print(sorted_calories[0])
print(sum(sorted_calories[0:3]))
