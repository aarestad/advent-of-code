## advent of code 2023
## https://adventofcode.com/2023
## day 19

from enum import StrEnum
from dataclasses import dataclass
from typing import Optional, List, Dict, NewType
import re


class Category(StrEnum):
    X_COOL = "x"
    MUSICAL = "m"
    AERO = "a"
    SHINY = "s"


Part = NewType("Part", Dict[Category, int])


class WorkflowCondition:
    def __init__(self, cond_str):
        cond_re = re.compile(r"(\w)([<|>])(\d+)")
        cond_match = cond_re.match(cond_str)
        self.category = cond_match[1]
        self.comparator = cond_match[2]
        self.value = int(cond_match[3])

    def passes(self, part: Part) -> bool:
        match self.comparator:
            case "<":
                return part[self.category] < self.value
            case ">":
                return part[self.category] > self.value
            case _:
                raise ValueError(f"bad comparator: {self.comparator}")


class WorkflowResult(StrEnum):
    REJECT = "R"
    ACCEPT = "A"


class WorkflowRule:
    def __init__(self, rule_str):
        rule_split = rule_str.split(":")

        if len(rule_split) == 1:
            self.result = rule_split[0]
            self.condition = None
        else:
            self.condition = WorkflowCondition(rule_split[0])
            self.result = rule_split[1]

    def evaluate(self, part: Part) -> Optional[str | WorkflowResult]:
        if self.condition is None or self.condition.passes(part):
            return self.result

        return None


@dataclass
class Workflow:
    name: str
    rules: List[WorkflowRule]

    def __init__(self, workflow_str):
        workflow_re = re.compile(r"(\w+)\{(.+)\}")
        workflow_match = workflow_re.match(workflow_str)
        self.name = workflow_match[1]
        rule_strs = workflow_match[2].split(",")

        self.rules = [WorkflowRule(rs) for rs in rule_strs]

    def run(self, part: Part) -> str | WorkflowResult:
        for rule in self.rules:
            result = rule.evaluate(part)

            if result is not None:
                return result
        else:
            raise ValueError(f"rule {self.name} has no matching rules")


def parse_input(lines):
    workflows = dict()
    parts = []

    for line in lines:
        if ":" in line:
            wf = Workflow(line)
            workflows[wf.name] = wf
        elif "=" in line:
            part_str = re.match(r"^\{(.+)\}", line)

            part = {}

            for prop in part_str[1].split(","):
                label, value = prop.split("=")
                part[label] = int(value)

            parts.append(part)
        else:
            if line:
                raise ValueError(f"unexpected non-blank line {line}")

    return workflows, parts


def part1(workflows, parts):
    prop_sum = 0

    for part in parts:
        prev_workflow = "in"
        possible_result = None

        print(f"{part}: ", end="")

        while possible_result not in list(WorkflowResult):
            print(f"{prev_workflow} -> ", end="")
            workflow = workflows[prev_workflow]
            possible_result = workflow.run(part)

            if possible_result in list(WorkflowResult):
                print(possible_result)

                if possible_result == WorkflowResult.ACCEPT:
                    prop_sum += sum(part.values())

                break
            else:
                prev_workflow = possible_result

    return prop_sum


def part2(workflows, parts):
    pass
