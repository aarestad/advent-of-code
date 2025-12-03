example = """3,4,3,1,2"""

example_input = example.split("\n")

with open("input/day6.txt") as input:
    problem_input = [i.strip() for i in input.readlines()]

if __name__ == "__main__":
    fish_timers = [int(t) for t in problem_input[0].split(",")]

    num_fish_by_timer = {}

    for ft in fish_timers:
        if ft not in num_fish_by_timer:
            num_fish_by_timer[ft] = 1
        else:
            num_fish_by_timer[ft] += 1

    for d in range(256):
        new_fish_timers = {}

        for time, num_fish in num_fish_by_timer.items():
            if time > 0:
                new_time = time - 1

                if new_time not in new_fish_timers:
                    new_fish_timers[new_time] = num_fish
                else:
                    new_fish_timers[new_time] += num_fish
            else:
                if 6 not in new_fish_timers:
                    new_fish_timers[6] = num_fish
                else:
                    new_fish_timers[6] += num_fish

                new_fish_timers[8] = num_fish

        print(f"{sum(new_fish_timers.values())} fish after {d+1} days")
        num_fish_by_timer = new_fish_timers
