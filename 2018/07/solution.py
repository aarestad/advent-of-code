## advent of code 2018
## https://adventofcode.com/2018
## day 07
import re
from dataclasses import dataclass
from typing import Dict
from itertools import filterfalse, tee


@dataclass
class Step:
    name: str
    required_steps: list[str]


def parse_input(lines) -> Dict[str, Step]:
    steps_by_name: Dict[str, Step] = {}

    arrow_pattern = re.compile(r'Step (\w) must be finished before step (\w) can begin.')

    for line in lines:
        prereq_name, step_name = arrow_pattern.search(line).groups()

        if step_name in steps_by_name:
            steps_by_name[step_name].required_steps.append(prereq_name)
        else:
            steps_by_name[step_name] = Step(name=step_name, required_steps=[prereq_name])

        if prereq_name not in steps_by_name:
            steps_by_name[prereq_name] = Step(name=prereq_name, required_steps=[])

    return steps_by_name


def part1():
    with open('input.txt') as f:
        steps = parse_input(f.readlines())
        print(steps)

        steps_taken: list[str] = []

        while len(steps) > 0:
            possible_steps = [s.name for s in steps.values() if all(p in steps_taken for p in s.required_steps)]
            possible_steps.sort()
            next_step = possible_steps[0]
            steps_taken.append(next_step)
            del steps[next_step]

        print(''.join(steps_taken))

def part2(data):
    base_length = 3
    num_workers = 2

    with open('example_input.txtinput.txt') as f:
        steps = parse_input(f.readlines())
        print(steps)

        steps_taken: list[str] = []

        timer = 0
        current_workers = []

        while len(steps) > 0:
            possible_steps = [s.name for s in steps.values() if all(p in steps_taken for p in s.required_steps)]
            possible_steps.sort()

            finished, not_finished = [], []

            finished_pred = lambda w: timer - w[1] >= base_length

            for cw in current_workers:
                (finished if finished_pred(cw) else not_finished).append(cw)

            current_workers = not_finished
            current_workers.sort(key=lambda w: w[0])

            while len(current_workers) < num_workers:
                finished_worker = current_workers.pop(0)

if __name__ == '__main__':
    part1()