class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __eq__(self, other):
        return self.value == other.value


num_elves = 3001330
# num_elves = 5

first_elf = Node(1)
prev_elf = first_elf

for i in range(2, num_elves + 1):
    next_elf = Node(i)
    prev_elf.next = next_elf
    prev_elf = next_elf

prev_elf.next = first_elf

curr_elf = first_elf

num_left = num_elves

while num_left > 1:
    if num_left % 2 == 0:
        across = num_left // 2
    else:
        across = (num_left - 1) // 2

    curr = curr_elf

    while across > 1:
        curr = curr.next
        across -= 1

    print("deleting %d" % curr.next.value)

    curr.next = curr.next.next
    curr_elf = curr_elf.next
    num_left -= 1

print(curr_elf.value)
