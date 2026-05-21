if __name__ == "__main__":
    example_input = """s1,x3/4,pe/b"""

    with open("input/day16.txt") as input:
        problem_input = [i.strip() for i in input.readlines()][0]

        dance_moves = problem_input.split(',')

        dancers = list('abcdefghijklmnop')

        for p in range(1_000_000_000):
            if p % 1_000 == 0:
                print(p)

            for dm in dance_moves:
                if dm.startswith('s'):
                    spin_amt = int(dm[1:])
                    dancers = dancers[-spin_amt:] + dancers[:-spin_amt]
                elif dm.startswith('x'):
                    d1, d2 = (int(d) for d in dm[1:].split('/'))
                    dancers[d1], dancers[d2] = dancers[d2], dancers[d1]
                elif dm.startswith('p'):
                    d1, d2 = dm[1:].split('/')
                    d1_idx = dancers.index(d1)
                    d2_idx = dancers.index(d2)
                    dancers[d1_idx], dancers[d2_idx] = d2, d1
                else:
                    raise ValueError(f'illegal dance move: {dm}')

        print(''.join(dancers))