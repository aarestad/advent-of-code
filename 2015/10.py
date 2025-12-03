def look_and_say(input_str):
    out = ''

    char_run = ''
    char_run_count = 0

    for i in range(len(input_str)):
        char_run_count += 1
        if i < len(input_str) - 1 and input_str[i] == input_str[i + 1]:
            char_run = input_str[i]
        else:
            out += str(char_run_count)
            out += input_str[i]
            char_run_count = 0

    return out


start = '1113122113'

for _ in range(50):
    start = look_and_say(start)

print(len(start))
