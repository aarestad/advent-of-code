from typing import Optional

if __name__ == "__main__":
    example = """16,1,2,0,4,2,7,1,2,14"""

    example_input = example.split("\n")

    with open("input/day7.txt") as input:
        problem_input = [i.strip() for i in input.readlines()]

    positions = [int(p) for p in problem_input[0].split(",")]
    positions.sort()

    best_position = None
    best_fuel: Optional[int] = None

    for position in range(positions[-1] + 1):
        other_positions = positions[:]

        total_fuel = 0

        for p in other_positions:
            diff = abs(p - position)
            total_fuel += (diff * (diff + 1)) / 2

        if best_fuel is None or total_fuel < best_fuel:
            best_position = position
            best_fuel = total_fuel

    print((best_position, best_fuel))
