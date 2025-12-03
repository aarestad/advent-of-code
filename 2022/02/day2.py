part_1_score = 0
part_2_score = 0

game_scores = {
    "A": {
        "X": 3,
        "Y": 6,
        "Z": 0,
    },
    "B": {
        "X": 0,
        "Y": 3,
        "Z": 6,
    },
    "C": {
        "X": 6,
        "Y": 0,
        "Z": 3,
    },
}

choices = {
    "A": {
        "X": "Z",
        "Y": "X",
        "Z": "Y",
    },
    "B": {
        "X": "X",
        "Y": "Y",
        "Z": "Z",
    },
    "C": {
        "X": "Y",
        "Y": "Z",
        "Z": "X",
    },
}

choice_scores = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}

with open("day2.txt") as guide:
    for line in guide:
        (opponent, response) = line.split()
        part_1_score += choice_scores[response]
        part_1_score += game_scores[opponent][response]

        part_2_choice = choices[opponent][response]
        part_2_score += choice_scores[part_2_choice]
        part_2_score += game_scores[opponent][part_2_choice]

print(part_1_score)
print(part_2_score)
