if __name__ == "__main__":
    example = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""

    example_input = example.split("\n")

    with open("input/day8.txt") as input:
        problem_input = [i.strip() for i in input.readlines()]

    freq_locs = defaultdict()

    for freq in list(range(48, 58)) + list(range(65, 91)) + list(range(97, 123)):
        c = chr(freq)
        print(c)
