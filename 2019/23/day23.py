from collections import deque
from itertools import cycle
from typing import Dict

from aoc_2019.intcode import IntcodeMachine

if __name__ == "__main__":
    with open("23_input.txt") as nic_program_file:
        nic_program = nic_program_file.readline().strip()

    nics = {}

    input_queues: Dict[int, deque] = {addr: deque() for addr in range(50)}

    for address in range(50):
        nic = IntcodeMachine(nic_program, name=str(address))
        nic.send(address)
        nics[address] = nic

    nic_add = 0

    while True:
        print(f"checking machine {nic_add}")
        nic = nics[nic_add]

        if not input_queues[nic_add]:
            nic.send(-1)
        else:
            msg = input_queues[nic_add].popleft()
            nic.send(msg[0])
            nic.send(msg[1])

        send_addr = nic.receive()

        if send_addr is None:
            continue

        send_x = nic.receive()
        send_y = nic.receive()

        if send_addr == 255:
            print(send_y)
            exit()

        input_queues[send_addr].append((send_x, send_y))
        nic_add = send_addr
