# Fuel required to launch a given module is based on its mass. Specifically, to find the fuel required for a module,
# take its mass, divide by three, round down, and subtract 2.
#
# For example:
#
#     For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
#     For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
#     For a mass of 1969, the fuel required is 654.
#     For a mass of 100756, the fuel required is 33583.
#
# The Fuel Counter-Upper needs to know the total fuel requirement. To find it, individually calculate the fuel needed
# for the mass of each module (your puzzle input), then add together all the fuel values.
#
# What is the sum of the fuel requirements for all of the modules on your spacecraft?


def part_1_module_fuel(mass):
    return mass // 3 - 2


def part_2_module_fuel(mass):
    total_module_fuel = part_1_module_fuel(mass)

    additional_fuel = total_module_fuel

    while True:
        additional_fuel = part_1_module_fuel(additional_fuel)

        if additional_fuel <= 0:
            break

        total_module_fuel += additional_fuel

    return total_module_fuel


if __name__ == "__main__":
    total_fuel = 0

    with open("01_input.txt") as module_weights:
        for module_weight in module_weights:
            total_fuel += part_2_module_fuel(int(module_weight.strip()))

    print(total_fuel)
