num_elves = 3001330
# num_elves = 5

elves = [None] * num_elves

for i in range(num_elves):
    elves[i] = i + 1

i = 0

while len(elves) > 1:
    if len(elves) % 100 == 0:
        print("%d left" % len(elves))

    if len(elves) % 2 == 0:
        across = (i + len(elves) // 2) % len(elves)
    else:
        across = (i + (len(elves) - 1) // 2) % len(elves)

    # print(across)

    del elves[across]

    i += 1
    if i >= len(elves):
        i = 0

print(elves)
