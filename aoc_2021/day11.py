if __name__ == "__main__":
    example = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""

    example_input = example.split("\n")

    with open("input/day11.txt") as input:
        problem_input = [i.strip() for i in input.readlines()]

    octopi: list[list[int]] = []

    for line in problem_input:
        octopi.append([int(c) for c in line])

    num_flashes = 0

    for step in range(1, 2000):
        start_flashes = num_flashes

        for row in range(len(octopi)):
            for col in range(len(octopi[row])):
                octopi[row][col] += 1

        while True:
            flashed_this_turn = set()

            for row, line in enumerate(octopi):
                for col, octopus in enumerate(line):
                    if octopus > 9:
                        octopi[row][col] = 0
                        flashed_this_turn.add((row, col))

                        if row > 0:
                            if col > 0 and octopi[row - 1][col - 1] > 0:
                                octopi[row - 1][col - 1] += 1

                            if octopi[row - 1][col] > 0:
                                octopi[row - 1][col] += 1

                            if col <= len(line) - 2 and octopi[row - 1][col + 1] > 0:
                                octopi[row - 1][col + 1] += 1
                        if col > 0 and octopi[row][col - 1] > 0:
                            octopi[row][col - 1] += 1
                        if col <= len(line) - 2 and octopi[row][col + 1] > 0:
                            octopi[row][col + 1] += 1
                        if row <= len(octopi) - 2:
                            if col > 0 and octopi[row + 1][col - 1] > 0:
                                octopi[row + 1][col - 1] += 1

                            if octopi[row + 1][col] > 0:
                                octopi[row + 1][col] += 1

                            if col <= len(line) - 2 and octopi[row + 1][col + 1] > 0:
                                octopi[row + 1][col + 1] += 1

            if len(flashed_this_turn) == 0:
                break

            num_flashes += len(flashed_this_turn)

        if step == 100:
            print(f"{num_flashes} flashes after 100 steps")

        if num_flashes - start_flashes == 100:
            print(f"all 100 synced at step {step}")
            break
