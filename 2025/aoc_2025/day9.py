def part1(input):
    best_area = 0
    
    for i, p1_str in enumerate(input):
        p1 = tuple(int(c) for c in p1_str.split(","))

        for p2_str in input[i+1:]:
            p2 = tuple(int(c) for c in p2_str.split(","))
            area = (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)

            if area > best_area:
                best_area = area
    
    return best_area

if __name__ == "__main__":
    example = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3"""

    example_input = example.split("\n")
    # print(part1(example_input))

    with open("input/day9.txt") as input:
        problem_input = [i.strip() for i in input.readlines()]
        print(part1(problem_input))
