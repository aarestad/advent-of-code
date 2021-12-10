import math


def corrupting_char(line: str) -> str:
    open_chunks = []

    for c in line:
        if c in ["(", "[", "{", "<"]:
            open_chunks.append(c)
        else:
            last_char = open_chunks.pop()
            if (
                last_char == "("
                and c != ")"
                or last_char == "["
                and c != "]"
                or last_char == "{"
                and c != "}"
                or last_char == "<"
                and c != ">"
            ):
                return c

    return ""


def completing_chars(line: str) -> str:
    open_chunks = []

    for c in line:
        if c in ["(", "[", "{", "<"]:
            open_chunks.append(c)
        else:
            open_chunks.pop()

    completion = ""

    for c in reversed(open_chunks):
        if c == "(":
            completion += ")"
        else:
            completion += chr(ord(c) + 2)

    return completion


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

    score = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
    }

    print(sum(score[c] for c in corrupting_chars if c in score))

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
