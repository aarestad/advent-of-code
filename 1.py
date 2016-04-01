with open('input_1.txt') as input:
  floor = 0
  current_char = 0

  for line in input:
    for c in line:
      current_char += 1
      if c == '(': floor += 1
      if c == ')': floor -= 1
      if floor < 0: print current_char

print floor
