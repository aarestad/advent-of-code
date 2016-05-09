def decoded_len(s):
    chars = 0

    # 0: not in an escape sequence
    # 1: just saw a \
    # 2: in a hex sequence (just saw \x)
    # 3: passed the first of 2 hex chars (just saw \xd for some digit d)
    state = 0

    for c in s[1:-1]: # assume all strings are quoted
        if state == 0 and c == "\\":
            state = 1
            continue
        if state == 1 and (c == "\\" or c == '"'):
            chars += 1
            state = 0
            continue
        if state == 1 and c == 'x':
            state = 2
            continue
        if state == 2:
            state = 3
            continue
        if state == 3:
            chars += 1
            state = 0
            continue
        # just a normal char
        chars += 1
        continue

    return chars

total_raw_chars = 0
total_computed_chars = 0

with open('input_8.txt') as strings:
    for s in strings:
        s = s.strip()
        raw_chars = len(s)
        computed_chars = decoded_len(s)
        print s, raw_chars, computed_chars
        total_raw_chars += raw_chars
        total_computed_chars += computed_chars

print(total_raw_chars - total_computed_chars)
