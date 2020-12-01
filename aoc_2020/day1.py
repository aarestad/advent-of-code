if __name__ == '__main__':
    entries = []

    with open('input_01.txt') as entry_file:
        for entry in entry_file:
            entries.append(int(entry.strip()))

    for idx, val1 in enumerate(entries):
        for val2 in entries[idx + 1:]:
            for val3 in entries[idx + 2:]:
                if val1 + val2 + val3 == 2020:
                    print(val1 * val2 * val3)
                    exit()
