from itertools import combinations

if __name__ == "__main__":
    with open("input/day9.txt") as encrypted_file:
        encrypted_numbers = [int(n.strip()) for n in encrypted_file.readlines()]

    target_number = -1

    for x in range(25, len(encrypted_numbers)):
        target_number = encrypted_numbers[x]

        if all(
            sum(combo) != target_number
            for combo in combinations(encrypted_numbers[x - 25 : x], 2)
        ):
            break

    print(target_number)

    for i in range(len(encrypted_numbers)):
        for j in range(i + 1, len(encrypted_numbers)):
            sublist = encrypted_numbers[i:j]

            if sum(sublist) == target_number:
                sublist.sort()
                print(sublist[0] + sublist[-1])
                exit()
