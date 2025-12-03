total_area = 0
total_ribbon_length = 0

with open('input_2.txt') as input:
    for package in input:
        sides = sorted(int(s) for s in package.split('x'))

        side_1 = sides[0] * sides[1]
        side_2 = sides[0] * sides[2]
        side_3 = sides[1] * sides[2]
        volume = sides[0] * sides[1] * sides[2]
        total_area += 2 * (side_1 + side_2 + side_3) + min(side_1, side_2, side_3)
        total_ribbon_length += 2 * sides[0] + 2 * sides[1] + volume

print(total_area, 'sf of paper')
print(total_ribbon_length, 'f of ribbon')
