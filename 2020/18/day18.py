examples = [
    ("1 + 2 * 3 + 4 * 5 + 6", 71),
    ("1 + (2 * 3) + (4 * (5 + 6))", 51),
    ("2 * 3 + (4 * 5)", 26),
    ("5 + (8 * 3 + 9 + 3 * 4 * 3)", 437),
    ("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))", 12240),
    ("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2", 13632),
]


def evaluate(stmt: str) -> int:
    result = None
    current_op = None

    for idx, char in enumerate(stmt):
        try:
            val = int(char)

            if result is None:
                result = val
            elif current_op == "+":
                result += val
            elif current_op == "*":
                result *= val
            else:
                raise ValueError("unexpected state")
        except ValueError:
            if char == "+" or char == "*":
                current_op = char
            if char == "(":
                open_paren_count = 1
                substr_start = idx + 1

                for idx, subc in enumerate(stmt[substr_start:]):
                    substr_end = substr_start + idx

                    if subc == "(":
                        open_paren_count += 1
                    elif subc == ")":
                        open_paren_count -= 1
                        if open_paren_count == 0:
                            val = evaluate

                            if result is None:
                                result = val
                            elif current_op == "+":
                                result += val
                            elif current_op == "*":
                                result *= val
                            else:
                                raise ValueError("unexpected state")

    return result


if __name__ == "__main__":
    results = [evaluate(ex[0]) for ex in examples]
    print(results)
    print([ex[1] for ex in examples])
