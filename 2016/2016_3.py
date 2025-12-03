def solve_part_one(triangles):
    num_possible_triangles = 0

    for triangle in triangles:
        triangle.sort()

        if triangle[0] + triangle[1] > triangle[2]:
            num_possible_triangles += 1

    return num_possible_triangles


# part 1
# with open('input_3.txt') as triangles:
#     triangles_parsed = []
#
#     for line in triangles:
#         triangles_parsed.append([int(s) for s in line.split()])
#
#     print(solve_part_one(triangles_parsed))

# part 2
with open("input_3.txt") as triangle_cols:
    triangles_parsed = []

    t1 = []
    t2 = []
    t3 = []

    for line in triangle_cols:
        nums = [int(s) for s in line.split()]
        t1.append(nums[0])
        t2.append(nums[1])
        t3.append(nums[2])

        if len(t1) == 3:
            triangles_parsed.append(t1)
            triangles_parsed.append(t2)
            triangles_parsed.append(t3)

            t1 = []
            t2 = []
            t3 = []

    print(triangles_parsed)

print(solve_part_one(triangles_parsed))
