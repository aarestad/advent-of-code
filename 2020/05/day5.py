if __name__ == "__main__":
    occupied_seats = []

    with open("input/day5.txt") as ticket_ids:
        for ticket_id in ticket_ids:
            seat_binary = (
                ticket_id.strip()
                .replace("F", "0")
                .replace("B", "1")
                .replace("L", "0")
                .replace("R", "1")
            )
            occupied_seats.append(int(seat_binary, 2))

    occupied_seats.sort()

    for idx, seat in enumerate(occupied_seats):
        if occupied_seats[idx + 1] != seat + 1:
            print(seat + 1)
            exit()
