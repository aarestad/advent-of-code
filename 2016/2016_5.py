from hashlib import md5

def solve_part_1(door_id):
    idx = 0

    password = []

    while len(password) < 8:
        if idx % 1000000 == 0: print(idx)

        m = md5()
        m.update(door_id)
        m.update(bytearray(str(idx), 'utf-8'))
        digest = m.hexdigest()

        if digest[:5] == '00000':
            print('***' + digest[5])
            password.append(digest[5])

        idx += 1

    return ''.join(password)

def solve_part_2(door_id):
    idx = 0

    password = [None] * 8

    while len(list(filter(lambda x: x is None, password))) > 0:
        if idx % 1000000 == 0: print(idx)

        m = md5()
        m.update(door_id)
        m.update(bytearray(str(idx), 'utf-8'))
        digest = m.hexdigest()

        if digest[:5] == '00000':
            try:
                password_idx = int(digest[5])
            except ValueError:
                idx += 1
                continue

            if password_idx > 7 or password[password_idx] is not None:
                idx += 1
                continue
                
            print('index ' + digest[5])
            print('letter ' + digest[6])
            password[password_idx] = digest[6]

        idx += 1

    return ''.join(password)

#print(solve_part_1('abbhdwsy'))
print(solve_part_2('abbhdwsy'))
