depths = [int(line.strip()) for line in open("input/day1.txt")]

raw_increases = 0
window_increases = 0
prev_values = ()

for depth in depths:
    if len(prev_values) > 0 and depth > prev_values[-1]:
        raw_increases += 1

    if len(prev_values) == 3 and sum(prev_values[1:]) + depth > sum(prev_values):
        window_increases += 1

    prev_values = (prev_values if len(prev_values) < 3 else prev_values[1:]) + (depth,)

print(raw_increases)
print(window_increases)
