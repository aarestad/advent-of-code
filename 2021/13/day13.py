import re


if __name__ == "__main__":
    example = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""

    example_input = example.split("\n")

    with open("input/day13.txt") as input:
        problem_input = [i.strip() for i in input.readlines()]

    dots: set[(int, int)] = set()
    folds: list[(str, int)] = []

    parsing_folds = False
    for line in problem_input:
        if not line:
            parsing_folds = True
            continue

        if parsing_folds:
            parsed_fold = re.match(r"fold along (\w)=(\d+)", line)
            folds.append((parsed_fold[1], int(parsed_fold[2])))
        else:
            dot_x, dot_y = line.split(",")
            dots.add((int(dot_x), int(dot_y)))

    max_x = next(dot[0] for dot in sorted(dots, key=lambda d: d[0], reverse=True))
    max_y = next(dot[1] for dot in sorted(dots, key=lambda d: d[1], reverse=True))

    paper: list[list[str]] = []

    for row in range(max_y + 1):
        paper.append(["."] * (max_x + 1))

    for dot in dots:
        paper[dot[1]][dot[0]] = "#"

    for fold in folds:
        max_x = next(dot[0] for dot in sorted(dots, key=lambda d: d[0], reverse=True))
        max_y = next(dot[1] for dot in sorted(dots, key=lambda d: d[1], reverse=True))

        axis, value = fold

        new_paper: list[list[str]] = []
        new_dots: set[(str, str)] = set()

        if axis == "y":
            for row in range(value):
                new_paper.append([" "] * (max_x + 1))

            for dot in dots:
                dot_x = dot[0]
                dot_y = 2 * value - dot[1] if dot[1] > value else dot[1]

                if 0 <= dot_y < value:
                    new_dots.add((dot_x, dot_y))
        else:  # x
            for row in range(max_y + 1):
                new_paper.append([" "] * value)

            for dot in dots:
                dot_x = 2 * value - dot[0] if dot[0] > value else dot[0]
                dot_y = dot[1]

                if 0 <= dot_x < value:
                    new_dots.add((dot_x, dot_y))

        for dot in new_dots:
            new_paper[dot[1]][dot[0]] = "#"

        paper = new_paper
        dots = new_dots

        num_visible_dots = 0

        if fold == folds[0]:
            num_visible_dots = 0
            for line in paper:
                num_visible_dots += sum(1 for c in line if c == "#")
            print(num_visible_dots)

    for line in paper:
        print("".join(line))
