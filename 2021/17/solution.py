## advent of code 2021
## https://adventofcode.com/2021
## day 17
import re


def parse_input(lines):
    parsed_input = re.match(
        r"target area: x=(\d+)\.\.(\d+), y=(-?\d+)\.\.(-?\d+)", lines[0]
    )
    target_x_range = (int(parsed_input[1]), int(parsed_input[2]))
    target_y_range = (int(parsed_input[3]), int(parsed_input[4]))
    return (target_x_range, target_y_range)


def part1(target_x_range, target_y_range):
    best_y = 0

    # TODO max = ??? (73 found by experiment)
    for dy in range(target_y_range[0], 74):
        # TODO this range can be tightened based on dy
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
                    highest_for_shot = 0 if dy <= 0 else (dy * (dy + 1)) // 2

                    if best_y < highest_for_shot:
                        best_y = highest_for_shot

                    break

                if (
                    target_x_range[1] < current_pos[0]
                    or target_y_range[0] > current_pos[1]
                ):
                    break

                # else still on its way; adjust velocity
                velocity = (max(0, velocity[0] - 1), velocity[1] - 1)

    return best_y


def part2(target_x_range, target_y_range):
    num_hit_velocities = 0

    for dy in range(target_y_range[0], 74):
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
                    break

                if (
                    target_x_range[1] < current_pos[0]
                    or target_y_range[0] > current_pos[1]
                ):
                    break

                # else still on its way; adjust velocity
                velocity = (max(0, velocity[0] - 1), velocity[1] - 1)

    return num_hit_velocities
