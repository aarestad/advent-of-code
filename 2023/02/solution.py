## advent of code 2023
## https://adventofcode.com/2023
## day 02

from dataclasses import dataclass
import re
from typing import List


@dataclass
class Turn:
    num_red: int
    num_blue: int
    num_green: int


@dataclass
class Game:
    id: int
    turns: List[Turn]


# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
GAME_RE = re.compile(r"Game (\d+): (.+)")
RED_RE = re.compile(r"(\d+) red")
BLUE_RE = re.compile(r"(\d+) blue")
GREEN_RE = re.compile(r"(\d+) green")


def parse_input(lines):
    games = []

    for line in lines:
        match = GAME_RE.search(line)
        game_id = int(match.group(1))
        turn_strs = match.group(2).split("; ")

        turns = []

        for t in turn_strs:
            turn = Turn(0, 0, 0)

            if m := RED_RE.search(t):
                turn.num_red = int(m.group(1))

            if m := BLUE_RE.search(t):
                turn.num_blue = int(m.group(1))

            if m := GREEN_RE.search(t):
                turn.num_green = int(m.group(1))

            turns.append(turn)

        games.append(Game(game_id, turns))

    return games


def part1(games):
    game_id_sum = 0
    # 12 red cubes, 13 green cubes, and 14 blue cubes
    for g in games:
        if all(
            t.num_red <= 12 and t.num_green <= 13 and t.num_blue <= 14 for t in g.turns
        ):
            game_id_sum += g.id

    return game_id_sum


def part2(games):
    game_power_sum = 0

    for g in games:
        min_red = 0
        min_green = 0
        min_blue = 0

        for t in g.turns:
            if t.num_red > min_red:
                min_red = t.num_red
            if t.num_green > min_green:
                min_green = t.num_green
            if t.num_blue > min_blue:
                min_blue = t.num_blue

        game_power_sum += min_red * min_green * min_blue

    return game_power_sum
