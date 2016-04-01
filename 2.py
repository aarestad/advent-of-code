total_area = 0
total_ribbon_length = 0

with open('input_2.txt') as input:
  for package in input:
    dims = package.split('x')
    l, w, h = map(int, dims)

    smallest_side = min(l, w, h)
    other_sides = [l, w, h]
    other_sides.remove(smallest_side)
    second_smallest_side = min(*other_sides)
    side_1 = l*w
    side_2 = l*h
    side_3 = w*h
    volume = l*w*h
    total_area += 2*(side_1 + side_2 + side_3) + min(side_1, side_2, side_3)
    total_ribbon_length += 2 *smallest_side + 2*second_smallest_side + volume

print total_area, 'sf of paper'
print total_ribbon_length, 'f of ribbon'
