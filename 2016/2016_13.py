favorite_number = 1358

def is_open(x, y):
    return count_bits(x*x + 3*x + 2*x*y + y + y*y + favorite_number) % 2 == 0

def count_bits(i):
    bit_count = 0

    while i > 0:
        bit_count += i & 1
        i >>= 1

    return bit_count

def count_bits_fast(i):
    i = i - ((i >> 1) & 0x55555555)
    i = (i & 0x33333333) + ((i >> 2) & 0x33333333)
    return (((i + (i >> 4)) & 0x0F0F0F0F) * 0x01010101) >> 24

for y in range(40):
    for x in range(40):
        print('x' if x == 1 and y == 1 else '*' if x == 31 and y == 39 else '.' if is_open(x, y) else '#', end='')
    print()
