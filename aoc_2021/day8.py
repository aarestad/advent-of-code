import itertools

if __name__ == "__main__":
    example = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""

    example_input = example.split("\n")

    with open("input/day8.txt") as input:
        problem_input = [i.strip() for i in input.readlines()]

    numbers = []

    for line in problem_input:
        identified_patterns = [""] * 10
        length_5_patterns = []
        length_6_patterns = []

        at_output = False

        (patterns, output) = line.split("|")

        for pattern in patterns.split():
            if len(pattern) == 2:
                identified_patterns[1] = pattern
            elif len(pattern) == 3:
                identified_patterns[7] = pattern
            elif len(pattern) == 4:
                identified_patterns[4] = pattern
            elif len(pattern) == 5:
                length_5_patterns.append(pattern)
            elif len(pattern) == 6:
                length_6_patterns.append(pattern)
            elif len(pattern) == 7:
                identified_patterns[8] = pattern
            else:
                raise ValueError(f"unexpected length for {pattern}")

        one_letters = [c for c in identified_patterns[1]]

        for pattern in length_5_patterns:  # 2, 3, 5
            if all(letter in pattern for letter in one_letters):
                identified_patterns[3] = pattern

        top_left_element = [
            c for c in identified_patterns[4] if c not in identified_patterns[3]
        ][0]

        for pattern in length_5_patterns:  # 2, 5
            if top_left_element in pattern:
                identified_patterns[5] = pattern
            elif pattern != identified_patterns[3]:
                identified_patterns[2] = pattern

        middle_element = [
            c
            for c in identified_patterns[4]
            if c in identified_patterns[2] and c in identified_patterns[5]
        ][0]

        top_right_element = [
            c for c in identified_patterns[1] if c not in identified_patterns[5]
        ][0]

        for pattern in length_6_patterns:  # 0, 6, 9
            if middle_element not in pattern:
                identified_patterns[0] = pattern
            elif top_right_element in pattern:
                identified_patterns[9] = pattern
            else:
                identified_patterns[6] = pattern

        number = ""

        for digit in output.split():
            for d, p in enumerate(identified_patterns):
                perms = list("".join(perm) for perm in itertools.permutations(p))
                if digit in perms:
                    number += str(d)

        numbers.append(int(number))
        print(number)

    print(sum(numbers))
