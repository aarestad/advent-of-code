from itertools import chain

if __name__ == '__main__':
    layers = []

    with open('08_input.txt') as img_input:
        img_data = img_input.readline().strip()

    for idx, c in enumerate(img_data):
        if idx % 150 == 0:
            layers.append([[], [], [], [], [], []])

        frame_no = idx // 150
        row_no = (idx % 150) // 25
        layers[frame_no][row_no].append(int(c))

    fewest_zeros_layer = None
    fewest_num_zeroes = None

    for layer in layers:
        num_zeros = len([x for x in chain(*layer) if x == 0])

        if fewest_zeros_layer is None or num_zeros < fewest_num_zeroes:
            fewest_zeros_layer = layer
            fewest_num_zeroes = num_zeros

    num_ones = len([x for x in chain(*fewest_zeros_layer) if x == 1])
    num_twos = len([x for x in chain(*fewest_zeros_layer) if x == 2])
    print(num_ones * num_twos)

    image = [[], [], [], [], [], []]

    for x in range(150):
        for layer in layers:
            pixel = layer[x // 25][x % 25]
            if pixel == 2:
                continue

            image[x // 25].append(pixel)
            break

    for line in image:
        print(''.join(' ' if x == 0 else '*' for x in line))
