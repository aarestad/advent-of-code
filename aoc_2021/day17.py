import re

if __name__ == "__main__":
    example = """target area: x=20..30, y=-10..-5"""

    example_input = example.split("\n")

    with open("input/day17.txt") as input:
        problem_input = [i.strip() for i in input.readlines()]

    parsed_input = re.match(
        r"target area: x=(\d+)\.\.(\d+), y=(-?\d+)..(-?\d+)", problem_input[0]
    )
    target_x_range = (int(parsed_input[1]), int(parsed_input[2]))
    target_y_range = (int(parsed_input[3]), int(parsed_input[4]))

    best_y = 0

    num_hit_velocities = 0

    # max = ??? (73 found by experiment)
    for dy in range(target_y_range[0], 74):
        # min = smallest n s.t. nth triangle number >= target_x_range[0]
        for dx in range(24, target_x_range[1] + 1):
            current_pos = (0, 0)
            velocity = (dx, dy)

            while True:
                current_pos = (
                    current_pos[0] + velocity[0],
                    current_pos[1] + velocity[1],
                )

                if (
                    target_x_range[0] <= current_pos[0] <= target_x_range[1]
                    and target_y_range[0] <= current_pos[1] <= target_y_range[1]
                ):
                    num_hit_velocities += 1
                    highest_for_shot = 0 if dy <= 0 else (dy * (dy + 1)) // 2

                    if best_y < highest_for_shot:
                        best_y = highest_for_shot

                    break

                if target_y_range[0] > current_pos[1]:
                    break

                # else still on its way; adjust velocity
                velocity = (max(0, velocity[0] - 1), velocity[1] - 1)

    print(f"best y is {best_y}")
    print(f"number of hitting velocities: {num_hit_velocities}")
