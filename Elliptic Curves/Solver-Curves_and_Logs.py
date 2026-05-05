#!/usr/bin/env python3
import hashlib

p = 9739
a = 497
b = 1768

QA = (815, 3190)
nB = 1829


def inverse_mod(k, p):
    return pow(k, -1, p)


def point_add(P, Q):
    if P is None:
        return Q

    if Q is None:
        return P

    x1, y1 = P
    x2, y2 = Q

    if x1 == x2 and (y1 + y2) % p == 0:
        return None

    if P == Q:
        m = ((3 * x1 * x1 + a) * inverse_mod(2 * y1, p)) % p
    else:
        m = ((y2 - y1) * inverse_mod(x2 - x1, p)) % p

    x3 = (m * m - x1 - x2) % p
    y3 = (m * (x1 - x3) - y1) % p

    return (x3, y3)


def scalar_mult(k, P):
    result = None
    addend = P

    while k > 0:
        if k & 1:
            result = point_add(result, addend)

        addend = point_add(addend, addend)
        k >>= 1

    return result


def main():
    shared_secret = scalar_mult(nB, QA)
    x = shared_secret[0]
    flag = hashlib.sha1(str(x).encode()).hexdigest()

    print(f"Shared secret: {shared_secret}")
    print(f"x coordinate: {x}")
    print(f"Flag: {flag}")


if __name__ == "__main__":
    main()

# Flag: crypto{80e5212754a824d3a4aed185ace4f9cac0f908bf}
