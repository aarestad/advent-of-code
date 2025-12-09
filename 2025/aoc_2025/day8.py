from math import sqrt

def part1(input):
    box_locs = [[int(c) for c in l.split(",")] for l in input]
    print(box_locs)
    
    points_with_distances = []
    
    for i in range(len(box_locs)):
        for j in range(i+1, len(box_locs)):
            point_a = box_locs[i]
            point_b = box_locs[j]
            
            points_with_distances.append(((point_a, point_b), distance_btwn(point_a, point_b)))
    
    points_with_distances.sort(key=lambda x: x[1])
    
    

def distance_btwn(a, b):
    return sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2 + (a[2] - b[2])**2)

if __name__ == "__main__":
    example = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""

    example_input = example.split("\n")
    part1(example_input)

    with open("input/day8.txt") as input:
        problem_input = [i.strip() for i in input.readlines()]
