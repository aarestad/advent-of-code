from hashlib import md5
import re

salt = b"cuanljph"


def has_triplet(s):
    match = re.search(r"(.)\1\1", s)
    if match:
        return match.group(1)
    return None


def has_quintuplet_of(s, c):
    return re.search(c * 5, s)


def is_key(idx):
    digest = None

    for _ in range(2017):
        m = md5()
        s = (
            bytearray(digest, "utf-8")
            if digest
            else salt + bytearray(str(idx), "utf-8")
        )
        m.update(s)
        digest = m.hexdigest()

    c = has_triplet(digest)

    if c:
        for i in range(1, 1001):
            digest2 = None

            for _ in range(2017):
                m2 = md5()
                s2 = (
                    bytearray(digest2, "utf-8")
                    if digest2
                    else salt + bytearray(str(idx + i), "utf-8")
                )
                m2.update(s2)
                digest2 = m2.hexdigest()

            if has_quintuplet_of(digest2, c):
                print("%s %s" % (idx, digest))
                print("* %s %s" % (idx + i, digest2))
                return True

    return False


num_key = 0

idx = 0

while num_key < 64:
    if idx % 10 == 0:
        print(idx)
    if is_key(idx):
        num_key += 1
    idx += 1
