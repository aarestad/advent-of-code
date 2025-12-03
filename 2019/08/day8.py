from itertools import chain

if __name__ == "__main__":
    layers = []

    with open("08_input.txt") as img_input:
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

    for row in range(6):
        for col in range(25):
            pixel_layer = (layer[row][col] for layer in layers)
            non_transparent_pixel_layer = filter(lambda p: p != 2, pixel_layer)
            image[row].append(non_transparent_pixel_layer.__next__())

    for line in image:
        print("".join(" " if x == 0 else "*" for x in line))
