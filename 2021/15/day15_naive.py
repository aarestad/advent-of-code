if __name__ == "__main__":
    example = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""

    example_input = example.split("\n")

    with open("input/day15.txt") as input:
        problem_input = [i.strip() for i in input.readlines()]

    map = example_input
    best_score = 9999999999
    best_path = []

    for run in range(2 ** ((len(map) - 1) * 2)):
        if run % 1000 == 0:
            print(run)
        current_loc = [0, 0]
        current_path = []

        for bit in range((len(map) - 1) * 2):
            if run & (1 << bit):
                if current_loc[0] < len(map) - 1:
                    current_loc[0] += 1
                else:
                    current_loc[1] += 1
            else:
                if current_loc[1] < len(map) - 1:
                    current_loc[1] += 1
                else:
                    current_loc[0] += 1

            current_path.append(int(example_input[current_loc[1]][current_loc[0]]))

        score = sum(current_path)
        if score < best_score:
            best_score = score
            best_path = current_path

    print(best_path)
    print(best_score)
