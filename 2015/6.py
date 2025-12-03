with open("input_6.txt") as light_rows:
    light_row = [0] * 1000

    lights = []

    for _ in range(1000):
        lights.append(light_row[:])

    for line in light_rows:
        tokens = line.split()
        if tokens[0] == "turn":
            verb = tokens[1]
            start = tokens[2]
            stop = tokens[4]
        else:
            verb = "toggle"
            start = tokens[1]
            stop = tokens[3]

        (start_x, start_y) = map(int, start.split(","))
        (stop_x, stop_y) = map(int, stop.split(","))

        print(verb, start_x, start_y, stop_x, stop_y)

        for x in range(start_x, stop_x + 1):
            for y in range(start_y, stop_y + 1):
                if verb == "on":
                    lights[x][y] += 1
                elif verb == "off" and lights[x][y] > 0:
                    lights[x][y] -= 1
                elif verb == "toggle":
                    lights[x][y] += 2

    total_brightness = 0

    for x in range(0, 1000):
        for y in range(0, 1000):
            total_brightness += lights[x][y]

    print(total_brightness)
