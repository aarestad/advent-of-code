import math


brackets = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}


def corrupting_char(line: str) -> str:
    open_chunks = []

    for c in line:
        if c in brackets:
            open_chunks.append(c)
        elif brackets[open_chunks.pop()] != c:
            return c

    return ""


def completing_chars(line: str) -> str:
    open_chunks = []

    for c in line:
        if c in brackets:
            open_chunks.append(c)
        else:
            open_chunks.pop()

    return "".join(brackets[c] for c in reversed(open_chunks))


if __name__ == "__main__":
    example = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""

    example_input = example.split("\n")

    with open("input/day10.txt") as input:
        problem_input = [i.strip() for i in input.readlines()]

    corrupting_chars = [corrupting_char(l) for l in problem_input]

    part_1_score = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
    }

    print(sum(part_1_score[c] for c in corrupting_chars if c in part_1_score))

    incomplete_lines = [l for l in problem_input if corrupting_char(l) == ""]

    completions = [completing_chars(l) for l in incomplete_lines]

    part_2_score = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4,
    }

    scores = []

    for completion in completions:
        score = 0

        for c in completion:
            score = score * 5 + part_2_score[c]

        scores.append(score)

    scores.sort()
    print(scores[math.floor(len(scores) / 2)])
