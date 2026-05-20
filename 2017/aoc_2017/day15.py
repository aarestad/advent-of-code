def generator_a(init: int):
    next = init

    while True:
        next = (next * 16807) % 2147483647
        if next & 0b11 == 0:
            yield next

def generator_b(init: int):
    next = init

    while True:
        next = (next * 48271) % 2147483647
        if next & 0b111 == 0:
            yield next

if __name__ == "__main__":
    gen_a = generator_a(883)
    gen_b = generator_b(879)

    rounds = 0

    judge_count = 0

    for a, b in zip(gen_a, gen_b):
        if a & 0xffff == b & 0xffff:
            print("match!")
            print(f"a={a}, b={b}, round={rounds+1}")
            judge_count += 1

        rounds += 1
        if rounds == 5_000_000:
            break

    print(judge_count)
