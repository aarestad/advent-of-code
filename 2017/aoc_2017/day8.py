def score_groups(stream: str) -> (int, int):
    nest_level = 0
    cancelling = False
    skip_next = False

    score = 0
    garbage_chars = 0

    for c in stream:
        if not skip_next:
            if c == '!':
                skip_next = True
            elif not cancelling:
                if c == '{':
                    nest_level += 1
                elif c == '}':
                    if nest_level < 1:
                        raise ValueError('nesting would go negative!')
                    score += nest_level
                    nest_level -= 1
                elif c == '<' :
                    cancelling = True
            elif c == '>':
                cancelling = False
            else:
                garbage_chars += 1
        else:
            skip_next = False

    if nest_level != 0:
        raise ValueError('unbalanced groups')

    return score, garbage_chars

if __name__ == "__main__":
    with open("input/day8.txt") as input:
        pass
        problem_input = [i.strip() for i in input.readlines()][0]
        print(score_groups(problem_input))
