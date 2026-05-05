p = 9739
a = 497
b = 1768

O = None 


def inv_mod(x, p):
    return pow(x, -1, p)


def point_add(P, Q):
    if P is None:
        return Q
    if Q is None:
        return P

    x1, y1 = P
    x2, y2 = Q

    # P + (-P)
    if x1 == x2 and (y1 + y2) % p == 0:
        return None

    if P != Q:
        lam = ((y2 - y1) * inv_mod(x2 - x1, p)) % p
    else:
        lam = ((3 * x1 * x1 + a) * inv_mod(2 * y1, p)) % p

    x3 = (lam * lam - x1 - x2) % p
    y3 = (lam * (x1 - x3) - y1) % p

    return (x3, y3)


def scalar_mult(n, P):
    R = None
    Q = P

    while n > 0:
        if n % 2 == 1:
            R = point_add(R, Q)
        Q = point_add(Q, Q)
        n //= 2

    return R


P = (2339, 2213)
n = 7863

Q = scalar_mult(n, P)

print("Q =", Q)

# Flag: crypto{9467, 2742}
