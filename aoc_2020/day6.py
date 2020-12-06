example = """abc

a
b
c

ab
ac

a
a
a
a

b
"""


def part_one_count(answer_lists):
    count = 0

    for c in range(97, 123):  # lowercase letters in ASCII
        group_answers = list(chr(c) in answer for answer in answer_lists)

        if len(group_answers) > 0 and any(group_answers):
            count += 1

    return count


def part_two_count(answer_lists):
    count = 0

    for c in range(97, 123):  # lowercase letters in ASCII
        group_answers = list(chr(c) in answer for answer in answer_lists)

        if len(group_answers) > 0 and all(group_answers):
            count += 1

    return count


if __name__ == "__main__":
    part_one_total = 0
    part_two_total = 0

    with open("input/day6.txt") as answers:
        answer_set = []

        for line in answers:
            line = line.strip()

            if line == "":
                part_one_total += part_one_count(answer_set)
                part_two_total += part_two_count(answer_set)
                answer_set.clear()
                continue

            answer_set.append(line)

    # don't forget the last record (again)
    part_one_total += part_one_count(answer_set)
    part_two_total += part_two_count(answer_set)

    print(part_one_total)
    print(part_two_total)
