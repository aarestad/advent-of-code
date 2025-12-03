from __future__ import print_function

# To continue, please consult the code grid in the manual.  Enter the code at row 2947, column 3029.


def next_code(prev_code):
    return (prev_code * 252533) % 33554393


first_code = 20151125

row = 1
col = 1

while row != 2947 or col != 3029:
    first_code = next_code(first_code)

    if row == 1:
        row = col + 1
        col = 1
    else:
        row -= 1
        col += 1

print(row, col, first_code)
