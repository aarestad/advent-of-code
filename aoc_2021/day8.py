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
        pattern_map = {num: "" for num in range(1, 10)}
        length_5_patterns = []
        length_6_patterns = []

        at_output = False

        (patterns, output) = line.split("|")

        for pattern in patterns.split():
            if len(pattern) == 2:
                pattern_map[1] = pattern
            elif len(pattern) == 3:
                pattern_map[7] = pattern
            elif len(pattern) == 4:
                pattern_map[4] = pattern
            elif len(pattern) == 5:
                length_5_patterns.append(pattern)
            elif len(pattern) == 6:
                length_6_patterns.append(pattern)
            elif len(pattern) == 7:
                pattern_map[8] = pattern
            else:
                raise ValueError(f"unexpected length for {pattern}")

        one_letters = [c for c in pattern_map[1]]

        top_element = [c for c in pattern_map[7] if c not in pattern_map[1]][0]

        for pattern in length_5_patterns:  # 2, 3, 5
            if all(letter in pattern for letter in one_letters):
                pattern_map[3] = pattern

        top_left_element = [c for c in pattern_map[4] if c not in pattern_map[3]][0]

        for pattern in length_5_patterns:  # 2, 5
            if top_left_element in pattern:
                pattern_map[5] = pattern
            elif pattern != pattern_map[3]:
                pattern_map[2] = pattern

        middle_element = [
            c
            for c in pattern_map[4]
            if c in pattern_map[2] and c in pattern_map[4] and c in pattern_map[5]
        ][0]

        top_right_element = [c for c in pattern_map[1] if c not in pattern_map[5]][0]

        for pattern in length_6_patterns:  # 0, 6, 9
            if middle_element not in pattern:
                pattern_map[0] = pattern
            elif top_right_element in pattern:
                pattern_map[9] = pattern
            else:
                pattern_map[6] = pattern

        number = ""

        for digit in output.split():
            for d, p in pattern_map.items():
                perms = list("".join(perm) for perm in itertools.permutations(p))
                if digit in list(perms):
                    number += str(d)

        numbers.append(int(number))
        print(number)

    print(sum(numbers))
