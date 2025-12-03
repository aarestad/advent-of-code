# GRID_SIZE = 100
#
# def lights_iteration(orig_lights):
# 	new_light_row = [False] * GRID_SIZE
#
# 	new_lights = []
#
# 	for _ in range(GRID_SIZE):
# 		new_lights.append(new_light_row[:])
#
# 	for row in range(GRID_SIZE):
# 		for col in range(GRID_SIZE):
# 			neighbors_on = sum((xx, yy) in lights_on for xx in range(x - 1, x + 2) for yy in range(y - 1, y + 2) if (xx, yy) != (x, y))
#
# 			if orig_lights[row][col]:
# 				new_lights[row][col] = (neighbors_on == 2 or neighbors_on == 3)
# 			else:
# 				new_lights[row][col] = neighbors_on == 3
#
# 	return new_lights
#
# light_row = [False] * GRID_SIZE
#
# lights = []
#
# for _ in range(GRID_SIZE):
# 	lights.append(light_row[:])
#
# with open('input_18.txt') as light_rows:
# 	for row, light_row in enumerate(light_rows):
# 		for col, c in enumerate(light_row.strip()):
# 			if c == '#': lights[row][col] = True
#
# for _ in range(100):
# 	lights = lights_iteration(lights)
#
# lights_on = 0
#
# for row in range(GRID_SIZE):
# 	for col in range(GRID_SIZE):
# 		if lights[row][col]: lights_on += 1
#
# print(lights_on)
# !/usr/bin/env python

# !/usr/bin/env python

# Advent of Code 2015
#
# Day 18: Like a GIF For Your Yard
#
# Giacomo Boccardo 2015

steps = 100
grid_width = 100
grid_height = 100


def evaluate_lights_on(lights_always_on):
    with open('input_18.txt') as f:
        lights_on = {(x, y) for y, line in enumerate(f) for x, char in enumerate(line.strip()) if '#' == char}
        lights_on |= lights_always_on

    def count_neighbors_on(x, y):
        return sum((xx, yy) in lights_on for xx in range(x - 1, x + 2) for yy in range(y - 1, y + 2) if (xx, yy) != (x, y))

    for _ in range(steps):
        lights_on = {(x, y) for x in range(grid_width) for y in range(grid_height)
                     if
                     (x, y) in lights_on and count_neighbors_on(x, y) in (2, 3)
                     or
                     (x, y) not in lights_on and count_neighbors_on(x, y) == 3}
        lights_on |= lights_always_on

    return lights_on


print("Part 1: %d" % len(evaluate_lights_on(set())))
# 821

corners_always_on = {(0, 0), (0, 99), (99, 0), (99, 99)}
print("Part 2: %d" % len(evaluate_lights_on(corners_always_on)))
# 886
