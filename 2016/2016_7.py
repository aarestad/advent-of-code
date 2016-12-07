import re

def is_abba(s):
    return s[0] != s[1] and s[0] == s[3] and s[1] == s[2]

def is_aba(s):
    return s[0] != s[1] and s[0] == s[2]

def is_corresponding_bab(s, aba):
    return s[0] == aba[1] and s[1] == aba[0] and is_aba(s)

def find_bracketed_subseqs(address):
    subseqs = []

    subseq = None

    for c in address:
        if c == '[':
            subseq = []
            continue
        elif c != ']' and subseq is not None:
            subseq.append(c)
            continue
        elif c == ']':
            subseqs.append(''.join(subseq))
            subseq = None

    return subseqs

def is_tls_address(address):
    hypernet_seqs = find_bracketed_subseqs(address)
    #print('inside brackets: %s' % hypernet_seqs)

    for seq in hypernet_seqs:
        for i in range(0, len(seq) - 3):
            if is_abba(seq[i:i+4]):
                #print('%s is not TLS' % address)
                return False

    seqs_outside_brackets = re.split(r'\[\w+\]', address)
    #print('outside brackets: %s' % seqs_outside_brackets)

    for seq in seqs_outside_brackets:
        for i in range(0, len(seq) - 3):
            if is_abba(seq[i:i+4]):
                #print('%s is TLS' % address)
                return True

    #print('%s is not TLS' % address)
    return False

def is_ssl_address(address):
    hypernet_seqs = find_bracketed_subseqs(address)
    seqs_outside_brackets = re.split(r'\[\w+\]', address)

    for seq in seqs_outside_brackets:
        for i in range(0, len(seq) - 2):
            subseq = seq[i:i+3]

            if is_aba(subseq):
                for hseq in hypernet_seqs:
                    for i in range(0, len(hseq) - 2):
                        if is_corresponding_bab(hseq[i:i+3], subseq):
                            return True

    return False

def solve_part_1(addresses):
    tls_count = 0

    for address in addresses:
        if is_tls_address(address): tls_count += 1

    return tls_count

def solve_part_2(addresses):
    ssl_count = 0

    for address in addresses:
        if is_ssl_address(address): ssl_count += 1

    return ssl_count

with open('input_7.txt') as adds:
    addresses = [a.strip() for a in adds.readlines()]
    print(solve_part_1(addresses))
    print(solve_part_2(addresses))
